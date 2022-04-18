import string
import time
import numpy as np
import serial
import os.path
from imuOurVersion import *
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
    makeFolder()
    f1, f2 = logdataGps(i)
    f3, f4, f5 = logdataImu(i)
    while(1):
        talkerGps(f1, f2)
        talkerImu(f3, f4, f5)