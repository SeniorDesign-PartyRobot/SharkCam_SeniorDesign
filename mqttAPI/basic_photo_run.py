import time
from mqtt_functions import MQTTFunctions

robot_ip = "192.168.8.209"

mqtt_client = MQTTFunctions(robot_ip)

mqtt_client.clean_NO_VAC()

#capture_number = 2 # Number of times robot pauses to capture
#capture_interval = 10 # Time between captures

#mqtt_client.basic_photo_run(capture_number,capture_interval)
#mqtt_client.dock_robot()