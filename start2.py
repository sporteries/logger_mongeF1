#!/usr/bin/python
#from __future__ import print_function
import RPi.GPIO as GPIO
from led import Led
from bouton import Bouton
from camera import Camera
import picamera
from time import strftime
from time import sleep
from gyroscope import mpu6050
import os

#from gps import

#initialisation GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

recordCamera = False
camera = None
recordGps = False
gps = None
recordGyro = False
gyro = None
data = None
record = False
ledrouge = Led(17)
ledverte = Led(27)

def record_camera(record):
    global camera
    if record:
        print("start recording")
        camera =  picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording(strftime('/home/pi/video_%H:%M:%S.h264'))
        recordCamera = True
    else:
        print("stop recording")
        camera.stop_recording()
        camera.close()
        recordCamera = False

def record_gps(record):
    global gps
    if record:
        rercodGps = True
    else:
        recordGps = False

def record_gyro(record):
    global gyro
    if record:
        gyro = mpu6050(0x69)
        recordGyro = True
    else:
        recordGyro = False

def record_data():
    global data
    global record
    print("record data", data, id(data))
    if not record:
        record_camera(True)
        record_gps(True)
        record_gyro(True)
        record = True
    else:
        record_camera(False)
        record_gps(False)
        record_gyro(False)
        data.close()
        record = False

def write_data():
    global data
        if data is not None:
            print("record gyro",data, id(data))
            data.write(str(gyro.get_gyro_out())+"\t"+str(gyro.get_accel_out())+"\t"+str(gyro.get_rotation_x_y()))

def main():
    global data
    global record
    ledverte.on()
    sleep(5)
    data = open("/home/pi/gyro_gps_data.txt", "w")
    bouton1 = Bouton(23, record_data)
    ledverte.off()
    ledrouge.on()
    while 1:
        if record: 
		write_data():
	else:
            break
            sleep(0.1)
    ledrouge.off()
    ledverte.on()
    os.systen("shutdown -h now")

main()







