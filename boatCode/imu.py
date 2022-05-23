import numpy as np
import serial
import os.path
from datetime import datetime

imuPort = serial.Serial("/dev/IMU", baudrate=921600, timeout=3.0)

def logdataImu(num):
    f1 = os.path.join("data/dataFolder"+str(num), "gyroImuData.txt")
    f2 = os.path.join("data/dataFolder"+str(num), "accImuData.txt")
    f3 = os.path.join("data/dataFolder"+str(num), "incImuData.txt")
    return f1, f2, f3

def serial_reader2():
    raw1 = None
    raw2 = None
    raw3 = None
    
    while raw3 != b'\x0d' or raw2 != b'\x0a' or raw1 != b'\x93':  # 0d and 0a is end of a line and 90 is msg id
        raw3 = raw2
        raw2 = raw1
        raw1 = imuPort.read(1)

    raw = imuPort.read(30)

    data1 = (np.frombuffer(raw[0:3] + b'\x00' + raw[3:6] + b'\x00' + raw[6:9] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (29)))

    data2 = (np.frombuffer(raw[10:13] + b'\x00' + raw[13:16] + b'\x00' + raw[16:19] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (27)))

    data3 = (np.frombuffer(raw[20:23] + b'\x00' + raw[23:26] + b'\x00' + raw[26:29] + b'\x00', dtype='>i')
             .astype(np.float32) / (2 ** (30)))
      
    return data1, data2, data3


def talkerImu(f1, f2, f3):
    serial_data1, serial_data2, serial_data3 = serial_reader2()
    
    now = datetime.now()
    
    f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data1).strip("[]")+"\n")
    f2.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data2).strip("[]")+"\n")
    f3.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + str(serial_data3).strip("[]")+"\n")
    
    #vel = (serial_data2[0] + serial_data2[1] + serial_data2[2] - X) * 9.80665 * 0.008
    #return vel
