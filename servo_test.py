import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
DIR_A = 8
STEP_A = 10

DIR_B = 12
STEP_B = 11

DIR_C = 13
STEP_C = 15

CW = 1
CCW = 0
micro = 16
SPR = 200

GPIO.setup(DIR_A, GPIO.OUT)
GPIO.setup(STEP_A, GPIO.OUT)
GPIO.setup(DIR_B, GPIO.OUT)
GPIO.setup(STEP_B, GPIO.OUT)

GPIO.output((DIR_A, DIR_B), CCW)

delay = 0.004 / micro
motors = (STEP_A, STEP_B)

motion = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
          (1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]
resolution = len(motion)
step_count = int((SPR * micro)/resolution)

for x in range(step_count):
    for n in range(resolution):
        GPIO.output(motors, motion[n])
        sleep(delay)
        GPIO.output(motors, GPIO.LOW)
        sleep(delay)

GPIO.cleanup()
