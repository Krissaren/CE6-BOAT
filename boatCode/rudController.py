#Constants declaration
Kp = 5200
Ki = 200
Kd = 5000

inBearList = []
bearList = []
refbearList = []

delay = 0.05

upperRudLim = 60000
lowerRudLim = -60000


def bearController(bear, refbear):   
    inBearList.append(bear)
    refbearList.append(refbear)

    if len(bearList) < 5:
        nextBear = 0
        
    else:
        inBearLen = len(inBearList) - 1
        refbearLen = len(refbearList) - 1
        #print("refbear:", refbearList[-1])
        
        error = refbearList[refbearLen] - inBearList[inBearLen]
        preerror = refbearList[refbearLen - 1] - inBearList[inBearLen - 1]
        pre2error = refbearList[refbearLen - 2] - inBearList[inBearLen - 2]

        if error > 180:
            error = -360 + error
            
        elif error < -180:
            error = 360 + error
            
        if preerror > 180:
            preerror = -360 + preerror
            
        elif preerror < -180:
            preerror = 360 + preerror
            
        if pre2error > 180:
            pre2error = -360 + pre2error
            
        elif preerror < -180:
            pre2error = 360 + pre2error
            
        #print("bear error:", error)
        
        nextBear = Kp * (error - preerror) +  Ki * delay * error + (Kd / delay) * (error - 2 * preerror + pre2error) + inBearList[-1]
        #nextBear = Kp * (error)
    
    if(nextBear > upperRudLim):
        nextBear = upperRudLim
        
    if(nextBear < lowerRudLim):
        nextBear = lowerRudLim
        
    bearList.append(nextBear)

    return nextBear, error