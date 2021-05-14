from time import sleep
import RPi.GPIO as GPIO

class Motor:

    def __init__(self):
        self.DIR = 20       # Direction GPIO Pin
        self.STEP = 21      # Step GPIO Pin
        self.CW = 1         # Clockwise Rotation
        self.CCW = 0        # Counterclockwise Rotation
        self.SPR = 200       # Steps per Revolution (360 / 1.8)

	
    def printdetails(self):
        print("This piano is a/an " , self.DIR , " foot")
        print(self.STEP, "piano, " , self.SPR, "years old and costing" , self.CW , " dollars.")
