import time

from common.python_mqtt.mqtt_client import MQTTClient

class MQTTFunctions(MQTTClient):


    def test_func(self):
        self.clean()

    def pause_robot(self):
        while MQTTClient.is_paused == False:
            MQTTClient.pause()
            time.sleep(1)

    def dock_robot(self):
        while MQTTClient.is_docking == False:
            MQTTClient.dock()
            time.sleep(1)

    def clean_NO_VAC(self):
        while MQTTClient.is_cleaning() == False:
            MQTTClient.set_fan_speed(0)
            MQTTClient.clean()
            time.sleep(1)

    def move_robot_off_dock_NO_VAC(self):
        if MQTTClient.is_docked(self):
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
            MQTTClient.resume()