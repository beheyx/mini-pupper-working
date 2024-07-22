from src.MovementGroup import MovementGroups

Move = MovementGroups()

#start, introducing pupper
#pupper says hello, dance, etc.
# Move.head_ellipse()
# Move.look_up()
# Move.look_down()
# Move.stop()

import RPi.GPIO as GPIO

def touch_init():
    # There are 4 areas for touch actions
    # Each GPIO to each touch area
    touchPin_Front = 6
    touchPin_Left  = 3
    touchPin_Right = 16
    touchPin_Back  = 2

    # Use GPIO number but not PIN number
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO numbers to input
    GPIO.setup(touchPin_Front, GPIO.IN)
    GPIO.setup(touchPin_Left,  GPIO.IN)
    GPIO.setup(touchPin_Right, GPIO.IN)
    GPIO.setup(touchPin_Back,  GPIO.IN)


if __name__ == "__main__":


    touchPin_Front = 6
    touchPin_Left  = 3
    touchPin_Right = 16
    touchPin_Back  = 2

    # Use GPIO number but not PIN number
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO numbers to input
    GPIO.setup(touchPin_Front, GPIO.IN)
    GPIO.setup(touchPin_Left,  GPIO.IN)
    GPIO.setup(touchPin_Right, GPIO.IN)
    GPIO.setup(touchPin_Back,  GPIO.IN)


    while True:
        


MovementLib = Move.MovementLib