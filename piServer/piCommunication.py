"""
import time
import multiprocessing
import psutil
import RPi.GPIO as GPIO
import board
import adafruit_vl53l4cd
from common.python_mqtt.mqtt_client import MQTTClient
"""
import sys

data = "python process spawned"
print(data)
sys.stdout.write(data)

"""
capture_number = 2 # Number of times robot pauses to capture
capture_interval = 15 # Time between captures

robot_ip = "192.168.8.209"
mqtt_client = MQTTClient(robot_ip)

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


# def run_motor():
#     #Rotates motor four quarter turns
#     ControlPin = [11, 13, 15, 16]
#     num_steps = 512 # Set the number of steps for a full rotation
#     delay = 0.001 # Set delay between steps
#     step_sequence = [[1,0,0,0],[1,1,0,0],
#                     [0,1,0,0],[0,1,1,0],
#                     [0,0,1,0],[0,0,1,1],
#                     [0,0,0,1],[1,0,0,1]] 

#     # Set up the GPIO pins
#     GPIO.setmode(GPIO.BOARD)
#     for pin in ControlPin:
#         GPIO.setup(pin, GPIO.OUT)
#         GPIO.output(pin,0)

#     # Run the motor
#     for i in range(num_steps):
#         for step in range(8):
#             for pin in range(4):
#                 GPIO.output(ControlPin[pin], step_sequence[step][pin])
#             time.sleep(delay)
#         if i % 128 == 0: # quarter turn has been completed
#             time.sleep(1.5)
#     rotation_complete.set()   

def ranging():
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
            print("reference dist:" + str(reference_distance))
            is_calibrated = True
            is_calibratedEvent.set()
        if distance < reference_distance - detection_threshold:
            detection.set()
            #print("detection!")
        else:     
            detection.clear()

def clean_robot():
    #retries cleaning until state verified   
    while not mqtt_client.is_cleaning():
        mqtt_client.clean()
        time.sleep(1)    

def pause_robot():
    #retries pausing until state verified
    while not mqtt_client.is_paused():
        mqtt_client.pause()
        time.sleep(1)

def dock_robot():
    #retries docking until state verified
    while not mqtt_client.is_docking():
        mqtt_client.dock()
        time.sleep(1)

def move_robot_off_dock_NO_VAC():
     if mqtt_client.is_docked():
        mqtt_client.clean()
        print("moving off dock")
        mqtt_client.set_fan_speed(0)
        time.sleep(5)
        pause_robot()
        print("pausing")

def obstacle_avoidance():
    pause_robot()
    while detection.is_set():
        mqtt_client.turn(30, floor_type="hard")
        time.sleep(1)


def basic_photo_run(capture_number: int, capture_interval: int):
    global robot_ip
    robot_ip = "192.168.8.209"
    global mqtt_client
    mqtt_client = MQTTClient(robot_ip)
    
    #robot_ip = "192.168.8.209"
    #mqtt_client = MQTTClient(robot_ip)
    
    capture_time = 5 # Amount of time robot pauses to capture
    
    move_robot_off_dock_NO_VAC()
    while not is_calibratedEvent.is_set():
        pass
    mqtt_client.resume()
    print("starting")
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        pause_robot()
        print("pausing for photo")
        #run_motor()
        #while not rotation_complete.is_set():
        #    pass
        time.sleep(capture_time)
        rotation_complete.clear()
        mqtt_client.resume()
        print("resuming photo run")
    capture_Complete.set()
    dock_robot()
    print("returning to dock")

# always trigger
captureProcess = multiprocessing.Process(target=basic_photo_run, args=(capture_number,capture_interval))
captureProcess.start()
captureProcessPID = captureProcess.pid
rangingProcess = multiprocessing.Process(target=ranging, daemon=False)
rangingProcess.start()


while not capture_Complete.set():
    while not detection.is_set():
        pass
    psutil.Process(pid=captureProcessPID).suspend()
    print("suspending")
    print(mqtt_client)
    obstacle_avoidance()
    psutil.Process(pid=captureProcessPID).resume()
    print("resuming")
    if mqtt_client.is_docked():
        continue
"""
