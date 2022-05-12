import time as t

from setup import *
from mainLog import *
from readOldData import *

from throtController import *
from rudController import *

if __name__ == '__main__':
    refPoint = 0 #postion in the array of reference points
    #totvel = 0 #imu velocity
    final = 0
    
    pointList = createPointList()
    
    """
    #Code for setup in the center the rudder
    setupRud()
    
    t.sleep(15) #delay to set the Rudder in the center (15 from the left and 11.4 from the right)
    """
    
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
                    vel = 0
                
                velRef = velController(gpsvel)
                print("Encoder value throttle: ", velRef)
                setThrotPos(velRef)
                
                bearRef, error = bearController(bear, refbear)
                print("Encoder value rudder: ", bearRef)
                setRudPos(bearRef)
                
                print("Distance: ",dist," Bearing: ",bear," Velocity: ",vel," Point: ",refPoint, " Encoder value throttle: ", velRef, " Encoder value rudder: ", bearRef, " Bearing error: ", error)
                
                fextra.write("Distance: ",dist," Bearing: ",bear," Velocity: ",vel," Point: ",refPoint, " Encoder value throttle: ", velRef, " Encoder value rudder: ", bearRef, " Bearing error: ", error +"\n")
            
                if(dist != None):
                    if dist < 5 and refPoint <  len(pointList) and final == 0:    #Check in which point we want to go
                        if refPoint == (len(pointList) - 1):
                            final += 1
                        else:
                            refPoint += 1
            
            """
            #Code for reading old data
            dist, bear, vel = oldtalkerGps(file, pointList, count)
            count += 2
            """
               
            if(imuPort.in_waiting > 39):
                imuVel = talkerImu(fImu1, fImu2, fImu3)
                totvel += imuVel
                #print("Velocity of the IMU: ", totvel)
            
            """
            #Code for logging rudder and throttle
            if(rudPort.in_waiting > 5):
                talkerRud(fRud1)
            
            if(throtPort.in_waiting > 5):
                talkerThrot(fThrot1)
          
            #Code while developing, remove at the end
            currentTime = t.time()
            print("time", currentTime)
            if(currentTime - start > 0.05):
                if(dist != None):
                    distRef = distController(dist)
                velRef = velController(vel)
                print("Distance:",dist,", Bearing:",bear,", Velocity:",vel,", Point:",refPoint)
                print("Encoder value throttle: ", velRef)
                #print("hallo000000000000000000000", currentTime-start)
                start = currentTime
                setThrotPos(velRef)
                #print("buffffffffffffer", throtPort.out_waiting)
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

    
