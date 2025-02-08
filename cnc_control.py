from servo import Servos
import RPi.GPIO as GPIO
from time import sleep

servos = Servos()
servos.move(360, 360)
sleep(2)
servos.move(360, 180)
sleep(2)
servos.move(180, 45)
sleep(2)
servos.move(90, 20)
sleep(2)
servos.move(45, 10)

GPIO.cleanup()
