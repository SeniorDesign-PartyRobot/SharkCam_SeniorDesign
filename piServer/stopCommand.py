from common.python_mqtt.mqtt_client import MQTTClient
import sys
import time

data = "stop command spawned"
print(data)

robot_ip = "192.168.8.209"
mqtt_client = MQTTClient(robot_ip)

while not mqtt_client.is_docking():
        mqtt_client.dock()
        time.sleep(1)

