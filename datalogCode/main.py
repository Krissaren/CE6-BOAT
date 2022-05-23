import time
import os.path
from datetime import datetime

from rud import *
from throt import *

time.sleep(3)

from imu import *
from gps import * 

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

    try:
        while(1):
            now = datetime.now()
            talkerGps(fGps1, fGps2)
            talkerImu(fImu1, fImu2, fImu3)
            #talkerRud(fRud1)
            #talkerThrot(fThrot1)
            #print(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond))

    except KeyboardInterrupt: 
        fGps1.close()
        fGps2.close()
        fImu1.close()
        fImu2.close()
        fImu3.close()
        fRud1.close()
        fThrot1.close()