import time as t

from setup import *
from mainLog import *
from readOldData import *

from throtController import *
from rudController import *

from testgpsOurVersion import testtalkerGps

if __name__ == '__main__':
    refPointThrot, refPointRud = 0 #postion in the array of reference points
    #totvel = 0 #imu velocity
    finalThrot = 0
    finalRud = 0
    
    #Constants for the turning corner references distances
    refdistThrot = 5
    refdistRud = 5
    
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
                distThrot, distRud, bear, refbearThrot, refbearRud, gpsvel = talkerGps(fGps1, fGps2, pointList, refPointThrot, refPointRud)
                if(distThrot != None):
                    distRef = distController(distThrot)
                
                if(gpsvel == None):
                    gpsvel = 0
                
                velRef = velController(gpsvel)
                print("Encoder value throttle: ", velRef)
                setThrotPos(velRef)
                
                bearRef, error = bearController(bear, refbearRud)
                print("Encoder value rudder: ", bearRef)
                setRudPos(bearRef)
                
                print("Distance for throt: ",distThrot," Distance for rud: ",distRud," Bearing from GPS: ",bear, " Ref bear for throt", refbearThrot," Ref bear for rud", refbearRud," Bearing error for rud: ", error, " Velocity from GPS: ",gpsvel," Point for Throt: ",refPointThrot," Point for Rud: ",refPointRud, " Encoder value throttle: ", velRef, " Encoder value rudder: ", bearRef)
                
                fextra.write("Distance for throt: " + str(distThrot) + " Distance for rud: " + str(distRud) + " Bearing from GPS: " + str(bear) + " Ref bear for throt" + str(refbearThrot) + " Ref bear for rud" + str(refbearRud) + " Bearing error for rud: " + str(error) + " Velocity from GPS: " + str(gpsvel) + " Point for Throt: " + str(refPointThrot) + " Point for Rud: " + str(refPointRud) + " Encoder value throttle: " + str(velRef) + " Encoder value rudder: " + str(bearRef) + "\n")
            
                if(distThrot != None):
                    if distThrot < refdistThrot and refPointThrot <  len(pointList) and finalThrot == 0:    #Check in which point we want to go
                        if refPointThrot == (len(pointList) - 1):
                            finalThrot += 1
                        else:
                            refPointThrot += 1
                      
                if(distRud != None):  
                    if distRud < refdistRud and refPointRud <  len(pointList) and finalRud == 0:    #Check in which point we want to go
                        if refPointRud == (len(pointList) - 1):
                            finalRud += 1
                        else:
                            refPointRud += 1
            
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