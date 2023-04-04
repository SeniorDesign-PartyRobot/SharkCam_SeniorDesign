import time
import multiprocessing
import psutil
import RPi.GPIO as GPIO
import board
import adafruit_vl53l4cd
from common.python_mqtt.mqtt_client import MQTTClient

capture_number = 2 # Number of times robot pauses to capture
capture_interval = 15 # Time between captures

timing_budget = 50 # sample rate (Hz)
inter_measurement = 0 # time between samples
i2c = board.I2C()  # uses board.SCL and board.SDA
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)
ToF.inter_measurement = inter_measurement
ToF.timing_budget = timing_budget

detection = multiprocessing.Event()
is_calibratedEvent = multiprocessing.Event()
rotation_complete = multiprocessing.Event()
capture_Complete = multiprocessing.Event()

def ranging(mqtt_client):
    print("ranging")
    ToF.start_ranging()  # start measurments
    is_calibrated = False
    detection_threshold = 5 # change (cm) to trigger detection

    while True:
        while not ToF.data_ready:
            pass
        ToF.clear_interrupt()
        distance = ToF.distance
        if not is_calibrated:
            time.sleep(1)
            reference_distance = distance
            is_calibrated = True
            is_calibratedEvent.set()
        if distance < reference_distance - detection_threshold:
            detection.set()
        else:     
            detection.clear()

def clean_robot(mqtt_client):
    """retries cleaning until state verified"""    
    while not mqtt_client.is_cleaning():
        mqtt_client.clean()
        time.sleep(1)    

def pause_robot(mqtt_client):
    """retries pausing until state verified"""
    while not mqtt_client.is_paused():
        mqtt_client.pause()
        time.sleep(1)

def dock_robot(mqtt_client):
    """retries docking until state verified"""
    while not mqtt_client.is_docking():
        mqtt_client.dock()
        time.sleep(1)

def move_robot_off_dock_NO_VAC(mqtt_client):
     if mqtt_client.is_docked():
        mqtt_client.clean()
        mqtt_client.set_fan_speed(0)
        time.sleep(8)
        pause_robot(mqtt_client)

def obstacle_avoidance(mqtt_client):
    pause_robot(mqtt_client)
    while detection.is_set():
        mqtt_client.turn(30, floor_type="hard")
        time.sleep(1)


def basic_photo_run(capture_number: int, capture_interval: int, mqtt_client):
    global robot_ip
    robot_ip = "192.168.8.209"
    
    capture_time = 5 # Amount of time robot pauses to capture
    
    move_robot_off_dock_NO_VAC(mqtt_client)
    while not is_calibratedEvent.is_set():
        pass
    mqtt_client.resume()
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        pause_robot(mqtt_client)
        #run_motor()
        #while not rotation_complete.is_set():
        #    pass
        time.sleep(capture_time)
        rotation_complete.clear()
        mqtt_client.resume()
    capture_Complete.set()
    dock_robot(mqtt_client)


if __name__ == "__main__":

    manager = multiprocessing.Manager()
    shared_dict = manager.dict()

    robot_ip = "192.168.8.209"
    mqtt_client = MQTTClient(robot_ip)

    rangingProcess = multiprocessing.Process(target=ranging, args=(mqtt_client,), daemon=False)
    rangingProcess.start()

    captureProcess = multiprocessing.Process(target=basic_photo_run(capture_number, capture_interval, mqtt_client), daemon=False)
    captureProcess.start()
    while True:
        if capture_Complete.is_set():
            rangingProcess.terminate()
            captureProcess.terminate()
            break

    mqtt_client.disconnect()