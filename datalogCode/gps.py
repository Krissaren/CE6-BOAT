import serial
import os.path

i = 1
gpsPort = serial.Serial("/dev/GPS", baudrate=115200, timeout=3.0)

def logdataGps(i):
    f1 = os.path.join("data/dataFolder"+str(i), "gpggaGpsData.txt")
    f2 = os.path.join("data/dataFolder"+str(i), "gpvtgGpsData.txt")
    return f1, f2

def serial_reader():
    return gpsPort.readline()

def talkerGps(f1, f2):
    serial_data = serial_reader()
    
    if serial_data[0:6].decode('UTF-8') == "$GPGGA":
        f1.write(str(serial_data).strip("b'")+"\n")
            
    if serial_data[0:6].decode('UTF-8') == "$GPVTG":
        f2.write(str(serial_data).strip("b'")+"\n")