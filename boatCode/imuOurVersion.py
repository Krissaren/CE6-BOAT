#!/usr/bin/env python
import time as t
import numpy as np
import serial
import os.path
from datetime import datetime

imuPort = serial.Serial("/dev/IMU", baudrate=921600, timeout=3.0)

class msg:
    time = np.uint64 
    gyrox = np.float32
    gyroy = np.float32
    gyroz = np.float32
    accx = np.float32
    accy = np.float32
    accz = np.float32
    incx = np.float32
    incy = np.float32
    incz = np.float32

def logdataImu(num):
    f1 = os.path.join("data/dataFolder"+str(num), "gyroImuData.txt")
    f2 = os.path.join("data/dataFolder"+str(num), "accImuData.txt")
    f3 = os.path.join("data/dataFolder"+str(num), "incImuData.txt")
    return f1, f2, f3
	
def serial_reader():
    data = None
    raw = imuPort.readline()

    if len(raw) != 0:
        data = ":".join("{:02x}".format(c) for c in raw)
    
    return data


def format(data1, data2, data3):

    string = str(data1)
    length = len(string)
    string = string[1:length - 1]

    index1 = int(string.find(" ", 6))
    index2 = int(string.rfind(" ", index1 + 1, length - 10))

    msg.time = int(round(t.time() * 1000))
    msg.gyrox = float(string[0:index1])
    msg.gyroy = float(string[index1 + 1:index2])
    msg.gyroz = float(string[index2:length])

    string = str(data2)
    length = len(string)
    string = string[1:length - 1]
    index1 = int(string.find(" ", 6))
    index2 = int(string.rfind(" ", index1 + 1, length - 10))

    msg.accx = float(string[0:index1])
    msg.accy = float(string[index1 + 1:index2])
    msg.accz = float(string[index2:length])

    string = str(data3)
    length = len(string)
    string = string[1:length - 1]
    index1 = int(string.find(" ", 6))
    index2 = int(string.rfind(" ", index1 + 1, length - 10))

    msg.incx = float(string[0:index1])
    msg.incy = float(string[index1 + 1:index2])
    msg.incz = float(string[index2:length])
    return msg


def serial_reader2():
    raw1 = None
    raw2 = None
    raw3 = None
    
    while raw3 != b'\x0d' or raw2 != b'\x0a' or raw1 != b'\x93':  # 0d and 0a is end of a line and 90 is msg id
        raw3 = raw2
        raw2 = raw1
        raw1 = imuPort.read(1)

    raw = imuPort.read(30)
    
    #print(raw)

    data1 = (np.frombuffer(raw[0:3] + b'\x00' + raw[3:6] + b'\x00' + raw[6:9] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (21 + 8)))

    data2 = (np.frombuffer(raw[10:13] + b'\x00' + raw[13:16] + b'\x00' + raw[16:19] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (19 + 8)))

    data3 = (np.frombuffer(raw[20:23] + b'\x00' + raw[23:26] + b'\x00' + raw[26:29] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (22 + 8)))
    
    #print(data1)
    #print(data2)
    #print(data3)
    
    return data1, data2, data3


def talkerImu(f1, f2, f3):
    msgnew = msg
    msgold = msg
    
    serial_data1, serial_data2, serial_data3 = serial_reader2()
    
    msgold = msgnew #for later with the speed
    msgnew = format(serial_data1, serial_data2, serial_data3)
    
    now = datetime.now()
    
    f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data1).strip("[]")+"\n")
    f2.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data2).strip("[]")+"\n")
    f3.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data3).strip("[]")+"\n")
    
    vel = (serial_data2[0] + serial_data2[1] + serial_data2[2] - X) * 9.80665 * 0.008
    
    return vel