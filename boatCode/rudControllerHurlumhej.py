#Constants declaration
Kp = 700
Ki = 200
Kd = 5000

inBearList = []
bearList = []
refbearList = []

delay = 0.05

upperRudLim = 80000
lowerRudLim = -80000


def bearController(bear, refbear):   
    inBearList.append(bear)
    refbearList.append(refbear)
    meanError = 0
    if len(bearList) < 10:
        nextBear = 0
        
    else:
        inBearLen = len(inBearList) - 1
        refbearLen = len(refbearList) - 1
        #print("refbear:", refbearList[-1])
        
        error = refbearList[refbearLen] - inBearList[inBearLen]
        preerror = refbearList[refbearLen - 1] - inBearList[inBearLen - 1]
        pre2error = refbearList[refbearLen - 2] - inBearList[inBearLen - 2]
        pre3error = refbearList[refbearLen - 3] - inBearList[inBearLen - 3]
        pre4error = refbearList[refbearLen - 4] - inBearList[inBearLen - 4]
        pre5error = refbearList[refbearLen - 5] - inBearList[inBearLen - 5]
        pre6error = refbearList[refbearLen - 6] - inBearList[inBearLen - 6]
        pre7error = refbearList[refbearLen - 7] - inBearList[inBearLen - 7]
        pre8error = refbearList[refbearLen - 8] - inBearList[inBearLen - 8]
        pre9error = refbearList[refbearLen - 9] - inBearList[inBearLen - 9]
        meanError[2] = meanError[1]
        meanError[1] = meanError[0]
        meanError[0] = (error + preerror + pre2error + pre3error + pre4error + pre5error + pre6error +pre7error)/8
        #meanPreerror = (preerror + pre2error + pre3error +pre4error +pre5error + pre6error + pre7error + pre8error)/8
        #meanPre2error = (pre2error + pre3error + pre4error +pre5error + pre6error + pre7error + pre8error + pre9error)/8

        if meanError[0] > 180: #make it between -180 and 180 degrees
            meanError[0] = -360 + meanError
            
        elif meanError[0] < -180:
            meanError[0] = 360 + meanError

        if meanError[0] < 0: #finds direction
            direction = 1
            meanError[0] = abs(-360 + meanError)

        elif meanError[0] >= 0:
            direction = (-1)
            meanError[0] = abs(360 + meanError)
            
        print("kp err:", meanError-meanPreerror, " ki err:", meanError, "kd err:", meanError -2*meanPreerror +meanPre2error)
        
        nextBear = direction*(Kp * (meanError - meanPreerror) +  Ki * delay * meanError + (Kd / delay) * (meanError - 2 * meanPreerror + meanPre2error)) + bearList[-1]
        #nextBear = Kp * (error)
    
    if(nextBear > upperRudLim):
        nextBear = upperRudLim
        
    if(nextBear < lowerRudLim):
        nextBear = lowerRudLim
        
    bearList.append(nextBear)

    #nextBear *= direction

    return nextBear, meanError