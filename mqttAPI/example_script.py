import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "10.221.203.1"

mqtt_client = MQTTClient(robot_ip)


def move_robot_off_dock():
    if mqtt_client.is_docked():
        mqtt_client.clean()
        time.sleep(15)
        mqtt_client.pause()


move_robot_off_dock()

# Turn robot 90 degrees counter clockwise
mqtt_client.turn(90, floor_type="hard")

# Move robot forward 20 inches
mqtt_client.move(20, floor_type="hard")

# Turn robot 90 degrees counter clockwise
mqtt_client.turn(90, floor_type="hard")

# Move robot forward 20 inches
mqtt_client.move(20, floor_type="hard")

# Turn robot 180 degrees clockwise
mqtt_client.turn(180, floor_type="hard")

time.sleep(10)

# Send robot back to dock
mqtt_client.dock()
