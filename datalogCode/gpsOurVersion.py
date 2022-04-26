#!/usr/bin/env python
import string
import time
import numpy as np
import serial
import os.path

i = 1
gpsPort = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

class msg_gpgga:
    time = np.uint64 
    message_id = string
    utc_seconds = np.float64 # UTC seconds from midnight
    lat = np.float64
    lon = np.float64
    lat_dir = string
    lon_dir = string
    gps_qual = np.uint32
    num_sats = np.uint32
    hdop = np.float32
    alt = np.float32
    altitude_units = string
    undulation = np.float32
    undulation_units = string
    diff_age = np.float32
    station_id = string

class msg_gpvtg:
    time = np.uint64 
    utc_seconds = np.float64 # UTC seconds from midnight
    vel = np.float32

def logdataGps(i):
    f1 = os.path.join("data/dataFolder"+str(i), "gpggaGpsData.txt")
    f2 = os.path.join("data/dataFolder"+str(i), "gpvtgGpsData.txt")
    
    return f1, f2

def serial_reader():
    return gpsPort.readline()

def gpgga(data):
    string = data.decode('UTF-8')
    msg = msg_gpgga

    index1 = 0
    index2 = string.find(",")
    msg.time = int(round(time.time() * 1000))
    msg.message_id = string[index1:index2]

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.utc_seconds = float(0)
    else:
        msg.utc_seconds = float(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.lat = str(0)
    else:
        msg.lat = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.lat_dir = str(0)
    else:
        msg.lat_dir = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.lon = str(0)
    else:
        msg.lon = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.lon_dir = str(0)
    else:
        msg.lon_dir = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.gps_qual = int(0)
    else:
        msg.gps_qual = int(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.num_sats = int(0)
    else:
        msg.num_sats = int(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.hdop = float(0)
    else:
        msg.hdop = float(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.alt = float(0)
    else:
        msg.alt = float(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.altitude_units = str(0)
    else:
        msg.altitude_units = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.undulation = float(0)
    else:
        msg.undulation = float(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.undulation_units = str(0)
    else:
        msg.undulation_units = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        msg.diff_age = float(0)
    else:
        msg.diff_age =float(string[index1+1:index2])

    index1 = index2
    index2 = string.find("*", index2+1)
    if string[index1+1:index2] == "":
        msg.station_id = str(0)
    else:
        msg.station_id = str(string[index1+1:index2])
    return msg


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


def next(string, number):
    index1 = 0
    index2 = 0

    for i in range(number):
        index1 = index2
        index2 = string.find(",",index2)

    return string[index1:index2]


def talkerGps(f1, f2):
    serial_data = serial_reader()
    
    if serial_data[0:6].decode('UTF-8') == "$GPGGA":
        #msg1 = gpgga(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        f1.write(str(serial_data).strip("b'")+"\n")
            
    if serial_data[0:6].decode('UTF-8') == "$GPVTG":
        #msg2 = gpvtg(serial_data)
        #f.write(serial_data.decode('UTF-8', 'ignore').strip('\r\n')+"\n")
        f2.write(str(serial_data).strip("b'")+"\n")