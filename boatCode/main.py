import time as t

from setup import *
from mainLog import *
from readOldData import *

from throtController import *
from rudController import *

if __name__ == '__main__':
    refPoint = 0 # Variable for the postion in the array of reference points
    #totvel = 0 # Variable for the IMU velocity
    final = 0 # Variable to chechk if the search pattern is completly done
    
    pointList = createPointList()
       
    fGps1, fGps2, fImu1, fImu2, fImu3, fRud1, fThrot1, fextra = mainLog()
    
    """
    #Code for reading old data
    count = 0
    file, old_serial_data = readOldData()
    if old_serial_data[count][0:6] != "$GPGGA":
        count += 1
    """
    
    start = t.time()
    try:
        while(1):            
            
            if(gpsPort.in_waiting > 44):
                dist, bear, refbear, gpsvel = talkerGps(fGps1, fGps2, pointList, refPoint)
                if(dist != None):
                    distRef = distController(dist)
                
                if(gpsvel == None):
                    gpsvel = 0
                
                velRef = velController(gpsvel)
                setThrotPos(velRef)
                
                bearRef, error = bearController(bear, refbear)
                setRudPos(bearRef)
                
                print("Distance: ",dist," Bearing: ",bear, " Ref bear", refbear, " Velocity: ",gpsvel," Point: ",refPoint, " Encoder value throttle: ", velRef, " Encoder value rudder: ", bearRef, " Bearing error: ", error)
                
                fextra.write("Distance: " + str(dist) + " Bearing: " + str(bear) + " Ref bearing: " + str(refbear) + " Velocity: " + str(gpsvel) + " Point: " + str(refPoint) + " Encoder value throttle: " +  str(velRef) + " Encoder value rudder: " +  str(bearRef) + " Bearing error: " + str(error) + "\n")
            
                if(dist != None):
                    if dist < 5 and refPoint <  len(pointList) and final == 0:    #Check in which point we want to go
                        if refPoint == (len(pointList) - 1):
                            final += 1
                        else:
                            refPoint += 1
                            newPoint = 1
            
            """
            #Code for reading old data
            dist, bear, vel = oldtalkerGps(file, pointList, count)
            count += 2
            """
            
            if(imuPort.in_waiting > 39):
                talkerImu(fImu1, fImu2, fImu3)
                #totvel += imuVel
                #print("Velocity of the IMU: ", totvel)
            
            """
            #Code for logging rudder and throttle
            if(rudPort.in_waiting > 5):
                talkerRud(fRud1)
            
            if(throtPort.in_waiting > 5):
                talkerThrot(fThrot1)
            """
            
    except (KeyboardInterrupt, final == 1): # End the execution went Ctrl+C is pressed or when the search pattern is done

        fGps1.close()
        fGps2.close()
        fImu1.close()
        fImu2.close()
        fImu3.close()
        fRud1.close()
        fThrot1.close()