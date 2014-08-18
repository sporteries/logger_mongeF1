#!/usr/bin/python
import RPi.GPIO as GPIO
from time import *
from led import Led
from bouton import Bouton
from camera import Camera
import picamera

#initialisation GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

record = 0 # 0 : init, 1 : record, -1 : end
camera = None

def record_camera():
    global record
    global camera
    if record == 0:
        print("start recording")
        camera =  picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('/home/pi/video.h264')
        record = 1
    elif record == 1:
        #camera.wait_recording(240)
        print("stop recording")
        camera.stop_recording()
        camera.close()
        record = -1

def main():
    bouton1 = Bouton(23, record_camera)
    while 1:
        pass


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
#   file = open("gpsdata.txt", "a")
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_recording('/home/pi/video.h264')
        camera.wait_recording(240)
        camera.stop_recording()
    if count == 2:
    ledRouge.status(LED_OFF)
    ledVerte.status(LED_ON)
#   file.close()
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
#        if file is not None:
#           if not file.closed:
#                    for i in dict:
#                   file.write(str(dict[i]).replace(".", ",") + ";")
#                    file.write("\n")
            ledRouge.status(LED_OFF)
            time.sleep(.2)
            ledRouge.status(LED_ON)
#while count != 3:
#os.systen("shutdown -h now")"""
main()







