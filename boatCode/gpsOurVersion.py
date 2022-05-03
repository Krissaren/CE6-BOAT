#!/usr/bin/env python
import string
import numpy as np
import serial
import os.path
from longLatToDistAndHead import *
from obtainVel import *

i = 1
#gpsPort = serial.Serial("/dev/GPS", baudrate=115200, timeout=3.0)
    
class coord:
    lat = np.float64    
    lon = np.float64

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

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

def createPointList():
    #Code for the path planning and returns a list with all the points (lon,lat)
    global pointList
    
    point1 = coord(57.05853139607721, 9.87175894295371)
    point2 = coord(57.05877432742965, 9.872404241980814)
    point3 = coord(57.059179209484505, 9.871792035211508)
    point4 = coord(57.058504403606584, 9.869988507161391)
    point5 = coord(57.057784597150466, 9.871295651344504)
    point6 = coord(57.05871134537982, 9.873595563261626)
    point7 = coord(57.059836008759575, 9.871725850695908)
    
    pointList = [point1, point2, point3, point4, point5, point6, point7]
    
    return len(pointList)

def talkerGps(f1, f2, pointNum):
    serial_data = serial_reader()
    
    ref = pointList[pointNum]
    
    if serial_data[0:6].decode('UTF-8') == "$GPGGA":
        #msg1 = gpgga(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        f1.write(str(serial_data).strip("b'")+"\n")
        dist, bear = obtainValues(str(serial_data).strip("b'"), ref)
            
    if serial_data[0:6].decode('UTF-8') == "$GPVTG":
        #msg2 = gpvtg(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        f2.write(str(serial_data).strip("b'")+"\n")
        vel = obtainVel(str(serial_data).strip("b'"))
        
    return dist, bear, vel

#dist = 10
#bear = 10
#vel = 10 

def oldtalkerGps(file1, pointNum, count, serial_data):
    
    global dist, bear, vel
    print(serial_data[count])
    print(pointNum)
    ref = pointList[pointNum]
    
    if serial_data[count][0:6] == "$GPGGA":
        #msg1 = gpgga(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        
        #f1.write(str(serial_data).strip("b'")+"\n")
        dist, bear = obtainValues(serial_data[count], ref)
    else:
        dist = 999
        bear = 999
        
    if serial_data[count][0:6] == "$GPVTG":
        #msg2 = gpvtg(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        
        #f2.write(str(serial_data).strip("b'")+"\n")
        vel = obtainVel(serial_data[count])
    else:
        vel = 999

    return dist, bear, vel