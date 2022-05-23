import serial
import os.path
from datetime import datetime

throtPort = serial.Serial("/dev/Throttle", baudrate=115200, timeout=3.0)
	
def logdataThrot(i):
	return os.path.join("data/dataFolder"+str(i), "throtData.txt")
	
def serial_reader():
	return throtPort.readline()

def talkerThrot(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))

def setThrotPos(enc):
	enc= str(int(enc))
	throtPort.write(bytes(enc + "A", 'utf-8'))
	print("buffer", throtPort.out_waiting)