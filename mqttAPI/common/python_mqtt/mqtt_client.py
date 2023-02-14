"""Creates instances of mqtt connections."""
import base64
import inspect
import ipaddress
import json
import logging
import re
import secrets
import socket
import sys
import time
from enum import Enum
from math import radians
from typing import Any, ByteString, Dict, List, Type, Union
from tenacity import retry, stop_after_delay, wait_fixed

import paho.mqtt.client as mqtt
import requests

from . import constants
from .protobuf import PbDebug_pb2, PbInput_pb2, PbMessages_pb2, PbOutput_pb2

logging.basicConfig(
    filename="mqtt_client.log",
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# PbOutput
PbVersionT = {}
PriorityT = {}
SysStateT = {}
ErrorCodeT = {}
WarningCodeT = {}
PbToggleT = {}
StateSignalT = {}
WifiCtrT = {}
FloorControlT = {}
UltraCleanStateT = {}
ReloctStatus = {}
CarpetDetectModeT = {}

# PbInput
UserCtrlSignalT = {}


class CodeMapping(Enum):
    """Temporary mapping of pb_output and inputs."""

    # Note: These have to be camelCased due to MQTT exchange format.
    version = "PbVersionT"
    priority = "PriorityT"
    robotState = "SysStateT"
    errorCodes = "ErrorCodeT"
    warnCodes = "WarningCodeT"
    appConnected = "PbToggleT"
    stateSignal = "StateSignalT"
    wifiCtr = "WifiCtrT"
    powerOffSignal = "PbToggleT"
    mapUpdateOk = "PbToggleT"
    floorControl = "FloorControlT"
    DnDToggle = "PbToggleT"
    RRStatus = "PbToggleT"
    ERStatus = "PbToggleT"
    continueCrossHatchStatus = "PbToggleT"
    isRelocalizing = "PbToggleT"
    ultra_clean_state = "UltraCleanStateT"
    relocState = "ReloctStatus"
    isPriming = "PbToggleT"
    fanJetStatus = "PbToggleT"
    carpetDetectStatus = "CarpetDetectModeT"
    wetCleanState = "PbToggleT"


for name, variables in CodeMapping.__members__.items():
    for sub_name, sub_value in PbOutput_pb2._PBOUTPUT.fields_by_name[name].enum_type.values_by_name.items():
        globals()[variables.value][sub_name] = sub_value.number

for sub_name, sub_value in PbInput_pb2._PBINPUT.fields_by_name["UserCtr"].enum_type.values_by_name.items():
    globals()["UserCtrlSignalT"][sub_name] = sub_value.number


class MQTTClient:
    """Generates a instance of client that suscribes to mqtt server."""

    __TIMEOUT = 20

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 9006,
        timeout: int = __TIMEOUT,
        client_log: bool = False,
        backend_log: bool = False,
    ) -> None:
        """Initialize connection to robot.

        Note: __TIMEOUT has default value of 10 seconds.

        Args:
            host (str, optional): Hosts IP Address. Defaults to "127.0.0.1".
            port (int, optional): Port to connect to. Defaults to 9006.
            timeout (int, optional): Time to wait until the connection is established. Defaults to __TIMEOUT.
            client_log (bool, optional): Generate logs from functions. Defaults to False.
            backend_log (bool, optional): Should logger be attached to backend mqtt connection (High Spam Rate). \
                Defaults to False.

        Raises:
            ValueError:  If IP address is invalid.
            ConnectionError: If Connection is not established within the given timeout.
        """
        try:
            ipaddress.ip_address(host)
            socket.inet_aton(host)
        except Exception:
            raise ValueError(f"Could not connect to this IP address : {host}")

        connection_timeout = time.time() + timeout
        self.host = host
        self.port = port
        self.client_log = client_log
        self.methods = [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]
        self.__data = {
            constants.PBOUTPUT_TOPIC: {},
            constants.RVC_TOPIC: {},
            constants.ROBOTEST_LOG_TOPIC: {},
            "robopad_info": {},
        }
        self.__is_connected = False

        self.client = mqtt.Client(
            client_id=f"robotest_{secrets.token_hex(nbytes = 4)}",
            transport="websockets",
        )

        if not self.client_log:
            logging.getLogger("requests").setLevel(logging.WARNING)
            logging.getLogger("urllib3").setLevel(logging.WARNING)

        if backend_log:
            self.client.enable_logger(logger)

        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message
        self.client.on_disconnect = self.__on_disconnect
        self.client.connect_async(host, port)
        self.client.loop_start()

        # Allow time for connection.
        while not self.is_connected():
            if time.time() >= connection_timeout:
                raise ConnectionError(f"Unable to connect to {host} on port {port} within {timeout} seconds. "
                                      f"Make sure the firewall is disabled on robot (enable robopad)")

        # Give a second to populate infos.
        time.sleep(1)

    # The callback for when the client receives a CONNACK response from the server.
    def __on_connect(self, client: Type[mqtt.Client], userdata: Any, flags: Any, rc: int) -> None:
        """Suscribe to topics once connection is established.

        Args:
            client (Type[mqtt.Client]): Client connection.
            userdata (Any): Not Used.
            flags (Any): Not Used.
            rc (int): Connection result code.
        """
        print(f"Connected to {self.host} result code {rc}.")
        self.__write_log(f"Connected to {self.host} result code {rc}.")
        self.__is_connected = True
        topics = [
            constants.PBOUTPUT_TOPIC,
            constants.RVC_TOPIC,
            constants.ROBOTEST_LOG_TOPIC,
            "robopad_info",
        ]

        suscribe_to = []

        for topic in topics:
            suscribe_to.append((topic, 0))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe(suscribe_to)
        if constants.RVC_TOPIC in topics:
            self.__request_rvc()

        self.__populate_info_from_device_info()

    # The callback for when the client receives a disconnect response from the server.
    def __on_disconnect(self, client: Type[mqtt.Client], userdata: Any, rc: int) -> None:
        """Change connection status upon disconnect.

        Normally should not trigger, but if there is an issue,
        lets take care of it.

        Args:
            client (Type[mqtt.Client]): Client connection.
            userdata (Any): Not Used.
            rc (int): Connection result code.

        Raises:
            ConnectionError: If client gets disconnected unsafely (i.e not triggered by user), raise an error.
        """
        self.__is_connected = False
        self.__write_log(f"Connection to {self.host} disconnected with result code {rc}.")
        if rc != 0:
            raise ConnectionError(f"Connection to {self.host} disconnected with result code {rc}.")

    def __request_rvc(self) -> None:
        """Suscribe to rvc channel."""
        self.__write_log(self.client.publish("/robopad/readrvc", json.dumps({"count": 1000})))

    def __pb_output_to_dict(self, message: Type[PbOutput_pb2.PbOutput]) -> Dict[str, Any]:
        """Convert message sent as mqtt message over to dictionary.

        Args:
            message (Type[PbOutput_pb2.PbOutput]): Pb output message.

        Returns:
            dict[str, Any]: Returns a dict with str keys and values.
        """
        message_dict = {}

        for descriptor in message.DESCRIPTOR.fields:
            key = descriptor.name
            value = getattr(message, descriptor.name)

            if descriptor.label == descriptor.LABEL_REPEATED:
                message_list = []

                for sub_message in value:
                    if descriptor.type == descriptor.TYPE_MESSAGE:
                        message_list.append(self.__pb_output_to_dict(sub_message))
                    else:
                        message_list.append(sub_message)

                message_dict[key] = message_list
            else:
                if descriptor.type == descriptor.TYPE_MESSAGE:
                    message_dict[key] = self.__pb_output_to_dict(value)
                else:
                    message_dict[key] = value
        return message_dict

    def __rvc_output_to_dict(self, message: str) -> dict:
        return json.loads(re.sub(r"([{,])(\s*)([A-Za-z0-9_\-]+?)\s*:", r'\1"\3":', message.replace("\n", "")))

    # The callback for when a PUBLISH message is received from the server.
    def __on_message(self, client: Type[mqtt.Client], userdata: Any, msg: Type[PbOutput_pb2.PbOutput]) -> None:
        """When a message is recieved from robot, emit it to other event listener.

        Args:
            client (Type[mqtt.Client]): mqtt client connection.
            userdata (Any): Not Used.
            msg (Type[PbOutput_pb2.PbOutput]): Mqtt message.
        """
        if msg.topic == constants.PBOUTPUT_TOPIC:
            pb_output = None
            try:
                _buffer = base64.b64decode(msg.payload)
                pb_output = PbOutput_pb2.PbOutput()
                pb_output.ParseFromString(_buffer)
            except Exception as e:
                print("PbOutput.deserializeBinary error")
                print(e)
                return
            self.__data[constants.PBOUTPUT_TOPIC] = self.__pb_output_to_dict(pb_output)
        elif msg.topic == constants.RVC_TOPIC:
            self.__data[constants.RVC_TOPIC] = self.__rvc_output_to_dict(msg.payload.decode("utf-8"))
        else:
            self.__data[msg.topic] = msg.payload.decode("utf-8")

    def __send_cmd(self, pb_input: Type[PbInput_pb2.PbInput]) -> None:
        """Send PB Input message to robot by serializing it.

        Args:
            pbInput (Type[PbInput_pb2.PbInput]): PB Input message.
        """
        pb_input_str = base64.b64encode(pb_input.SerializeToString())
        self.__write_log(self.client.publish(constants.PBINPUT_TOPIC, pb_input_str))

    def __write_log(self, log_message: Any) -> None:
        """Write log appending information about robot and traceback calls.

        Args:
            log_message (Any): Message to log.
        """
        if not self.client_log:
            return
        traceback_functions = ""
        frame = 0
        while True:
            # Fix for when things are offloaded to a thread.
            # Tries to traceback to original thread and errors.
            try:
                method = sys._getframe(frame).f_code.co_name
            except ValueError:
                break
            # If we are at the module that called us, break.
            if method == "<module>":
                break
            if method in self.methods:
                traceback_functions = traceback_functions + f" | [{method}]"
            frame += 1
        logging.debug(f"[MQTTClient] | [{self.host}]{traceback_functions} : {log_message}")

    def __log_then_return(self, data: Any) -> Any:
        """Write log then returns the value.

        Args:
            data (Any): Data to write in the log.

        Returns:
            Any: Returns original data.
        """
        self.__write_log(data)
        return data

    def __search_device_info(self, match_word: str, match_in: str) -> Union[str, None]:
        """Match regrex and return the value after :.

        Args:
            match_word (str): Word to match for.
            match_in (str): What to match word from.

        Returns:
            Union[str, None]: Return string right of : if there is match, None otherwise.
        """
        _match = re.search(rf"{match_word}:(\S+)", match_in)
        if _match:
            return _match.group(1)
        return None

    def __populate_info_from_device_info(self) -> None:
        """Populate self.device_info values using device info function."""
        _device_info = self.get_robot_info().replace("\t", "").replace(" ", "")
        self.device_info = {}
        self.device_info["MCUVersion"] = {}
        self.device_info["MCUVersion"]["Hardware"] = self.__search_device_info("HardWare", _device_info)
        self.device_info["MCUVersion"]["Bootloader"] = self.__search_device_info("Bootloader", _device_info)
        self.device_info["MCUVersion"]["Firmware"] = self.__search_device_info("Firmware", _device_info)
        self.device_info["FWVersion"] = self.__search_device_info("FWVersion", _device_info)
        self.device_info["APPVersion"] = self.__search_device_info("APPVersion", _device_info)
        self.device_info["SCMVersion"] = self.__search_device_info("SCMVersion", _device_info)
        self.device_info["PRO_BUFVersion"] = self.__search_device_info("PRO_BUFVersion", _device_info)
        self.device_info["BuildTime"] = self.__search_device_info("BuildTime", _device_info)
        self.device_info["HostInfo"] = self.__search_device_info("HostInfo", _device_info)
        self.device_info["MCUSDKVersion"] = self.__search_device_info("MCUSDKVersion", _device_info)
        self.device_info["VendorInfo"] = self.__search_device_info("VendorInfo", _device_info)
        self.device_info["dsn"] = self.__search_device_info("dsn", _device_info)
        self.device_info["region"] = self.__search_device_info("region", _device_info)
        self.device_info["mac"] = "".join(self.__search_device_info("MAC", _device_info).split(":"))

    """
    ############################# Everything
    ############################# under
    ############################# this
    ############################# is
    ############################# exposed
    ############################# and
    ############################# callable.
    """

    def is_connected(self) -> bool:
        """Return the mqtt connection status.

        Returns:
            bool: True if connection is established, false otherwise.
        """
        return self.__is_connected

    def disconnect(self) -> None:
        """Safely disconnected the connection."""
        self.__write_log(self.client.disconnect())

    def get_pb_output(
        self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT
    ) -> Dict[str, Union[str, int, list, dict]]:
        """Return the pb output message converted to dictionary.

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): [description]. Time to wait for. Defaults to __TIMEOUT.

        Raises:
            TimeoutError: If the data was not received the given time.

        Returns:
            Dict[str, Union[str, int, list, dict]]: Returns pb output message in dictionary form.
        """
        try_until = time.time() + timeout
        while not bool(self.__data[constants.PBOUTPUT_TOPIC]):
            if time.time() > try_until:
                raise TimeoutError(f"Pb Output was not received within {timeout}seconds.")
            continue
        if not wait_for_refresh:
            return self.__log_then_return(self.__data[constants.PBOUTPUT_TOPIC])

        curr_id = self.__data[constants.PBOUTPUT_TOPIC]["msgID"]

        while curr_id == self.__data[constants.PBOUTPUT_TOPIC]["msgID"] and self.is_connected():
            if time.time() > try_until:
                raise TimeoutError(f"Pb Output was not received within {timeout} seconds.")
            continue
        return self.__log_then_return(self.__data[constants.PBOUTPUT_TOPIC])

    def get_rvc_data(
        self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT
    ) -> Dict[str, Union[str, int, list, dict]]:
        """Return the rvc message converted to dictionary.

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): [description]. Time to wait for. Defaults to __TIMEOUT.

        Raises:
            TimeoutError: If the data was not received the given time.

        Returns:
            Dict[str, Union[str, int, list, dict]]: Returns rvc data in dictionary form.
        """
        # Sometimes the rvc messages stops, request it again just to be safe.
        self.__request_rvc()
        try_until = time.time() + timeout
        while not bool(self.__data[constants.RVC_TOPIC]):
            if time.time() > try_until:
                raise TimeoutError(f"RVC was not received within {timeout} seconds.")
            continue

        if not wait_for_refresh:
            return self.__log_then_return(self.__data[constants.RVC_TOPIC])

        curr_id = self.__data[constants.RVC_TOPIC]["frame_id"]

        while curr_id == self.__data[constants.RVC_TOPIC]["frame_id"] and self.is_connected():
            if time.time() > try_until:
                raise TimeoutError(f"RVC was not received within {timeout} seconds.")
            continue
        return self.__log_then_return(self.__data[constants.RVC_TOPIC])

    def send_user_control(self, signal: int) -> None:
        """Send user controls. Takes in int equivaent of signals/commands.

        Args:
            signal (int): Interger value of the commands.
        """
        pb_input = PbInput_pb2.PbInput()
        pb_input.UserCtr = signal
        self.__write_log(self.__send_cmd(pb_input))

    def set_error(self, error: int) -> None:
        """Mock robot to have this error.

        Note: This has to be executed with 'clean' command to trigger error.
        This only sets the error. It does not trigger it.

        Args:
            error (int): Integer value of the error.
        """
        pb_input = PbInput_pb2.PbInput()
        pb_input.errorCodes.append(error)
        self.__write_log(self.__send_cmd(pb_input))

    def set_fan_speed(self, percent: int) -> None:
        """Set suction motor speed Effectively replacing power mode.

        Mapping seems to be:
            0 = 0 || 1 - 50 = 50 (eco) || 51 - 75 = 82 (normal) || 76+ = 100 (max)

        Args:
            percent (int): Percentage to set power to.
        """
        pb_input = PbInput_pb2.PbInput()
        pb_input.config.cleanMode.fanSpeed = percent
        self.__write_log(self.__send_cmd(pb_input))

    def set_bdp_cmd(self, cmd: str) -> None:
        """Send the bdp command.

        Note: This should be chained with get_bdp_value.
        The next get_bdp_value message should be the response to this request.

        Args:
            cmd (str): The query to send to robot.
        """
        dbg_settings = PbDebug_pb2.PbDbgSetting()
        dbg_settings.bdpInput = cmd
        pb_input = PbInput_pb2.PbInput()
        pb_input.debugSetting.CopyFrom(dbg_settings)
        self.__write_log(self.__send_cmd(pb_input))

    def verify_robot_state(self, val: int, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> bool:
        """Wait for robot state until timeout to go to stated value.

        Args:
            val (int): Interger value of the state.
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            bool: True if robot state was as expected. False otherwise.
        """
        robot_state = self.get_robot_state(wait_for_refresh, timeout)
        return self.__log_then_return(robot_state is not None and val == robot_state)

    def get_robot_state(self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> int:
        """Get current robot state

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            Any: current robot state
        """
        return self.__log_then_return(
            self.get_pb_output(wait_for_refresh=wait_for_refresh, timeout=timeout)["robotState"])

    def get_robot_state_as_str(self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> str:
        """Get current robot state

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            str: current robot state as str

        """
        robot_state = self.get_robot_state(wait_for_refresh, timeout)
        return self.__log_then_return([key for key, value in SysStateT.items() if value == robot_state][0])

    def get_bdp_value(self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> Any:
        """Return BDP Value.

        Note: THIS HAS NOT BEEN TESTED. DIRECT PORT OF NODEJS.

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            Any: BDP returned value. None if no value.
        """
        obj = self.get_pb_output(wait_for_refresh=wait_for_refresh, timeout=timeout)
        if obj["dbgInfo"]:
            return self.__log_then_return(obj["dbgInfo"])
        return self.__log_then_return(None)

    def get_data(
        self, obj_keys: str, wait_for_refresh: bool = True, timeout: int = __TIMEOUT
    ) -> Union[None, Union[int, str, dict]]:
        """Return data corresponding to one of the PB_OUTPUT_KEYS.

        Args:
            obj_keys (str): Keys corresponding to PB_OUTPUT_KEYS
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Raises:
            TimeoutError: If no data is returned within the given time.time()

        Returns:
            Union[None, Union[int, str, dict]]: Returns data depending on the keys. None if no value.
        """
        pb_output_keys = [
            "msgID",
            "version",
            "priority",
            "robotState",
            "errorCodes",
            "warnCodes",
            "mapOut",
            "config",
            "deviceInfo",
            "appConnected",
            "netConfig",
            "deviceProfile",
            "audioID",
            "otaInfo",
            "baseControl",
            "ppOutput",
            "vtOutput",
            "rpcAck",
            "dbgInfo",
            "stateSignal",
            "wifiCtr",
            "powerCtr",
            "powerOffSignal",
            "mapUpdateOk",
            "currentLanguagePkg",
            "modulesRequest",
            "audioFile",
            "floorControl",
            "floorControlParams",
            "DnDToggle",
            "diagnoseInfo",
            "RRStatus",
            "ERStatus",
            "internalOutput",
            "continueCrossHatchStatus",
            "isRelocalizing",
            "ultra_clean_state",
            "relocState",
            "isPriming",
            "fanJetStatus",
            "carpetDetectStatus",
            "wetCleanState",
        ]
        output = self.get_pb_output(wait_for_refresh=wait_for_refresh, timeout=timeout)
        if obj_keys in pb_output_keys and output[obj_keys] is not None:
            return self.__log_then_return(output[obj_keys])
        return self.__log_then_return(None)

    """
    ############################# Everything
    ############################# under
    ############################# this
    ############################# is
    ############################# Utility.
    """

    def clean(self) -> None:
        """Send clean command to robot."""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_AUTO"]))

    def pause(self) -> None:
        """Send pause command to robot."""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_PAUSE"]))

    def resume(self) -> None:
        """Send resume command to robot. This is sent to resume cleaning when robot is paused"""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_RESUME"]))

    def dock(self) -> None:
        """Send dock command to robot."""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_DOCK"]))

    def explore(self) -> None:
        """Send explore command to robot."""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_AUTO_EXPLORE"]))

    def eco(self) -> None:
        """Set power mode to eco."""
        self.__write_log(self.set_fan_speed(50))

    def max(self) -> None:
        """Set power mode to max."""
        self.__write_log(self.set_fan_speed(100))

    def normal(self) -> None:
        """Set power mode to normal."""
        self.__write_log(self.set_fan_speed(70))

    def is_cleaning(self) -> bool:
        """Verify the robot is cleaning.

        Returns:
            bool: True if cleaning, false otherwise.
        """
        return self.__log_then_return(self.verify_robot_state(SysStateT["SYS_ST_CLEANING"]))

    def is_paused(self) -> bool:
        """Verify the robot is paused.

        Returns:
            bool: True if paused, false otherwise.
        """
        return self.__log_then_return(self.verify_robot_state(SysStateT["SYS_ST_PAUSE"]))

    def is_docking(self) -> bool:
        """Verify the robot is docking.

        Returns:
            bool: True if docking, false otherwise.
        """
        return self.__log_then_return(self.verify_robot_state(SysStateT["SYS_ST_DOCKING"]))

    def is_exploring(self) -> bool:
        """Verify the robot is exploring.

        Returns:
            bool: True if exploring, false otherwise.
        """
        return self.__log_then_return(self.verify_robot_state(SysStateT["SYS_ST_AUTO_EXPLORE"]))

    def is_docked(self) -> bool:
        """Verify the robot is docked.

        Returns:
            bool: True if docked, false otherwise.
        """
        return self.__log_then_return(
            self.get_data("robotState") in [SysStateT["SYS_ST_CHARGING"], SysStateT["SYS_ST_BATTERY_FULL"]]
        )

    def is_errored(self) -> bool:
        """Verify the robot is errored.

        Returns:
            bool: True if errored, false otherwise.
        """
        return self.__log_then_return(self.verify_robot_state(SysStateT["SYS_ST_ERROR"]))

    def is_eco(self) -> bool:
        """Verify the robot is in eco mode.

        Returns:
            bool: True if eco, false otherwise.
        """
        return self.get_fan_speed() == 50

    def is_max(self) -> bool:
        """Verify the robot is max mode.

        Returns:
            bool: True if max, false otherwise.
        """
        return self.get_fan_speed() == 100

    def is_normal(self) -> bool:
        """Verify the robot is normal mode.

        Returns:
            bool: True if normal, false otherwise.
        """
        return 82 >= self.get_fan_speed() >= 80

    @retry(stop=stop_after_delay(30), wait=wait_fixed(1))
    def verify_power_mode(self, expected_mode):
        """ Verifies and waits until robot is in the given mode

        Returns:
            None
        """
        current_fan_speed = self.get_fan_speed()
        if expected_mode.lower() == "eco":
            assert self.is_eco(), f"Robot is not in eco mode; Current fan speed {current_fan_speed}"
        elif expected_mode.lower() == "max":
            assert self.is_max(), f"Robot is not in max mode Current fan speed {current_fan_speed}"
        elif expected_mode.lower() == "normal":
            assert self.is_normal(), f"Robot is not in normal mode Current fan speed {current_fan_speed}"
        else:
            raise ValueError(f"Unknown power mode: {expected_mode}")

    def get_fan_speed(self) -> int:
        """
        Get the current fan speed

        Returns:
            int: value 50 - 100
        """
        return self.__log_then_return(self.get_data("baseControl")["fanSpeed"])

    def get_battery(self, wait_for_refresh: bool = False) -> int:
        """Return battery percentage.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            int: Current battery percentage.
        """
        return self.__log_then_return(self.get_data("deviceInfo", wait_for_refresh=wait_for_refresh)["battery"])

    def get_error_codes(self, wait_for_refresh: bool = False) -> List[int]:
        """Get the current error codes.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            List[int]: Returns error codes in a List of ints. Empty List if there are no error.
        """
        return self.__log_then_return(self.get_data("errorCodes", wait_for_refresh=wait_for_refresh))

    def get_warning_codes(self, wait_for_refresh: bool = False) -> List[int]:
        """Get the current warning codes.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            List[int]: Returns warning codes in a List of ints. Empty List if there are no error.
        """
        return self.__log_then_return(self.get_data("warnCodes", wait_for_refresh=wait_for_refresh))

    def get_config(self, wait_for_refresh: bool = False) -> Dict[str, Union[int, Dict[str, int]]]:
        """Get the configs.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            Dict[str, Union[int, Dict[str, int]]]: Returns the current config.
        """
        return self.__log_then_return(self.get_data("config", wait_for_refresh=wait_for_refresh))

    def get_map_out(
        self, wait_for_refresh: bool = False
    ) -> List[Dict[str, Union[int, float, list, Dict[str, Union[int, float, ByteString, list]]]]]:
        """Get the current map output.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            List[Dict[str, Union[int, float, list, Dict[str, Union[int, float, ByteString, list]]]]]: Returns the map \
                output.
        """
        return self.__log_then_return(self.get_data("mapOut", wait_for_refresh=wait_for_refresh))

    def play_audio_id(self, id: int) -> None:
        """Play audio using the id, if it exists.

        Note: Not all id numbers are linked to an audio. If such id is provided, no sound will be played.

        Args:
            id (int): Plays audio assigned to this id.
        """
        pb_input = PbInput_pb2.PbInput()
        pb_input.audioID = id
        self.__write_log(self.__send_cmd(pb_input))

    def send_bdp_and_get_response(self, cmd: str, debug_level: str = None, quit_bdp: bool = True) -> str:
        """Combine set_bdp_cmd and get_bdp_value into one.

        Args:
            cmd (str): The query to send to the robot.
            debug_mode (str, optional): If this command requires certain debug mode. Defaults to None.
            quit_bdp (bool, optional): If bdp mode to should be restored to *DS0. Defaults to True.

        Returns:
            str: The returned value for the query.
        """
        if debug_level:
            self.set_bdp_cmd(debug_level)
        self.set_bdp_cmd(cmd)
        # try three times to fetch the value
        returned_value = ''
        i = 1
        while (returned_value == '' or cmd in (returned_value)) and i <= 3:
            returned_value = self.get_bdp_value()["bdpOutput"]
            i += 1
        
        if quit_bdp:
            self.set_bdp_cmd("*DS0")
        return self.__log_then_return(returned_value)

    def twist(self, linear_speed: int = 0, angular_speed: int = 0) -> None:
        """Move robot a certain way.

        Args:
            linearSpeed (int, optional): Forward speed.. Defaults to 0.
            angularSpeed (int, optional): Turn speed. Defaults to 0.
        """
        tw = PbMessages_pb2.PbTwist()
        tw.linearSpeed = linear_speed
        tw.angularSpeed = angular_speed
        pb_input = PbInput_pb2.PbInput()
        pb_input.twist.CopyFrom(tw)
        self.__write_log(self.__send_cmd(pb_input))

    def move(self, inch: int, floor_type: str = "hard", factor: int = 1) -> None:
        """Move robot by given inch.

        Args:
            inch (int): Distance to move.
            floor_type (str, optional): Floor type determines how long it takes. Defaults to "hard".
            factor (int, optional): If you want to speed up the process. Higher factor = less accuracy. Defaults to 1.

        Raises:
            ValueError: If inch is negative.
            ValueError: If floor type is not hard or carpet.
            ValueError: If factor is less than or equal to 0 or greater than 10.
        """
        if inch <= 0:
            raise ValueError("inch has to be a positive integer. inch provided: {inch}.")
        if floor_type not in ["hard", "carpet"]:
            raise ValueError(
                f"floor_type must be one of the following: 'hard' |'carpet'. floor_type provided : {floor_type}"
            )
        if 0 <= factor > 10:
            raise ValueError(
                f"Only int between 0(exclusive) and 10(inclusive) is allowed for factor. factor provided : {factor}"
            )
        _conversion_variable = 2.15 if floor_type == "hard" else 2
        _time_required = time.time() + inch / (factor * _conversion_variable)

        while time.time() < _time_required:
            self.twist(linear_speed=factor * 0.0575)
            time.sleep(0.025)
        self.pause()

    def turn(self, degree: int, floor_type: str = "hard", factor: int = 1) -> None:
        """Turn robot by certain degree.

        Note: Passing in negative degree turns the robot clockwise. Positive = counter clockwise, Negative = clockwise.

        Args:
            degree (int): Degree to turn to.
            floor_type (str, optional): Floor type determines how long it takes. Defaults to "hard".
            factor (int, optional): If you want to speed up the process. Higher factor = less accuracy. Defaults to 1.

        Raises:
            ValueError: If floor type is not hard or carpet.
            ValueError: If factor is less than or equal to 0 or greater than 10.
        """
        if floor_type not in ["hard", "carpet"]:
            raise ValueError(
                f"floor_type must be one of the following: 'hard' |'carpet'. floor_type provided : {floor_type}"
            )
        if 0 <= factor > 10:
            raise ValueError(
                f"Only int between 0(exclusive) and 10(inclusive) is allowed for factor. factor provided : {factor}"
            )
        _turn_direction = 1
        if degree == 0:
            return
        if degree < 0:
            _turn_direction = -1
            degree = degree * _turn_direction

        _conversion_variable = 11 if floor_type == "hard" else 10
        _time_required = time.time() + degree / (factor * _conversion_variable)

        while time.time() < _time_required:
            self.twist(angular_speed=_turn_direction * factor * radians(11))
            time.sleep(0.025)
        self.pause()

    def wiggle_robot(self, turn_degree: int = 90, move_inches: int = 5) -> None:
        """ Turn robot 90 degrees and move forward 5 inches (both can be overridden with parameters.

        This is mainly used to get the robot unstuck, especially in the case of a bumper error.

        """
        self.__write_log("Turning robot 90 degrees")
        self.turn(turn_degree)
        time.sleep(5)

        self.__write_log("Moving robot 5 inches")
        self.move(move_inches)
        time.sleep(10)

    def get_robot_info(self) -> str:
        """Get robot info. Equivalent to 'Device Info' page in robopad.

        Returns:
            str: Info under Device Info page in robopad.
        """
        response = requests.get(url=f"http://{self.host}:8080/main.cgi?action=version")
        response.raise_for_status()
        return self.__log_then_return(response.text)

    def get_logs(self, save_name: str = None, include_mnt: bool = False) -> str:
        """Pull log from robot and save.

        Note: If save_name is not provided, file is saved under current timestamp in following format:
                %Y_%m_%d_%H_%M_%S.tar.gz. File will be saved under the cwd.

        Args:
            save_name (str, optional): Save name. Defaults to None.
            include_mnt (bool, optional): If whole mnt folder should be included.
                Defaults to False. This options takes about 2 minute.
                The following path are excluded:
                    "mnt/res/hw_test",
                    "mnt/res/lost+found",
                    "mnt/res/stress_test",
                    "mnt/udisk/auto*",
                    "mnt/udisk/console*",
                    "mnt/udisk/www",
                    "mnt/udisk/webdir"

        Returns:
            str: save file name.
        """
        if save_name is None:
            _time = time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime(time.time()))
            save_name = f"logs_{self.get_mac()}_{_time}.tar.gz"

        self.__write_log("Generating logs...")

        if include_mnt:
            _include = ["/tmp", "/mnt"]
            _exclude = [
                "mnt/res/hw_test",
                "mnt/res/lost*",
                "mnt/res/stress_test",
                "mnt/udisk/auto*",
                "mnt/udisk/console*",
                "mnt/udisk/www",
                "mnt/udisk/webdir",
            ]

            _shell_cmd = "time -p tar -czvf logs.tar.gz"

            for stuff in _include:
                _shell_cmd = f"{_shell_cmd} {stuff}"
            for stuff in _exclude:
                _shell_cmd = f"{_shell_cmd} --exclude='{stuff}'"

            _shell_cmd = f"{_shell_cmd} > /dev/null"

            self.__write_log("Removing tmplogs folder (if one exists)...")
            self.shell("rm -rf tmplogs && sync")

            self.__write_log("Creating temporary logs folder (tmplogs)...")
            self.shell("mkdir tmplogs && sync")

            self.__write_log("Zipping contents to logs.tar.gz...Will take approximately 100 seconds...")
            print("Zipping contents to logs.tar.gz...Will take approximately 100 seconds...")
            self.shell(f"cd tmplogs && {_shell_cmd} && sync")

            self.__write_log("Fetching logs...")

            pull_log = requests.get(url=f"http://{self.host}:8080/tmplogs/logs.tar.gz")
            pull_log.raise_for_status()

            self.__write_log("Removing tmplogs folder...")
            self.shell("rm -rf tmplogs && sync")
        else:
            generate_log = requests.get(url=f"http://{self.host}:8080/main.cgi?action=logs")
            generate_log.raise_for_status()

            self.__write_log("Fetching logs...")

            pull_log = requests.get(url=f"http://{self.host}:8080/log/tmp.tar.gz")
            pull_log.raise_for_status()

        self.__write_log("Fetching success. Attempting to save...")

        with open(save_name, "wb") as f:
            f.write(pull_log.content)

        self.__write_log(f"Saving success. Filename: {save_name}")
        return save_name

    def shell(self, cmd: str) -> str:
        """Connect to web shell in robot. Equivalent to 'Terminal'.

        Note: If you need to chain command, do so using &&
            Example: "cd tmp && ls -la"

        Args:
            cmd (str): shell command to send to.

        Returns:
            str: output of shell command.
        """
        self.__write_log(f"Sending {cmd} to robot shell.")

        response = requests.get(url=f"http://{self.host}:8080/web_shell.cgi?cmd={cmd}")
        response.raise_for_status()
        return self.__log_then_return(response.text)

    def reboot(self) -> str:
        """Reboot the robot.

        Returns:
            str: reboot
        """
        return self.__write_log(self.shell("reboot"))

    def silent_reboot(self) -> None:
        """Reboot the robot but silent (same as nightly)."""
        self.__write_log(self.send_user_control(UserCtrlSignalT["USR_CTR_WARM_BOOT"]))

    def get_map(self, save_name: str = None, qfeel: bool = True) -> str:
        """Get map from robot and save it as png.

        Note: If save_name is not provided, file is saved under current timestamp in following format:
                %Y_%m_%d_%H_%M_%S.jpg. File will be saved under the cwd.

        Args:
            save_name (str, optional): Save name. Defaults to None.
            qfeel (bool, optional): If map info should be sent to qfeel (map.qfeeltech.com) for better \
                results. Defaults to True.

        Returns:
            str: save file name.
        """
        if save_name is None:
            _time = time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime(time.time()))
            save_name = f"map_{self.get_mac()}_{_time}.png"

        if qfeel:
            self.__write_log("Temporarily coping map from /mnt/udisk/map/default_map.pb...")

            self.shell("cp /mnt/udisk/map/default_map.pb default_map_copy.pb")

            self.__write_log("Fetching default_map.pb...")

            _get_map_from_robot = requests.get(url=f"http://{self.host}:8080/default_map_copy.pb")
            _get_map_from_robot.raise_for_status()
            _default_map_pb = _get_map_from_robot.content

            # Surpress Insecure Request Warning.
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

            self.__write_log("Sending default_map.pb to map.qfeeltech.com to be parsed...")

            _upload_to_qfeel = requests.post(
                url="https://map.qfeeltech.com/upload",
                data={"type": "lidar"},
                files={"file": ("default_map.pb", _default_map_pb)},
                verify=False,
            )
            _upload_to_qfeel.raise_for_status()
            self.__write_log("Fetching image from map.qfeeltech.com...")

            _get_map_from_qfeel = requests.get(
                url=f"https://map.qfeeltech.com/static/uploads/upload_default_map.pb.png?t={time.time()}", verify=False
            )
            _get_map_from_qfeel.raise_for_status()

            self.__write_log("Fetching success. Attempting to save...")
            with open(save_name, "wb") as f:
                f.write(_get_map_from_qfeel.content)

            self.__write_log(f"Saving success. Filename: {save_name}")

            self.__write_log("Removing default_map_copy.pb...")

            self.shell("rm default_map_copy.pb")
        else:
            self.__write_log("Fetching map...")

            response = requests.get(url=f"http://{self.host}:8080/main.cgi?action=read_map")
            response.raise_for_status()

            self.__write_log("Fetching success. Attempting to save...")

            with open(save_name, "wb") as f:
                f.write(response.content)

            self.__write_log(f"Saving success. Filename: {save_name}")
        return save_name

    def get_mcu_version(self) -> Dict[str, str]:
        """Return MCU Version.

        Returns:
            Dict[str, str]: Return Dict of Hardware, Bootloader, Firmware version.
        """
        return self.__log_then_return(self.device_info["MCUVersion"])

    def get_mcu_hardware(self) -> str:
        """Return MCU Hardware version.

        Returns:
            str: Return MCU Hardware version.
        """
        return self.__log_then_return(self.device_info["MCUVersion"]["Hardware"])

    def get_mcu_bootloader(self) -> str:
        """Return MCU Bootloader version.

        Returns:
            str: Return MCU Bootloader version.
        """
        return self.__log_then_return(self.device_info["MCUVersion"]["Bootloader"])

    def get_mcu_firmware(self) -> str:
        """Return MCU Firmware version.

        Returns:
            str: Return MCU Firmware version.
        """
        return self.__log_then_return(self.device_info["MCUVersion"]["Firmware"])

    def get_fw_version(self) -> str:
        """Return Firmware version.

        Returns:
            str: Return Firmware version.
        """
        return self.__log_then_return(self.device_info["FWVersion"])

    def get_app_version(self) -> str:
        """Return App version.

        Returns:
            str: Return App version.
        """
        return self.__log_then_return(self.device_info["APPVersion"])

    def get_scm_version(self) -> str:
        """Return SCM version.

        Returns:
            str: Return SCM version.
        """
        return self.__log_then_return(self.device_info["SCMVersion"].split(":")[1])

    def get_protobuf_version(self) -> str:
        """Return Protobuf version.

        Returns:
            str: Return Protobuf version.
        """
        return self.__log_then_return(self.device_info["PRO_BUFVersion"])

    def get_build_time(self) -> str:
        """Return the buildtime for this firmware.

        Returns:
            str: Return the buildtime for this firmware.
        """
        return self.__log_then_return(self.device_info["BuildTime"])

    def get_host_info(self) -> str:
        """Return the host info.

        Returns:
            str: Return the host info.
        """
        return self.__log_then_return(self.device_info["HostInfo"])

    def get_mcusdk_version(self) -> str:
        """Return MCUSDK version.

        Returns:
            str: Return MCUSDK version.
        """
        return self.__log_then_return(self.device_info["MCUSDKVersion"])

    def get_vendor_info(self) -> str:
        """Return vendor info.

        Returns:
            str: Return vendor info.
        """
        return self.__log_then_return(self.device_info["VendorInfo"])

    def get_dsn(self) -> str:
        """Return DSN.

        Returns:
            str: Return DSN.
        """
        return self.__log_then_return(self.device_info["dsn"])

    def get_region(self) -> str:
        """Return the region of the robot.

        Returns:
            str: Return the region of the robot.
        """
        return self.__log_then_return(self.device_info["region"])

    def get_mac(self) -> str:
        """Return mac for the robot.

        Returns:
            str: Return mac for the robot.
        """
        return self.__log_then_return(self.device_info["mac"])

    def read_config(self, file_path: str) -> str:
        """Read config file on the given file path on the robot.

        Args:
            file_path (str): Location of the config file.

        Raises:
            LookupError: If the location is not valid.

        Returns:
            str: Config file content.
        """
        self.__write_log(f"Reading config file located at {file_path}")

        response = requests.get(url=f"http://{self.host}:8080/main.cgi?action=read_config&file={file_path}")
        response.raise_for_status()

        if "failed" in response.text:
            self.__write_log(f"No such file or directory at {file_path}.")
            raise LookupError(f"No such file or directory at {file_path}. Please check the file path.")

        return self.__log_then_return(response.text)

    def update_config(self, file_path: str, key_value: Dict[str, Union[str, int]]) -> Type[requests.Response]:
        """Update config file on the given file path on the robot.

        Args:
            file_path (str): Location of the config file.
            key_value (Dict[str, Union[str, int]]): Key value pairs to update.
                *For example: {"enable_aed": 0, "enable_reclean_via_charge": 0}
                *Note, booleans are passed in as lower cased string aswell.

        Raises:
            ValueError: If the key does not exist in the config file.

        Returns:
            requests.Response: Response from the server.
        """
        text = self.read_config(file_path)

        for key, value in key_value.items():
            _match = re.search(rf"({key}\s+=\s+)(\S+)", text)

            if not _match:
                raise ValueError(f"{file_path} does not contain {key}.")

            self.__write_log(f"Changing {_match.group(1)}{_match.group(2)} => {_match.group(1)}{value}")
            text = re.sub(rf"({key}\s+=\s+)(\S+)", rf"\g<1>{value}", text)

        self.__write_log(f"Updating config file located at {file_path}")
        response = requests.post(
            url=f"http://{self.host}:8080/main.cgi", data={"action": "set_config", "file": file_path, "params": text}
        )
        response.raise_for_status()
        return self.__log_then_return(response)

    def overwrite_config(self, file_path: str, config_data: str) -> Type[requests.Response]:
        """Overwrite config file on the given file path with the config data provided.

        Args:
            file_path (str): Location of the config file.
            config_data (str): Config data to overwrite with.

        Returns:
            requests.Response: Response from the server.
        """
        self.__write_log(f"Overwriting config file located at {file_path}")
        response = requests.post(
            url=f"http://{self.host}:8080/main.cgi",
            data={"action": "set_config", "file": file_path, "params": config_data},
        )
        response.raise_for_status()
        return self.__log_then_return(response)

    def check_file_exists(self, file_path: str) -> bool:
        """Check if the file exists on the robot.

        Args:
            file_path (str): Location of the file.

        Returns:
            bool: True if the file exists.
        """
        self.__write_log(f"Checking if file exists at {file_path}")

        response = self.shell(f"[ -e {file_path} ] && echo 1 || echo 0")
        return bool(response.split("\n")[1])
