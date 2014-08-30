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

camera = None
gps = None
gyro = None
data = None
recordAll = 0
ledrouge = Led(17)
ledverte = Led(27)

# record_camera, record_gps et record_gyro prennent pour argument un booleen
# True : on commence l'enregistrement, False : on termine l'enregistrement
def record_camera(record):
    global camera
    if record:
        print("start recording")
        camera =  picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording(strftime('/home/pi/video_%H:%M:%S.h264'))
        recordCamera = True
    if not record:
        print("stop recording video")
        camera.stop_recording()
        camera.close()
        recordCamera = False

def record_gps(record):
    global gps
    if record:
        rercodGps = True
    if not record:       
        recordGps = False

def record_gyro(record):
    global gyro
    if record:
        gyro = mpu6050(0x69)
        recordGyro = True
    if not record:     
        recordGyro = False

def record_data():
    global data
    global recordAll
    print("record data", data, id(data))
    if recordAll == 0:      
        record_camera(True)
        record_gps(True)
        record_gyro(True)
        recordAll = 1 
        return
    if recordAll == 1:
        recordAll = 2           
        record_camera(False)
        record_gps(False)
        record_gyro(False)
        data.close()    

def write_data():
    if not data.closed: # si le fichier n'est pas ferme on enregistre
        data.write(str(gyro.get_gyro_out())+"\t"+str(gyro.get_accel_out())+"\t"+str(gyro.get_rotation_x_y()) + "\n")

def main():
    global data
    global recordAll
    ledverte.on()
    data = open("/home/pi/gyro_gps_data.txt", "w")
    bouton1 = Bouton(23, record_data)
    ledverte.off()
    ledrouge.on()
    while 1:
        if recordAll == 1:
            write_data()
        elif recordAll == 2:
            break
    ledrouge.off()
    ledverte.on()
    os.system("shutdown -h now")
    print("exit")

main()







