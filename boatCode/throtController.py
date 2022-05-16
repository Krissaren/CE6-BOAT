#Constants declaration
Kp_o = 0.059

Kp_i = 1746.5
Ki = 437.8
Kd = 1216.2

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
          
    if len(distList) < 5:
        nextVel = 0
        
    else:
        distLen = len(distList) - 1
        velLen = len(velList) - 1
        
        error = distList[distLen] - inVelList[velLen]
        preerror = (distList[distLen - 1] - inVelList[velLen - 1])
        pre2error = (distList[distLen - 2] - inVelList[velLen - 2])
        
        nextVel = Kp_i * (error - preerror) +  Ki * delay * error + (Kd / delay) * (error - 2 * preerror + pre2error) + velList[-1]

    if nextVel > upperThrotLim:
        nextVel = upperThrotLim
        
    elif nextVel < lowerThrotLim:
        nextVel = lowerThrotLim
    
    velList.append(nextVel)
    
    return nextVel + 10000 #addind the offset