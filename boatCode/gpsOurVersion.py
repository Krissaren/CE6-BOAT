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
class msg_gpvtg:
    time = np.uint64 

    # UTC seconds from midnight
    utc_seconds = np.float64

    vel = np.float32
    
def gpvtg(data):
    string = str(data)
    msg = msg_gpvtg
    msg.time = int(round(time.time() * 1000))
    
    index1 = 0
    index2 = string.find("N")
    index1 = index2
    index2 = string.find(",", index2 + 1)
    index1 = index2
    index2 = string.find(",", index2 + 1)
    
    if string[index1 + 1:index2] == "":
        msg.vel = float(0)
    else:
        msg.vel = float(string[index1 + 1:index2])
    msg.utc_seconds = float(0)

    return msg

def talkerGps(f1, f2, pointList, pointNum):
    global dist, bear, vel
    
    ref = pointList[pointNum]
    
    for i in range (2):
        serial_data = serial_reader()
        
        if serial_data[0:6].decode('UTF-8') == "$GPGGA":
            f1.write(str(serial_data).strip("b'")+"\n")
            dist, refbear = obtainValues(str(serial_data).strip("b'"), ref)
            
        elif serial_data[0:6].decode('UTF-8') == "$GPVTG":
            f2.write(str(serial_data).strip("b'")+"\n")
            vel = obtainVel(str(serial_data).strip("b'"))/3.6
            msg = gpvtg(serial_data)
            bear = msg.
        
    return dist, bear, vel