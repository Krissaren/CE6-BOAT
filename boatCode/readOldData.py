from longLatToDistAndHead import *
from obtainVel import *

old_serial_data = []

def readOldData():    
    file1 = open("throt15065E.txt", "r") #Name of the file in "name.txt" format
    line = file1.readline()
    cnt = 1

    while line:
        old_serial_data.append(line.strip())
        line = file1.readline()
        cnt += 1

    return file1, old_serial_data
        
def oldtalkerGps(file1, pointList, count):
    
    global dist, bear, vel

    ref = pointList[len(pointList) - 1]
    
    if old_serial_data[count][0:6] == "$GPGGA":
        dist, bear = obtainValues(old_serial_data[count], ref)
        
    if old_serial_data[count + 1][0:6] == "$GPVTG":
        vel = obtainVel(old_serial_data[count + 1])/3.6

    return dist, bear, vel