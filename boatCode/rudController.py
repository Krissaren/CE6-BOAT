Kp_i = 0
Ki = 0

bearList = []

def bearController(bear, timeList):
    if bearList == False:
        nextBear = 0
        
    elif len(bearList) == 1:
        print(bearList)
        nextBear = Kp_i * bearList[0]+ bear
        
    else:
        timeLen = len(timeList) - 1
        bearLen = len(bearList) - 1
        delay = timeList[timeLen] - timeList[timeLen - 1]
        nextBear = Kp_i * (bearList[bearLen] - bearList[bearLen - 1]) + delay * Ki * bearList[bearLen] + bear
    
    return nextBear