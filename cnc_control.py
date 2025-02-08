from servo import Servos
from RPi.GPIO as GPIO
from time import sleep

servos = Servos()
servos.move(360, 360)
sleep(2)
servos.move(360,180)

GPIO.cleanup()
