#!/usr/bin/env python
import serial
import os.path

from longLatToDistAndHead import *
from obtainVel import *

#Define global variables
dist = None
bear = None
vel = None

#Definir puerto
gpsPort = serial.Serial("/dev/GPS", baudrate=115200, timeout=3.0)   

def logdataGps(i):
    f1 = os.path.join("data/dataFolder"+str(i), "gpggaGpsData.txt")
    f2 = os.path.join("data/dataFolder"+str(i), "gpvtgGpsData.txt")
    
    return f1, f2

def serial_reader():
    return gpsPort.readline()

def next(string, number):
    index1 = 0
    index2 = 0

    for i in range(number):
        index1 = index2
        index2 = string.find(",",index2)

    return string[index1:index2]

def talkerGps(f1, f2, pointList, pointNum):
    global dist, bear, vel
    
    ref = pointList[pointNum]
    
    for i in range (2):
        serial_data = serial_reader()
        
        if serial_data[0:6].decode('UTF-8') == "$GPGGA":
            f1.write(str(serial_data).strip("b'")+"\n")
            dist, bear = obtainValues(str(serial_data).strip("b'"), ref)
            
        elif serial_data[0:6].decode('UTF-8') == "$GPVTG":
            f2.write(str(serial_data).strip("b'")+"\n")
            vel = obtainVel(str(serial_data).strip("b'"))/3.6
        
    return dist, bear, vel