import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "10.221.203.1"

mqtt_client = MQTTClient(robot_ip)


capture_number = 1 # Number of times robot pauses to capture
capture_interval = 10 # Time between captures

def move_robot_off_dock():
    if mqtt_client.is_docked():
        mqtt_client.clean()
        time.sleep(15)
        mqtt_client.pause()


def basic_photo_run(capture_number, capture_interval):
    capture_time = 5 # Amount of time robot pauses to capture
    
    move_robot_off_dock()
    mqtt_client.clean()
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        mqtt_client.pause()
        time.sleep(capture_time)
        mqtt_client.clean()
    
    mqtt_client.dock()

basic_photo_run(capture_number,capture_interval)
