# Inpired by VL53L4CD APi documentation from: Copyright (c) 2022 Carter Nelson for Adafruit Industries

# Simple demo of the VL53L4CD distance sensor.
# Will print the sensed range/distance every second.

import board
import adafruit_vl53l4cd

# set constants
min_distance = 5
timing_budget = 200
inter_measurement = 0

# start script
print("Hello")
print("--------------------")
flag = 0

i2c = board.I2C()  # uses board.SCL and board.SDA
ToF = adafruit_vl53l4cd.VL53L4CD(i2c)
ToF.inter_measurement = inter_measurement
ToF.timing_budget = timing_budget

ToF.start_ranging()  # start measurments
for i in range(10):
    while not ToF.data_ready:
        pass
    ToF.clear_interrupt()
    print("Distance: {} cm".format(ToF.distance))
    if ToF.distance <= min_distance and ToF.distance != 0.0:
        flag = 1
        print("too close")

print("--------------------")
print("Goodbye")
