import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"

mqtt_client = MQTTClient(robot_ip)


capture_number = 2 # Number of times robot pauses to capture
capture_interval = 10 # Time between captures

def pause_robot():
    while mqtt_client.is_paused == False:
        mqtt_client.pause()
        time.sleep(1)

def dock_robot():
    while mqtt_client.is_docking == False:
        mqtt_client.dock()
        time.sleep(1)

def clean_NO_VAC():
    while mqtt_client.is_cleaning() == False:
        mqtt_client.set_fan_speed(0)
        mqtt_client.clean
        time.sleep(1)

def move_robot_off_dock_NO_VAC():
     if mqtt_client.is_docked():
        clean_NO_VAC()
        time.sleep(15)
        pause_robot()


def basic_photo_run(capture_number, capture_interval):
    capture_time = 5 # Amount of time robot pauses to capture
    
    move_robot_off_dock_NO_VAC()
    clean_NO_VAC()
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        pause_robot()
        time.sleep(capture_time)
        clean_NO_VAC()

basic_photo_run(capture_number,capture_interval)
dock_robot()