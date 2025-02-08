from servo import Servos
import RPi.GPIO as GPIO
from time import sleep

servos = Servos()
servos.move(360, 360)
sleep(2)
servos.move(360, 180)
sleep(2)
servos.move(180, 180)

GPIO.cleanup()
