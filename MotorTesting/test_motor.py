import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motor
print("Hello")
ControlPin = [11, 13, 15, 16]

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

# Define the step sequence for the motor
# sequence set, change comment for different step options
step_sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]

# Define the number of steps and delay between steps
num_steps = 512
delay = 0.001

# Run the motor
for i in range(num_steps):
    for step in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], step_sequence[step][pin])
        time.sleep(delay)

# Clean up the GPIO pins
GPIO.cleanup()
print("Goodbye")
