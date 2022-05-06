
#Constants declaration
Kp_o = 0.1041

Kp_i = 595.66
Ki = 659.9

inVelList = []
distList = []
velList = []

delay = 0.05

opVelLim = 2.46
upperThrotLim = 5227
lowerThrotLim = 0

def distController(dist): 
    nextDist = Kp_o * dist
    
    if nextDist > opVelLim:
        nextDist = opVelLim
    
    distList.append(nextDist)
    
    return nextDist
    
def velController(vel):
                        #Like this if velController its called after distController, 
                        #if not add dist as a input variable of the function
    inVelList.append(vel)
    
    if distList == False:
        nextVel = 0
        
    elif len(distList) == 1:
        print(distList)
        nextVel = 0
        
    else:
        distLen = len(distList) - 1
        velLen = len(velList) - 1
        
        error = distList[distLen] - inVelList[velLen]
        preerror = (distList[distLen - 1] - inVelList[velLen - 1])
        
        nextVel = Kp_i * (error - preerror) + delay * Ki * error + velList[velLen]
        
    
    if nextVel > upperThrotLim:
        nextVel = upperThrotLim
    elif nextVel < lowerThrotLim:
        nextVel = lowerThrotLim
    
    velList.append(nextVel)
    
    return nextVel + 10000 #addind the offset