import time as t
import os.path
from datetime import datetime
#from rudOurVersion import *
#from throtOurVersion import *
#t.sleep(3)
#from imuOurVersion import *
from gpsOurVersion import * 

i = 1

def makeFolder():
    global i
    f=None
    
    while f is None:
        try:
            os.mkdir("data/dataFolder" + str(i) )
            f=1 
        except:
            i += 1

if __name__ == '__main__':
    point = 1 #postion in the array of points wanted
    count = 1 #line we are reading in the file
    """
    makeFolder()
    
    fGps1, fGps2 = logdataGps(i)
    fImu1, fImu2, fImu3 = logdataImu(i)
    fRud1 = logdataRud(i)
    fThrot1 = logdataThrot(i)

    fGps1 = open(fGps1, "a")
    fGps2 = open(fGps2, "a")
    fImu1 = open(fImu1, "a")
    fImu2 = open(fImu2, "a")
    fImu3 = open(fImu3, "a")
    fRud1 = open(fRud1, "a")
    fThrot1 = open(fThrot1, "a")
    setRudPos("40000")
    #setThrotPos("10000")
    t.sleep(2)
    setRudPos("0")
    #setThrotPos("0")
    """
    #fold = os.path.join("readinclass", "throt11150rud132652.txt")
    #print(fold)
    file1 = open("throt11150rud132652.txt", "r")
    line = file1.readline()
    cnt = 1
    serial_data=[]
    while line:
        serial_data.append(line.strip())
        print("Line {}: {}".format(cnt, line.strip()))
        line = file1.readline()
        cnt += 1
        
    numPoints = createPointList()
    print(numPoints)
    
    try:
        while(1):
            now = datetime.now()
            
            
            #dist, bear, vel = talkerGps(fGps1, fGps2, point)
            dist, bear, vel = oldtalkerGps(file1, point, count, serial_data)
            print("Distance:",dist,", Bearing:",bear,", Velocity:",vel)
            
            if dist < 5:    #Check in which point we want to go
                point += 1 
            count += 1
            """
            talkerImu(fImu1, fImu2, fImu3)
            
            talkerRud(fRud1)
            
            talkerThrot(fThrot1)
            """
            
            
            #print(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond))

    except KeyboardInterrupt: 
        """
        fGps1.close()
        fGps2.close()
        fImu1.close()
        fImu2.close()
        fImu3.close()
        fRud1.close()
        fThrot1.close()
        """
        #print("Files closed correctly")

    
