from setup import *
from mainLog import *
from readOldData import *

from throtController import *
from rudController import *

if __name__ == '__main__':
    refPoint = 1 #postion in the array of reference points
    
    pointList = createPointList()
    
    fGps1, fGps2, fImu1, fImu2, fImu3, fRud1, fThrot1 = mainLog()
    """
    count = 0
    file, old_serial_data = readOldData()
    if old_serial_data[count][0:6] != "$GPGGA":
        count += 1
    """
    try:
        while(1):            
            
            if(gpsPort.in_waiting > 44):
                dist, bear, vel = talkerGps(fGps1, fGps2, pointList, refPoint)
            """
            dist, bear, vel = oldtalkerGps(file, pointList, count)
            count += 2
            """
            print("Distance:",dist,", Bearing:",bear,", Velocity:",vel,", Point:",refPoint)
           
            if dist < 5 and refPoint <  len(pointList):    #Check in which point we want to go
                refPoint += 1 
            
            if(imuPort.in_waiting > 39):
                talkerImu(fImu1, fImu2, fImu3)
            
            talkerRud(fRud1)
            
            talkerThrot(fThrot1)
            
            distRef = distController(dist)
            #print(distRef)
            
            velRef = velController(vel)
            print("Encoder value throttle: ", velRef)
            #setThrotPos(velRef)
            """
            bearRef = bearController(bear)
            print("Encoder value rudder: ", bearRef)
            setRudPos(bearRef)
            """
    except KeyboardInterrupt: 

        fGps1.close()
        fGps2.close()
        fImu1.close()
        fImu2.close()
        fImu3.close()
        fRud1.close()
        fThrot1.close()

        #print("Files closed correctly")

    
