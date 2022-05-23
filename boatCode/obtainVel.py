import time as t
import numpy as np

class msg_gpvtg:
    time = np.uint64 
    utc_seconds = np.float64 # UTC seconds from midnight
    vel = np.float32
    
    def __init__(self,time,utc_seconds,vel):
        self.time = time
        self.utc_seconds = utc_seconds
        self.vel = vel
        
def gpvtg(data):
    string = str(data)
    time = int(round(t.time() * 1000))
    
    index1 = 0
    index2 = string.find("N")
    index1 = index2
    index2 = string.find(",", index2 + 1)
    index1 = index2
    index2 = string.find(",", index2 + 1)
    
    if string[index1 + 1:index2] == "":
        vel = float(0)
    else:
        vel = float(string[index1 + 1:index2])
    utc_seconds = float(0)

    return msg_gpvtg(time,utc_seconds,vel)

def obtainVel(data):
    msgVel = gpvtg(data)
    #print('Velocity in meters/seconds: ', msgVel.vel)
    
    return msgVel.vel