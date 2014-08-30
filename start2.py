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
record = 0
ledrouge = Led(17)
ledverte = Led(27)

def record_camera(record):
    global camera
    if record == 0:
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
    if record == 0:
        rercodGps = True
    else:
        recordGps = False

def record_gyro(record):
    global gyro
    if record == 0:
        gyro = mpu6050(0x69)
        recordGyro = True
    else:
        recordGyro = False

def record_data():
    global data
    global record
    print("record data", data, id(data))
    if record == 0:      
        record_camera(record)
        record_gps(record)
        record_gyro(record)
        record = 1          
    else:
        record_camera(record)
        record_gps(record)
        record_gyro(record)
        data.close()
        record = 2       

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
        if record == 0 or record == 1: 
            write_data()
        else:
            break
    ledrouge.off()
    ledverte.on()
    #os.system("shutdown -h now")
    print("exit")

main()







