import time as t
import os.path

from rud import *
from throt import *

t.sleep(3) # Timeout for the right setup of the Arduino's

from imu import *
from gps import * 

i = 1 # Definition global variables

def makeFolder():
    global i
    f=None
    
    while f is None:
        try:
            os.mkdir("data/dataFolder" + str(i) )
            f=1 
        except:
            i += 1

def mainLog():
    makeFolder()
    
    fGps1, fGps2 = logdataGps(i)
    fImu1, fImu2, fImu3 = logdataImu(i)
    fRud1 = logdataRud(i)
    fThrot1 = logdataThrot(i)
    fextra = os.path.join("data/dataFolder"+str(i), "extraData.txt")

    fGps1 = open(fGps1, "a")
    fGps2 = open(fGps2, "a")
    fImu1 = open(fImu1, "a")
    fImu2 = open(fImu2, "a")
    fImu3 = open(fImu3, "a")
    fRud1 = open(fRud1, "a")
    fThrot1 = open(fThrot1, "a")
    fextra = open(fextra, "a")
    
    return fGps1, fGps2, fImu1, fImu2, fImu3, fRud1, fThrot1, fextra