#!/usr/bin/python
import RPi.GPIO as GPIO

BOUTON_RISING = 0
BOUTON_FALLING = 1
BOUTON_BOTH = 2

class Bouton:
    channel = -1
    etat = -1
    type = GPIO.IN
    falling = 0
    rising = 0
    func = None
    args = ()
    
    def __init__(self, channel, func = None, mode = GPIO.FALLING, args  = ()):
        self.channel = channel
        self.setFunc(func, args)
        if self.channel > -1:
            GPIO.setup(self.channel, self.type)
            GPIO.add_event_detect(self.channel, mode, self.execEvent)

    def execEvent(self, channel):
        if self.func is not None:
            self.func(*self.args) 
                
    def setFunc(self, func, args):
        self.func = func
        self.args = args
    
    def status(self):
        etat =  GPIO.input(self.channel)
        return etat




    

