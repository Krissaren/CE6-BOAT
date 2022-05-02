#!/usr/bin/env python
import time as t
import serial
import numpy as np
import os.path
from datetime import datetime

rudPort = serial.Serial("/dev/Rudder", baudrate=115200, timeout=0)

class motordata:
	time = np.uint64
	encoder = np.int32
	set_point = np.int32
	
def logdataRud(i):
	return os.path.join("data/dataFolder"+str(i), "rudData.txt")
	
def serial_reader():
	a = rudPort.readline()
	print(a)
	return a

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

def talkerRud(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))
	
	#print("#"+str(set_point))
	#port.write(bytes(set_point))


def setRudPos(enc):
	print(rudPort.write(bytes(enc, 'utf-8')))