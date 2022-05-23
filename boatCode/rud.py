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
	return a

def talkerRud(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))
    
def setRudPos(enc):
	enc = str(int(enc))
	rudPort.write(bytes(enc + "A", 'utf-8'))