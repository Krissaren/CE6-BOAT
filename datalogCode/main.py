import string
import time
import numpy as np
import serial
import os.path
from datetime import datetime
from imuOurVersion import *
#from gpsOurVersion import * 
#from rudOurVersion import *
#from throtOurVersion import *

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
    #fGps1, fGps2 = logdataGps(i)
    fImu1, fImu2, fImu3 = logdataImu(i)
    #fRud1 = logdataRud(i)
    #fThrot1 = logdataThrot(i)
    
    while(1):
        #talkerGps(fGps1, fGps2)
        talkerImu(fImu1, fImu2, fImu3)
        #talkerRud(fRud1)
        #talkerThrot(fThrot1)

        now = datetime.now()
        print(str(now.hour) + " " + str(now.minute) + " " + str(now.second) + " " + str(now.microsecond))
