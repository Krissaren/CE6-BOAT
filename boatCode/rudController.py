Kp_i = 18000
Kd = 10000

bearList = []

def bearController(bear):        
    if len(bearList) < 3:
        nextBear = 0
        
    else:
        print("bearprint")
        bearLen = len(bearList) - 1
        error = bearList - 
        delay = 0.05
        #nextBear = Kd / delay * (bearList[bearLen] - 2 * bearList[bearLen - 1] + bearList[bearLen - 2]) + Kp_i * (bearList[bearLen] - bearList[bearLen - 1]) + bear
        nextBear = Kp_i * (bearList[bearLen] - bearList[bearLen - 1]) + bear
    
    if(nextBear > 60000):
        nextBear = 60000
    if(nextBear < -60000):
        nextBear = -60000
    bearList.append(nextBear)
    return nextBear