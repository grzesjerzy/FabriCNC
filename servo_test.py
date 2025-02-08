import RPi.GPIO as GPIO
from time import sleep
motion = []


def move_servo(cw_a, cw_b, spr):
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

    GPIO.output(dir_a, cw_a)
    GPIO.output(dir_b, cw_b)

    delay = max(0.00015, 0)
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
    motor_resolution = 200
    relative_resolution = 10
    motion.clear()

    if abs(x_move) >= abs(y_move):
        ratio = int(abs((y_move / x_move) * relative_resolution))
        distance = int(motor_resolution * (abs(x_move) / 360))
        ratio_setup = (1, 0)
    else:
        ratio = int(abs((x_move / y_move) * relative_resolution))
        distance = int(motor_resolution * (abs(y_move) / 360))
        ratio_setup = (0, 1)

    for i in range(1, relative_resolution + 1):
        if i > ratio:
            motion.append(ratio_setup)
        else:
            motion.append((1, 1))

    if x_move < 0:
        dir_x = 1
    else:
        dir_x = 0

    if y_move < 0:
        dir_y = 1
    else:
        dir_y = 0

    move_servo(dir_x, dir_y, distance)


sleep_time = 1
move(360, 360)
sleep(sleep_time)
move(-180, 0)
sleep(sleep_time)
move(-45, -45)
sleep(sleep_time)
move(0, 90)
sleep(sleep_time)
move(200, -225)
sleep(sleep_time)
move(25, 180)
