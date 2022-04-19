#!/usr/bin/env python
import time
import serial
import numpy as np
from datetime import datetime

rudPort = serial.Serial("/dev/throt", baudrate=115200, timeout=3.0)

class motordata:
	time = np.uint64
	encoder = np.int32
	set_point = np.int32
	
def logdataThrot(i):
	return os.path.join("data/dataFolder"+str(i), "throtData.txt")
	
def serial_reader():
        return port.readline()

def format(data):
        print(data)
        msg = motordata()
        msg.time = int(round(time.time() * 1000))
        try:
            msg.encoder = int(data)
        except:
            msg.encoder = set_point
        msg.set_point = set_point
        return msg

def talkerThrot(f1):
	serial_data = serial_reader()
	f = open(f1, "a")
	f.write(tr(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data+"\n")
	f.close()
    	
	#print("#"+str(set_point))
	#port.write(bytes(set_point))


