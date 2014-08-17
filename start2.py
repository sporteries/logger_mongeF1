#!/usr/bin/python
import RPi.GPIO as GPIO
from time import *
import os
#from gps import*
from threading import Timer as Timer
#import picamera


#initialisation GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED_ON = 1
LED_OFF = 0
LED_BLINK = 2
LED_STOP_BLINK = 3

class led:
    channel = -1
    type = GPIO.OUT
    etat = LED_OFF
    isBlink = False
    thread = None
    isBlink = False
    iterBlink = 0
    oldTimer = None
    
    def __init__(self, channel):
        self.channel = channel
        if self.channel > -1:
            GPIO.setup(self.channel, self.type)
            self.status(LED_OFF)
            
    def status(self, etat):
        if etat == LED_ON:
            self.on()
        if etat == LED_OFF:
            self.off()
        self.etat = etat                  
            
    def on(self):
        self.etat == LED_ON           
        GPIO.output(self.channel, GPIO.HIGH)
        
    def off(self):
        self.etat == LED_OFF
        GPIO.output(self.channel, GPIO.LOW)  
        
    def blink(self, time, iterBlink):
        self.isBlink = True
        self.iterBlink = iterBlink
        self.repeat_blink(time)   
        
    def stop_blink(self):
        self.isBlink = False
        if self.oldTimer is not None:
            self.oldTimer.cancel()
        self.iterBlink = 0           
            
    def blink_thread(self, time):
        self.status(not self.etat)
        self.repeat_blink(time)
		
    def repeat_blink(self, time):
        if  self.iterBlink != 0:
            if self.iterBlink != -1:
                self.iterBlink -= 1
            t = Timer(time, self.blink_thread, args = [time])
            t.start()
            self.oldTimer = t


"""BOUTON_RISING = 0
BOUTON_FALLING = 1
BOUTON_BOTH = 2

class bouton:
    channel = -1
    etat = -1
    type = GPIO.IN
    falling = 0
    rising = 0
    def __init__(self, channel, func = [None], mode = GPIO.FALLING, args  = [()]):
        self.channel = channel
        self.func = func
	self.args = args
        if self.channel > -1:
            GPIO.setup(self.channel, self.type)
            GPIO.add_event_detect(self.channel, mode, self.execEvent)

    def execEvent(self, channel):
	for i, func in enumerate(self.func):
       	    if func is not None:
                func(*self.args[i])
    
    def status(self):
        etat =  GPIO.input(self.channel)
        return etat
"""
ledRouge = led(27)
ledVerte = led(17)
ledRouge.on()
sleep(2)
ledRouge.off()
sleep(2)
ledRouge.blink(1, 10)
"""capteur = gpsCapteur()
file = None
count = 0

def call():
    global count
    global file
    count += 1
    if count == 1:
	ledVerte.status(LED_OFF)
	ledRouge.status(LED_ON)
#	file = open("gpsdata.txt", "a")
	with picamera.PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.start_recording('/home/pi/video.h264')
		camera.wait_recording(240)
		camera.stop_recording()
    if count == 2:
	ledRouge.status(LED_OFF)
	ledVerte.status(LED_ON)
#	file.close()
	count = 0

def stop():
    global count
    if count == 0:
    	count = 3
	ledVerte.status(LED_OFF)
    

boutonStart = bouton(23, [call])
boutonExit = bouton(18, [stop])
ledVerte.status(LED_ON)

while count != 3:
#     dict = capteur.getValues()
#     if dict["longitude"] != 0.:
#	     if file is not None:
#	        if not file.closed:
#                    for i in dict:
#        	        file.write(str(dict[i]).replace(".", ",") + ";")
#                    file.write("\n")
		    ledRouge.status(LED_OFF)
		    time.sleep(.2)
		    ledRouge.status(LED_ON)
#while count != 3:
#os.systen("shutdown -h now")"""





    

