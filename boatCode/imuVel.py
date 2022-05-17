import numpy as np
import serial
from statistics import mean

from imuOurVersion import serial_reader2

totVel = 0

imuPort = serial.Serial("/dev/IMU", baudrate=921600, timeout=3.0)
alist = []
try:
	while(1):
		if(imuPort.in_waiting > 39):
			serial_data1, serial_data2, serial_data3 = serial_reader2()
			   
			vel = (serial_data2[0] + serial_data2[1] + serial_data2[2] - 0.9887146370199428) * 9.80665 * 0.008
			#a = (serial_data2[0] + serial_data2[1] + serial_data2[2])

			totVel += vel
			
			#alist.append(a)
			print("Velocity of the IMU: ", totVel)
except KeyboardInterrupt:
	print("done")
	#print(mean(alist))
