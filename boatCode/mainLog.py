import time as t
import os.path

from rudOurVersion import *
from throtOurVersion import *

t.sleep(3)

from imuOurVersion import *
from gpsOurVersion import * 

#Definition global variables
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


def mainLog():
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
    
    return fGps1, fGps2, fImu1, fImu2, fImu3, fRud1, fThrot1