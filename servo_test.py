import RPi.GPIO as GPIO
from time import sleep
motion = []


def move_servo():
    GPIO.setmode(GPIO.BOARD)
    dir_a = 8
    step_a = 10

    dir_b = 12
    step_b = 11

    cw = 1
    ccw = 0
    micro = 32
    spr = 200

    GPIO.setup(dir_a, GPIO.OUT)
    GPIO.setup(step_a, GPIO.OUT)
    GPIO.setup(dir_b, GPIO.OUT)
    GPIO.setup(step_b, GPIO.OUT)

    GPIO.output((dir_a, dir_b), cw)

    delay = 0.004 / micro
    motors = (step_a, step_b)

    resolution = len(motion)
    step_count = int((spr * micro)/resolution)

    for x in range(step_count):
        for n in range(resolution):
            GPIO.output(motors, motion[n])
            sleep(delay)
            GPIO.output(motors, GPIO.LOW)
            sleep(delay)

    GPIO.cleanup()


def move(x_move, y_move):
    resolution = 10
    if x_move >= y_move:
        ratio = y_move / x_move
    else:
        ratio = x_move / y_move

    ratio = ratio * resolution

    for i in range(0, resolution):
        if i < ratio:
            motion.append((1, 1))
        else:
            motion.append((1, 0))

    move_servo()


move(2, 1)
