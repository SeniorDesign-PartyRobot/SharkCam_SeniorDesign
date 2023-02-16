import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"

mqtt_client = MQTTClient(robot_ip)    
        
def pause_robot():
    while mqtt_client.verify_robot_state(4) == False:
        mqtt_client.pause()
        time.sleep(1)

mqtt_client.clean()
time.sleep(15)
pause_robot()
time.sleep(5)