from servo import Servos
import RPi.GPIO as GPIO
from time import sleep

servos = Servos()
for n in range(10):
    servos.move(360, 360)
    sleep(1)
    servos.move(360, 180)
    sleep(1)
    servos.move(180, 45)
    sleep(1)
    servos.move(90, 19.8)
    sleep(1)
    servos.move(45, 10.8)
    sleep(1)
    servos.move(45, 10.8)
    sleep(1)
    servos.move(45, 10.8)
    sleep(1)
    servos.move(315, 82.8)
    sleep(1)

GPIO.cleanup()
