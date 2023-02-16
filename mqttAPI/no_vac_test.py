import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"

mqtt_client = MQTTClient(robot_ip,timeout=60)

def move_robot_off_dock_NO_VAC():
     if mqtt_client.is_docked():
        #mqtt_client.set_fan_speed(0)
        mqtt_client.clean()
        time.sleep(15)
        mqtt_client.pause()

move_robot_off_dock_NO_VAC()
#time.sleep(30)