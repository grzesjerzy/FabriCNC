from RPi.GPIO as GPIO
from time import sleep


class Servos:
    def __init__(self):
        self.delay = 0.00015
        self.dir_a = 8
        self.step_a = 10
        self.dir_b = 12
        self.step_b = 11
        self.micro_step = 32
        self.step_per_rotation = 200
        self.motion = []
        self.motors = (self.step_a, self.step_b)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.dir_a, GPIO.OUT)
        GPIO.setup(self.step_a, GPIO.OUT)
        GPIO.setup(self.dir_b, GPIO.OUT)
        GPIO.setup(self.step_b, GPIO.OUT)
        GPIO.output(self.dir_a, 1)
        GPIO.output(self.dir_b, 1)

    def move(self, x, y):

        x = (x / 360) * self.micro_step * self.step_per_rotation
        y = (y / 360) * self.micro_step * self.step_per_rotation
        self.create_pulsing_pattern(x, y)
        for n in range(len(self.motion)):
            GPIO.output(self.motors, self.motion[n])
            sleep(self.delay)
            GPIO.output(self.motors, GPIO.LOW)
            sleep(self.delay)

    def nwd(self, a, b):
        while b != 0:
            pom = b
            b = a % b
            a = pom
        return a

    def nww(self, a, b):
        return int(a / self.nwd(a, b) * b)

    def create_pulsing_pattern(self, x, y):
        self.motion.clear()
        int_nww = self.nww(x, y)

        for n in range(1, int_nww + 1):
            if n % (int_nww / x) == 0 and n % (int_nww / y) == 0:
                self.motion.append((1, 1))
            elif n % (int_nww / x) == 0:
                self.motion.append((1, 0))
            elif n % (int_nww / y) == 0:
                self.motion.append((0, 1))

        print(self.motion)

        x1 = 0
        y1 = 0
        for item in self.motion:
            x1 += item[0]
            y1 += item[1]

        print(x1)
        print(y1)
