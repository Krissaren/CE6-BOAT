import serial
import os.path
from datetime import datetime

rudPort = serial.Serial("/dev/Rudder", baudrate=115200, timeout=0)
	
def logdataRud(i):
	return os.path.join("data/dataFolder"+str(i), "rudData.txt")
	
def serial_reader():
	return rudPort.readline()

def talkerRud(f1):
	serial_data = serial_reader()
	now = datetime.now()
	
	f1.write(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond) + " " + serial_data.decode('UTF-8'))
	
def setRudPos(enc):
	rudPort.write(bytes(enc, 'utf-8'))