# Inpired by VL53L4CD APi documentation from: Copyright (c) 2022 Carter Nelson for Adafruit Industries

import time
import multiprocessing
import psutil
import board
import adafruit_vl53l4cd

timing_budget = 50
inter_measurement = 0

i2c = board.I2C()  # uses board.SCL and board.SDA
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)
ToF.inter_measurement = inter_measurement
ToF.timing_budget = timing_budget

detection = multiprocessing.Event()
distance = 4

def ranging():
    print("ranging")
    ToF.start_ranging()  # start measurments

    while True:
        while not ToF.data_ready:
            pass
        #print("fuck off")
        ToF.clear_interrupt()
        distance = ToF.distance
        #(distance)
        if distance < 2:
            detection.set()

def hello():
    while True: #not detection.is_set():
        print("hello")
        time.sleep(2)
        print("hello again")
        time.sleep(2)


if __name__ == "__main__":
    rangingProcess = multiprocessing.Process(target=ranging, daemon=False)
    rangingProcess.start()
    helloProcess = multiprocessing.Process(target=hello, daemon=False)
    helloProcess.start()

    helloProcessID = helloProcess.pid

    while True:
        while not detection.is_set():
            pass
        detection.clear()
        psutil.Process(pid=helloProcessID).suspend()
        print("detection!")
        time.sleep(3)
        psutil.Process(pid=helloProcessID).resume()
        print("resuming")
