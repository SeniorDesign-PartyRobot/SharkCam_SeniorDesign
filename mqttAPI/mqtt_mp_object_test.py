import time
import multiprocessing
from multiprocessing import Process, Value
import psutil
from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"
#mqtt_client = MQTTClient(robot_ip)

def pause_robot():
    """retries pausing until state verified"""
    while not mqtt_client.is_paused():
        mqtt_client.pause()
        time.sleep(1)

def clean_robot():
    """retries cleaning until state verified"""    
    while not mqtt_client.is_cleaning():
        mqtt_client.clean()
        time.sleep(1) 
        
def obstacle_avoidance():
    pause_robot()
    time.sleep(2)
    mqtt_client.turn(30, floor_type="hard")
    time.sleep(1)

def basic_photo_run():
    print("i exist")
    global mqtt_client
    var1 = 2
    var2 = 3
    print("vars initialized")
    #mqtt_client = MQTTClient(robot_ip)

    #for i in range(5):
    #    clean_robot()
    #    time.sleep(10)
    #    pause_robot()
    #    time.sleep(2)
    

if __name__ == "__main__":
    global var1
    var1 = 0
    captureProcess = multiprocessing.Process(target=basic_photo_run)
    captureProcess.start()
    if (not ('var1' in globals())):
        print("nope")
   
    captureProcessPID = captureProcess.pid
    #time.sleep(5)
    
    #print(var1)
    #print(var2)
    
    #time.sleep(5)
    #psutil.Process(pid=captureProcessPID).suspend()
    #print("suspending")
    #print(mqtt_client)
    #obstacle_avoidance()
    #psutil.Process(pid=captureProcessPID).resume()

    time.sleep(8)
    #obstacle_avoidance()
    
