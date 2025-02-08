import RPi.GPIO as GPIO
from time import sleep
motion = []


def move_servo(cw, spr):
    GPIO.setmode(GPIO.BOARD)
    dir_a = 8
    step_a = 10

    dir_b = 12
    step_b = 11

    micro = 32
    # spr = 200

    GPIO.setup(dir_a, GPIO.OUT)
    GPIO.setup(step_a, GPIO.OUT)
    GPIO.setup(dir_b, GPIO.OUT)
    GPIO.setup(step_b, GPIO.OUT)

    GPIO.output((dir_a, dir_b), cw)

    delay = max(0.0001, 0)
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


def move(x_move, y_move, direction):
    motor_resolution = 200
    linear_factor = 360 / 200

    resolution = 10
    motion.clear()
    if x_move >= y_move:
        ratio = y_move / x_move
        distance = motor_resolution * (x_move / 360)
    else:
        ratio = x_move / y_move
        distance = motor_resolution * (y_move / 360)

    ratio = ratio * resolution

    for i in range(1, resolution + 1):
        if i > ratio:
            motion.append((1, 0))
        else:
            motion.append((1, 1))

    move_servo(direction, distance)


move(360, 360, 1)
move(180, 0, 0)
