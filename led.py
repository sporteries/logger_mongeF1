#!/usr/bin/python
import RPi.GPIO as GPIO
from threading import Timer as Timer

LED_ON = 1
LED_OFF = 0
LED_BLINK = 2
LED_STOP_BLINK = 3

class Led:
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

    def on(self):
        self.etat == LED_ON
        GPIO.output(self.channel, GPIO.HIGH)

    def off(self):
        self.etat == LED_OFF
        self.stop_blink()
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
        self.etat = not self.etat
        self.status(self.etat)
        self.repeat_blink(time)

    def repeat_blink(self, time):
        if  self.iterBlink != 0:
            if self.iterBlink != -1:
                self.iterBlink -= 1
            t = Timer(time, self.blink_thread, args = [time])
            self.oldTimer = t
            t.start()







