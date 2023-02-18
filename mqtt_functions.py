import time

from common.python_mqtt.mqtt_client import MQTTClient

class MQTTFunctions(MQTTClient):

    def pause_robot(self):
        while self.is_paused == False:
            self.pause()
            time.sleep(1)

    def dock_robot(self):
        while self.is_docking == False:
            self.dock()
            time.sleep(1)

    def clean_NO_VAC(self):
        while self.is_cleaning() == False:
            self.set_fan_speed(0)
            self.clean
            time.sleep(1)

    def move_robot_off_dock_NO_VAC(self):
        if self.is_docked():
            self.clean_NO_VAC()
            time.sleep(15)
            self.pause_robot()

    def basic_photo_run(self, capture_number, capture_interval):
        capture_time = 5 # Amount of time robot pauses to capture
    
        self.move_robot_off_dock_NO_VAC()
        self.clean_NO_VAC()
    
        for i in range(capture_number):
            time.sleep(capture_interval)
            self.pause_robot()
            time.sleep(capture_time)
            self.clean_NO_VAC()