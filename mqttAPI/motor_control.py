import time
import RPi.GPIO as GPIO

def run_motor():
    print("Hello")

    # Set constants
    ControlPin = [11, 13, 15, 16]
    num_steps = 2048 # Set the number of steps for a full rotation
    delay = 0.0001 # Set delay between steps
    step_sequence = [[1,0,0,0],[1,1,0,0],
                    [0,1,0,0],[0,1,1,0],
                    [0,0,1,0],[0,0,1,1],
                    [0,0,0,1],[1,0,0,1]] 

    # Set up the GPIO pins
    GPIO.setmode(GPIO.BOARD)
    for pin in ControlPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)

    # Run the motor
    for i in range(num_steps):
        for step in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], step_sequence[step][pin])
            time.sleep(delay)
        if i % 512 == 0: # quarter turn has been completed
            time.sleep(0.5)
