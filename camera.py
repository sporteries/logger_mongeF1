#!/usr/bin/python
import RPi.GPIO as GPIO
import picamera

class Camera(picamera.PiCamera):
    fileName = ""
    wait = 240
    
    def __init__(self, fileName, resolution = (640, 480), wait = 240):
        self.resolution = resolution
        self.fileName = fileName
        self.wait = wait
        
    def record(self):
        camera.start_recording(self.fileName)
        camera.wait_recording(self.wait)
        camera.stop_recording()
        





    

