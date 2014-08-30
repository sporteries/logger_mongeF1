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
recordAll = 0
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
    if record == 1:
        print("stop recording video")
        camera.stop_recording()
        camera.close()
        recordCamera = False

def record_gps(record):
    global gps
    if record == 0:
        rercodGps = True
    if record == 1:
        print("stop recording gps")        
        recordGps = False

def record_gyro(record):
    global gyro
    if record == 0:
        gyro = mpu6050(0x69)
        recordGyro = True
    if record == 1:
        print("stop recording gyro")        
        recordGyro = False

def record_data():
    global data
    global recordAll
    print("record data", data, id(data))
    if recordAll == 0:      
        record_camera(0)
        record_gps(0)
        record_gyro(0)
        recordAll = 1          
    if recordAll == 1:
        recordAll = 2           
        record_camera(1)
        record_gps(1)
        record_gyro(1)
        data.close()    

def write_data():
    if data.closed():
        print("record gyro",data, id(data))
        data.write(str(gyro.get_gyro_out())+"\t"+str(gyro.get_accel_out())+"\t"+str(gyro.get_rotation_x_y()))

def main():
    global data
    global recordAll
    global gyro
    ledverte.on()
    sleep(5)
    data = open("/home/pi/gyro_gps_data.txt", "w")
    bouton1 = Bouton(23, record_data)
    ledverte.off()
    ledrouge.on()
    while 1:
        if recordAll == 0:
            pass
        elif recordAll == 1:
            if gyro is None:
                print("gyro is NULL")
            write_data()
        elif recordAll == 2:
            break
    ledrouge.off()
    ledverte.on()
    #os.system("shutdown -h now")
    print("exit")

main()







