#Constants declaration
Kp = 5400
Ki = 400
Kd =5000

inBearList = []
bearList = []
refbearList = []
newPoint = 0

delay = 0.05

upperRudLim = 80000
lowerRudLim = -80000


def bearController(bear, refbear):  
    global newPoint 
    inBearList.append(bear)
    refbearList.append(refbear)
    meanError = 0
    error = 0
    if len(bearList) < 10:
        nextBear = 0
        
    else:
        inBearLen = len(inBearList) - 1
        refbearLen = len(refbearList) - 1
        #print("refbear:", refbearList[-1])
        if(newPoint == 2):
            refbearList[1] = refbearList[0]
            refbearList[2] = refbearList[0]
            refbearList[3] = refbearList[0]
            refbearList[4] = refbearList[0]
            refbearList[5] = refbearList[0]
            refbearList[6] = refbearList[0]
            refbearList[7] = refbearList[0]
            refbearList[8] = refbearList[0]
            refbearList[9] = refbearList[0]
            newPoint = 0
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
        
        """#
        meanError = (error + preerror + pre2error + pre3error + pre4error + pre5error + pre6error +pre7error)/8
        meanPreerror = (preerror + pre2error + pre3error +pre4error +pre5error + pre6error + pre7error + pre8error)/8
        meanPre2error = (pre2error + pre3error + pre4error +pre5error + pre6error + pre7error + pre8error + pre9error)/8
        """
        meanError = (error + preerror + pre2error + pre3error )/4
        meanPreerror = (preerror + pre2error + pre3error +pre4error )/4
        meanPre2error = (pre2error + pre3error + pre4error +pre5error )/4
        

        if meanError > 180:
            meanError = -360 + meanError
            
        elif meanError < -180:
            meanError = 360 + meanError
            
        if meanPreerror > 180:
            meanPreerror = -360 + meanPreerror
            
        elif meanPreerror < -180:
            meanPreerror = 360 + meanPreerror
            
        if meanPre2error > 180:
            meanPre2error = -360 + meanPre2error
            
        elif meanPreerror < -180:
            meanPre2error = 360 + meanPre2error

        if error > 180:
            error = -360 + error
            
        elif error < -180:
            error = 360 + error
            
        print("kp err:", meanError-meanPreerror, " ki err:", meanError, "kd err:", meanError - 2*meanPreerror +meanPre2error)
        
        nextBear = Kp * (meanError - meanPreerror) +  Ki * delay * meanError + (Kd / delay) * (meanError - 2 * meanPreerror + meanPre2error) + bearList[-1]
        #nextBear = Kp * (error)
    
    if(nextBear > upperRudLim):
        nextBear = upperRudLim
        
    if(nextBear < lowerRudLim):
        nextBear = lowerRudLim
        
    bearList.append(nextBear)

    return nextBear, meanError