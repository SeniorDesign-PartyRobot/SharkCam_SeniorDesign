# python_mqtt
A way to communicate with robot using protobuf.

## Installation

Requires access to SharkNinja Bitbucket

Since this is still in development, please install using the following commands:
```bash
pip | pipenv install git+ssh://git@bitbucket.org/SharkNinja/automation-development.git/#egg=common
```
**On windows command prompt & key needs to be escaped with ^*
```bash
pip | pipenv install git+ssh://git@bitbucket.org/SharkNinja/automation-development.git/#egg=common
```


## Supported Commands and Returns:
The following examples will be using IP of 192.168.100.100
```python
from python_mqtt.mqtt_client import MQTTClient
client = MQTTClient('192.168.100.100')

MQTT Client has following options. 
"""
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
# Then you can do client.{functions listed below}
```
### Similarly these dictionaries can also be imported.
```python
from python_mqtt.mqtt_client import MQTTClient, UserCtrlSignalT, ErrorCodeT
```
```python
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
```
```python
    def is_connected(self) -> bool:
        """Return the mqtt connection status.

        Returns:
            bool: True if connection is established, false otherwise.
        """
```
```python
    def disconnect(self) -> None:
        """Safely disconnected the connection."""
```
```python
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
```
```python
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
```
```python
    def send_user_control(self, signal: int) -> None:
        """Send user controls. Takes in int equivaent of signals/commands.

        Args:
            signal (int): Interger value of the commands.
        """
```
```python
    def set_error(self, error: int) -> None:
        """Mock robot to have this error.

        Note: This has to be executed with 'clean' command to trigger error.
        This only sets the error. It does not trigger it.

        Args:
            error (int): Integer value of the error.
        """
```
```python
    def set_fan_speed(self, percent: int) -> None:
        """Set suction motor speed Effectively replacing power mode.

        Args:
            percent (int): Percentage to set power to.
        """
```
```python
    def set_bdp_cmd(self, cmd: str) -> None:
        """Send the bdp command.

        Note: This should be chained with get_bdp_value.
        The next get_bdp_value message should be the response to this request.

        Args:
            cmd (str): The query to send to robot.
        """
```
```python
    def verify_robot_state(self, val: int, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> bool:
        """Wait for robot state until timeout to go to stated value.

        Args:
            val (int): Interger value of the state.
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            bool: True if robot state was as expected. False otherwise.
        """
```
```python
    def get_bdp_value(self, wait_for_refresh: bool = True, timeout: int = __TIMEOUT) -> Any:
        """Return BDP Value.

        Note: THIS HAS NOT BEEN TESTED. DIRECT PORT OF NODEJS.

        Args:
            wait_for_refresh (bool, optional): Wait for refreshed value. Defaults to True.
            timeout (int, optional): Time to wait for. Defaults to __TIMEOUT.

        Returns:
            Any: BDP returned value. None if no value.
        """
```
```python
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
```
```python
    def clean(self) -> None:
        """Send clean command to robot."""
```
```python
    def pause(self) -> None:
        """Send pause command to robot."""
```
```python
    def dock(self) -> None:
        """Send dock command to robot."""
```
```python
    def explore(self) -> None:
        """Send explore command to robot."""
```
```python
    def eco(self) -> None:
        """Set power mode to eco."""
```
```python
    def max(self) -> None:
        """Set power mode to max."""
```
```python
    def normal(self) -> None:
        """Set power mode to normal."""
```
```python
    def is_cleaning(self) -> bool:
        """Verify the robot is cleaning.

        Returns:
            bool: True if cleaning, false otherwise.
        """
```
```python
    def is_paused(self) -> bool:
        """Verify the robot is paused.

        Returns:
            bool: True if paused, false otherwise.
        """
```
```python
    def is_docking(self) -> bool:
        """Verify the robot is docking.

        Returns:
            bool: True if docking, false otherwise.
        """
```
```python
    def is_exploring(self) -> bool:
        """Verify the robot is exploring.

        Returns:
            bool: True if exploring, false otherwise.
        """
```
```python
    def is_docked(self) -> bool:
        """Verify the robot is docked.

        Returns:
            bool: True if docked, false otherwise.
        """
```
```python
    def is_errored(self) -> bool:
        """Verify the robot is errored.

        Returns:
            bool: True if errored, false otherwise.
        """
```
```python
    def is_eco(self) -> bool:
        """Verify the robot is in eco mode.

        Returns:
            bool: True if eco, false otherwise.
        """
```
```python
    def is_max(self) -> bool:
        """Verify the robot is max mode.

        Returns:
            bool: True if max, false otherwise.
        """
```
```python
    def is_normal(self) -> bool:
        """Verify the robot is normal mode.

        Returns:
            bool: True if normal, false otherwise.
        """
```
```python
    def get_battery(self, wait_for_refresh: bool = False) -> int:
        """Return battery percentage.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            int: Current battery percentage.
        """
```
```python
    def get_error_codes(self, wait_for_refresh: bool = False) -> List[int]:
        """Get the current error codes.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            List[int]: Returns error codes in a List of ints. Empty List if there are no error.
        """
```
```python
    def get_warning_codes(self, wait_for_refresh: bool = False) -> List[int]:
        """Get the current warning codes.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            List[int]: Returns warning codes in a List of ints. Empty List if there are no error.
        """
```
```python
    def get_config(self, wait_for_refresh: bool = False) -> Dict[str, Union[int, Dict[str, int]]]:
        """Get the configs.

        Args:
            wait_for_refresh (bool, optional): If you want to wait for next pb output. Defaults to False.

        Returns:
            Dict[str, Union[int, Dict[str, int]]]: Returns the current config.
        """
```
```python
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
```
```python
    def play_audio_id(self, id: int) -> None:
        """Play audio using the id, if it exists.

        Note: Not all id numbers are linked to an audio. If such id is provided, no sound will be played.

        Args:
            id (int): Plays audio assigned to this id.
        """
```
```python
    def send_bdp_and_get_response(self, cmd: str, debug_level: str = None, quit_bdp: bool = True) -> str:
        """Combine set_bdp_cmd and get_bdp_value into one.

        Args:
            cmd (str): The query to send to the robot.
            debug_level (str, optional): If this command requires certain debug mode. Defaults to None.
            quit_bdp (bool, optional): If bdp mode to should be restored to *DS0. Defaults to True.

        Returns:
            str: The returned value for the query.
        """
```
```python
    def twist(self, linear_speed: int = 0, angular_speed: int = 0) -> None:
        """Move robot a certain way.

        Args:
            linearSpeed (int, optional): Forward speed.. Defaults to 0.
            angularSpeed (int, optional): Turn speed. Defaults to 0.
        """
```
```python
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
```
```python
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
```
```python
    def get_robot_info(self) -> str:
        """Get robot info. Equivalent to 'Device Info' page in robopad.

        Returns:
            str: Info under Device Info page in robopad.
        """
```
```python
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
```
```python
    def shell(self, cmd: str) -> str:
        """Connect to web shell in robot. Equivalent to 'Terminal'.

        Note: If you need to chain command, do so using &&
            Example: "cd tmp && ls -la"

        Args:
            cmd (str): shell command to send to.

        Returns:
            str: output of shell command.
        """
```
```python
    def reboot(self) -> str:
        """Reboot the robot.

        Returns:
            str: reboot
        """
```
```python
    def silent_eboot(self) -> None:
        """Reboot the robot but silent (same as nightly).
        """
```
```python
    def get_map(self, save_name: str = None) -> str:
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
```
```python
    def get_mcu_version(self) -> Dict[str, str]:
        """Return MCU Version.

        Returns:
            Dict[str, str]: Return Dict of Hardware, Bootloader, Firmware version.
        """
```
```python
    def get_mcu_hardware(self) -> str:
        """Return MCU Hardware version.

        Returns:
            str: Return MCU Hardware version.
        """
```
```python
    def get_mcu_bootloader(self) -> str:
        """Return MCU Bootloader version.

        Returns:
            str: Return MCU Bootloader version.
        """
```
```python
    def get_mcu_firmware(self) -> str:
        """Return MCU Firmware version.

        Returns:
            str: Return MCU Firmware version.
        """
```
```python
    def get_fw_version(self) -> str:
        """Return Firmware version.

        Returns:
            str: Return Firmware version.
        """
```
```python
    def get_app_version(self) -> str:
        """Return App version.

        Returns:
            str: Return App version.
        """
```
```python
    def get_scm_version(self) -> str:
        """Return SCM version.

        Returns:
            str: Return SCM version.
        """
```
```python
    def get_protobuf_version(self) -> str:
        """Return Protobuf version.

        Returns:
            str: Return Protobuf version.
        """
```
```python
    def get_build_time(self) -> str:
        """Return the buildtime for this firmware.

        Returns:
            str: Return the buildtime for this firmware.
        """
```
```python
    def get_host_info(self) -> str:
        """Return the host info.

        Returns:
            str: Return the host info.
        """
```
```python
    def get_mcusdk_version(self) -> str:
        """Return MCUSDK version.

        Returns:
            str: Return MCUSDK version.
        """
```
```python
    def get_vendor_info(self) -> str:
        """Return vendor info.

        Returns:
            str: Return vendor info.
        """
```
```python
    def get_dsn(self) -> str:
        """Return DSN.

        Returns:
            str: Return DSN.
        """
```
```python
    def get_region(self) -> str:
        """Return the region of the robot.

        Returns:
            str: Return the region of the robot.
        """
```
```python
    def get_mac(self) -> str:
        """Return mac for the robot.

        Returns:
            str: Return mac for the robot.
        """
```
```python
    def read_config(self, file_path: str) -> str:
        """Read config file on the given file path on the robot.

        Args:
            file_path (str): Location of the config file.

        Raises:
            LookupError: If the location is not valid.

        Returns:
            str: Config file content.
        """
```
```python
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
```
```python
    def overwrite_config(self, file_path: str, config_data: str) -> Type[requests.Response]:
        """Overwrite config file on the given file path with the config data provided.

        Args:
            file_path (str): Location of the config file.
            config_data (str): Config data to overwrite with.

        Returns:
            requests.Response: Response from the server.
        """
```
```python
    def check_file_exists(self, file_path: str) -> bool:
        """Check if the file exists on the robot.

        Args:
            file_path (str): Location of the file.

        Returns:
            bool: True if the file exists.
        """
```

***Note: There are internal methods starting with __, that are not documented in this README as they are not intended for external use. Calling them will cause Attribute Error.***


# bdp_decode
You will find another file called bdp_decoder.py along with this pull request. This file can decode bdp values returned by robot into a dictionary.
## Supported Commands and Returns:
```python
from python_mqtt.bdp_decoder import bdp_decode
```
You can use this as follows:

*There is also an BDPExamples enum provided for testing purposes*
```python
from python_mqtt.bdp_decoder import BDPExamples, bdp_decode
from python_mqtt.mqtt_client import MQTTClient

a = MQTTClient("192.168.86.146", client_log=False)
v = a.send_bdp_and_get_response("?BA", "*DS1")
translated = bdp_decode(v)

# Looping through the examples.
for _, y in BDPExamples.__members__.items():
    print(bdp_decode(y.value))
```
```python
def bdp_decode(data: str, extended: bool = False, append_units: bool = False) -> Dict[str, Union[str, int]]:
    """Decode string value to proper dictionary.

    Args:
        data (str): String version of the BDP Data.
        extended (bool, optional): If whole backend dictionary should be returned. Defaults to False.
        append_units (bool, optional): Append units where applicable. Defaults to False.

    Raises:
        ValueError: If input does not start with $.

    Returns:
        Dict[str, Union[str, int]]: Returns human readable dict.
    """
```
