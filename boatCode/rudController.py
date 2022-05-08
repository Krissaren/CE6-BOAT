Kp_i = 18000
Kd = 10000

delay = 0.05

inBearList = []
bearList = []
refbearList = []

upperRudLim = 60000
lowerRudLim = -60000

def bearController(bear, refbear):        
    inBearList.append(bear)
    refbearList.append(refbear)
    
    if len(bearList) < 3:
        nextBear = 0
        
    else:
        inBearLen = len(inBearList) - 1
        refbearLen = len(refbearList) - 1
        
        error = refbearList[refbearLen] - inBearList[inBearLen]
        preerror = refbearList[refbearLen - 1] - inBearList[inBearLen - 1]
        pre2error = refbearList[refbearLen - 2] - inBearList[inBearLen - 2]
        
        nextBear = Kd / delay * (error - 2 * preerror + pre2error) + Kp_i * (error - preerror) + bearList[-1]
    
    if(nextBear > upperRudLim):
        nextBear = upperRudLim
        
    if(nextBear < lowerRudLim):
        nextBear = lowerRudLim
        
    bearList.append(nextBear)
    
    return nextBear