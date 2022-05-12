Kp = 7200
Kd = 0
delay = 0.05

inBearList = []
bearList = []
refbearList = []

upperRudLim = 60000
lowerRudLim = -60000


def bearController(bear, refbear): 
    error=0
    inBearList.append(bear)
    refbearList.append(refbear)

    if len(bearList) < 3:
        nextBear = 0
        
    else:
        inBearLen = len(inBearList) - 1
        refbearLen = len(refbearList) - 1
        #print("refbear:", refbearList[-1])
        
        error = refbearList[refbearLen] - inBearList[inBearLen]
        preerror = refbearList[refbearLen - 1] - inBearList[inBearLen - 1]
        
        if error > 180:
            error = -360 + error
            
        elif error < -180:
            error = 360 + error
            
        if preerror > 180:
            preerror = -360 + preerror
            
        elif preerror < -180:
            preerror = 360 + preerror
            
        #print("bear error:", error)
        
        nextBear = Kp * error + (Kd / delay) * (error - preerror) 
        #nextBear = Kp_i * (error)
    
    if(nextBear > upperRudLim):
        nextBear = upperRudLim
        
    if(nextBear < lowerRudLim):
        nextBear = lowerRudLim
        
    bearList.append(nextBear)

    return nextBear, error