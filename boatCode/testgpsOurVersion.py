#!/usr/bin/env python
import serial
import os.path

from longLatToDistAndHead import *
from obtainVel import *

#Define global variables
distThrot = None
distRud = None
bear = None
refbearThrot = None
refbearRud = None
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
class msg_gpvtg1:
    time = np.uint64 

    # UTC seconds from midnight
    utc_seconds = np.float64

    vel = np.float32
    bear = np.float32
    
def gpvtg1(data):
    string = str(data)
    msg = msg_gpvtg1
    msg.time = int(round(t.time() * 1000))

    index1 = 0
    index2 = string.find(",")
    index1 = index2
    index2 = string.find(",", index2 + 1)
    if string[index1 + 1 : index2] == "":
        msg.bear = float(string[index1 +1: index2])
    else:
        msg.bear = float(string[index1 +1: index2])
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

def testtalkerGps(f1, f2, pointList, pointNumThrot, pointNumRud):
    global distThrot, distRud, bear, refbearThrot, refbearRud, vel
    
    refThrot = pointList[pointNumThrot]
    refRud = pointList[pointNumRud]
    
    for i in range (2):
        serial_data = serial_reader()
        
        if serial_data[0:6].decode('UTF-8') == "$GPGGA":
            f1.write(str(serial_data).strip("b'")+"\n")
            distThrot, refbearThrot = obtainValues(str(serial_data).strip("b'"), refThrot)
            distRud, refbearRud = obtainValues(str(serial_data).strip("b'"), refRud)
            
        elif serial_data[0:6].decode('UTF-8') == "$GPVTG":
            f2.write(str(serial_data).strip("b'")+"\n")
            vel = obtainVel(str(serial_data).strip("b'"))/3.6
            msg = gpvtg1(serial_data)
            bear = msg.bear
        
    return distThrot, distRud, bear, refbearThrot, refbearRud, vel