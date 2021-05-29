from time import sleep
import RPi.GPIO as GPIO

class Motor:


    def __init__(self, directionPin, stepPin):
        self.DIR = directionPin       # Direction GPIO Pin
        self.STEP = stepPin      # Step GPIO Pin
        self.CW = 1         # Clockwise Rotation
        self.CCW = 0        # Counterclockwise Rotation
        self.SPR = 800      # Steps per Revolution (360 / 1.8)
        self.DELAY = .005/1 # delay
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.output(self.DIR, self.CW)
        #MODE = (14, 15, 18) # Microstep Resolution GPIO Pins
        #GPIO.setup(MODE, GPIO.OUT)
        #RESOLUTION = {'Full': (0, 0, 0),'Half': (1, 0, 0),'1/4': (0, 1, 0),'1/8': (1, 1, 0),'1/16': (0, 0, 1),'1/32': (1, 0, 1)}
        #GPIO.output(MODE, RESOLUTION['Half'])

    def setDelay(self, delay):
        self.DELAY = delay

    def turn90CCW(self):
        GPIO.output(self.DIR, self.CW)
        sleep(.15)
        for x in range(int(self.SPR/4)):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.DELAY)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.DELAY)
    
    def turn90CW(self):
        GPIO.output(self.DIR, self.CCW)
        sleep(.15)
        for x in range(int(self.SPR/4)):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.DELAY)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.DELAY)

    def printdetails(self):
        print("This piano is a/an " , self.DIR , " foot")
        print(self.STEP, "piano, " , self.SPR, "years old and costing" , self.CW , " dollars.")
