#!/usr/bin/env python
import time as t
import serial
import numpy as np
import os.path
from datetime import datetime

throtPort = serial.Serial("/dev/Throttle", baudrate=115200, timeout=3.0)

class motordata:
	time = np.uint64
	encoder = np.int32
	set_point = np.int32
	
def logdataThrot(i):
	return os.path.join("data/dataFolder"+str(i), "throtData.txt")
	
def serial_reader():
	return throtPort.readline()

def format(data):
	#print(data)
	msg = motordata()
	msg.time = int(round(t.time() * 1000))
	
	try:
		msg.encoder = int(data)
	except:
		msg.encoder = set_point
	
	msg.set_point = set_point
	return msg

def talkerThrot(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))
    	
	#print("#"+str(set_point))
	#port.write(bytes(set_point))


def setThrotPos(enc):
	throtPort.write(bytes(enc, 'utf-8'))