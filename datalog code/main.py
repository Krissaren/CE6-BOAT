import string
import time
import numpy as np
import serial
import os.path
from imuOurVersion import *
#from gpsOurVersion import * 



if __name__ == '__main__':
    
    
    #try:
    while(1):
    	talkerImu()
    	talkerGps()
    #except:
     #   print("Something went wrong :(")
