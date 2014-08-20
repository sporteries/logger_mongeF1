#!/usr/bin/python
#from __future__ import print_function
import RPi.GPIO as GPIO
from led import Led
from bouton import Bouton
from camera import Camera
import picamera
from time import strftime
from gyroscope import mpu6050
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

def record_camera():
    pass
    """global recordCamera
    global camera
    if not recordCamera:
        print("start recording")
        camera =  picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording(strftime('/home/pi/video_%H:%M:%S.h264'))
        recordCamera = True
    else:
        print("stop recording")
        camera.stop_recording()
        camera.close()
        recordCamera = False"""

def record_gps():
    global recordGps
    global gps
    if not recordGps:
        rercodGps = True
    else:
        recordGps = False

def record_gyro():
    global recordGyro
    global gyro
    if not recordGyro:
        gyro = mpu6050(0x69)
        recordGyro = True
    else:
        recordGyro = False

def record_data(data):
    global data
    global record
    print(data, id(data))
    if not record:
        record_camera()
        record_gps()
        record_gyro()
        record = True
    else:
        data.close()

def write_data():
    global data
    if recordGps:
        pass
    if recordGyro:
        if data is not None:
            data.write(str(gyro.get_gyro_out())+"\t"+str(gyro.get_accel_out())+"\t"+str(gyro.get_rotation_x_y()))
def main():
    global data
    data = open("/home/pi/gyro_gps_data.txt", "w")
    bouton1 = Bouton(23, record_data, args = (data))
    print(data, id(data))
    while 1:
        write_data()


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







