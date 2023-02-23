import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motor
coil_A_1_pin = 11
coil_A_2_pin = 13
coil_B_1_pin = 15
coil_B_2_pin = 16

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Define the step sequence for the motor
# sequence set, change comment for different step options
step_sequence = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

# Define the number of steps and delay between steps
num_steps = 512
delay = 0.005

# Run the motor
for i in range(num_steps):
    for step in range(8):
        GPIO.output(coil_A_1_pin, step_sequence[step][0])
        GPIO.output(coil_A_2_pin, step_sequence[step][1])
        GPIO.output(coil_B_1_pin, step_sequence[step][2])
        GPIO.output(coil_B_2_pin, step_sequence[step][3])
        time.sleep(delay)

# Clean up the GPIO pins
GPIO.cleanup()
