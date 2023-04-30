#Simple demo of the stepper motor, does a full rotation
import RPi.GPIO as GPIO
import time

def run_motor():
    print("Hello")

    # Set constants
    ControlPin = [11, 13, 15, 16] # Set the GPIO pins for the motor
    num_steps = 512 # Set the number of step
    delay = 0.001 # Set delay between steps
    step_sequence = [[1,0,0,0],[1,1,0,0], # Set the step sequence for the motor
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

    # Clean up the GPIO pins 
    GPIO.cleanup()
    print("Goodbye")

if __name__ == "__main__":
    run_motor()
