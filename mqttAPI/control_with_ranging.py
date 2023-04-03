import time
import multiprocessing
import psutil
import board
import adafruit_vl53l4cd
from common.python_mqtt.mqtt_client import MQTTClient

capture_number = 2 # Number of times robot pauses to capture
capture_interval = 15 # Time between captures

timing_budget = 50 #sample rate (Hz)
inter_measurement = 0
i2c = board.I2C()  # uses board.SCL and board.SDA
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)
ToF.inter_measurement = inter_measurement
ToF.timing_budget = timing_budget

detection = multiprocessing.Event()
is_calibratedEvent = multiprocessing.Event()
captureComplete = multiprocessing.Event()

def ranging():
    print("ranging")
    ToF.start_ranging()  # start measurments
    is_calibrated = False
    detection_threshold = 5

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

def clean_robot():
    while not mqtt_client.is_paused():
        mqtt_client.pause()
        time.sleep(1)    

def pause_robot():
    while not mqtt_client.is_paused():
        mqtt_client.pause()
        time.sleep(1)

def dock_robot():
    while not mqtt_client.is_docking():
        mqtt_client.dock()
        time.sleep(1)

def move_robot_off_dock_NO_VAC():
     if mqtt_client.is_docked():
        mqtt_client.clean()
        mqtt_client.set_fan_speed(0)
        time.sleep(15)
        pause_robot()

def obstacle_avoidance():
    pause_robot()
    while detection.is_set():
        mqtt_client.turn(30, floor_type="hard")
        time.sleep(1)


def basic_photo_run(capture_number, capture_interval):
    global robot_ip
    robot_ip = "192.168.8.209"
    global mqtt_client
    mqtt_client = MQTTClient(robot_ip)
    
    capture_time = 5 # Amount of time robot pauses to capture
    
    move_robot_off_dock_NO_VAC()
    while not is_calibratedEvent.is_set():
        pass
    mqtt_client.resume()
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        pause_robot()
        time.sleep(capture_time)
        mqtt_client.resume()
    captureComplete.set()
    dock_robot()


if __name__ == "__main__":
    rangingProcess = multiprocessing.Process(target=ranging, daemon=False)
    rangingProcess.start()
    captureProcess = multiprocessing.Process(target=basic_photo_run, args=(capture_number,capture_interval))
    captureProcess.start()
    captureProcessPID = captureProcess.pid

    while not captureComplete.set():
        while not detection.is_set():
            pass
        psutil.Process(pid=captureProcessPID).suspend()
        print("detection!")
        obstacle_avoidance()
        psutil.Process(pid=captureProcessPID).resume()
        print("resuming")
        if mqtt_client.is_docked():
            continue