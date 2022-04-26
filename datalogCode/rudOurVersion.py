#!/usr/bin/env python
import time
import serial
import numpy as np
import os.path
from datetime import datetime

rudPort = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

class motordata:
	time = np.uint64
	encoder = np.int32
	set_point = np.int32
	
def logdataRud(i):
	return os.path.join("data/dataFolder"+str(i), "rudData.txt")
	
def serial_reader():
	return rudPort.readline()

def format(data):
	#print(data)
	msg = motordata()
	msg.time = int(round(time.time() * 1000))

	try:
	    msg.encoder = int(data)
	except:
	    msg.encoder = set_point

	msg.set_point = set_point
	return msg

def talkerRud(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))
	
	#print("#"+str(set_point))
	#port.write(bytes(set_point))
