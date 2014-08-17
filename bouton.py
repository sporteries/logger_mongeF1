#!/usr/bin/python
import RPi.GPIO as GPIO

#initialisation GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BOUTON_RISING = 0
BOUTON_FALLING = 1
BOUTON_BOTH = 2

class bouton:
    channel = -1
    etat = -1
    type = GPIO.IN
    falling = 0
    rising = 0
    func = []
    args = []
    
    def __init__(self, channel, func = [], mode = GPIO.FALLING, args  = []):
        self.channel = channel
        self.setFunc(func, args)
        if self.channel > -1:
            GPIO.setup(self.channel, self.type)
            GPIO.add_event_detect(self.channel, mode, self.execEvent)

    def execEvent(self, channel):
	for i, func in enumerate(self.func):
            func(*self.args[i])
                
    def setFunc(func, args = [()]):
        self.func = func
        self.args = args
    
    def status(self):
        etat =  GPIO.input(self.channel)
        return etat




    

