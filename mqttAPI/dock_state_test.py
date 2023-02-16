import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"

mqtt_client = MQTTClient(robot_ip)  

mqtt_client.clean()
time.sleep(20)
mqtt_client.dock()
print(mqtt_client.verify_robot_state(7))
print(mqtt_client.verify_robot_state(7))
print(mqtt_client.verify_robot_state(14))