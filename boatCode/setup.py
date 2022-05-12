import numpy as np
from rudOurVersion import *

#Setup code for the rudder and the throt
def setupRud():
    setRudPos(123415) #from the left
    #setRudPos(88585) #from the right
 
class coord:
    lat = np.float64    
    lon = np.float64

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

def createPointList():
    #Code for the path planning and returns a list with all the points (lon,lat)
    global pointList

    point1 = coord(57.01405450775168, 9.987992118860989)
    point2 = coord(57.014048169900235, 9.98860546200752)
    point3 = coord(57.01381476124234, 9.98861066434579)
    point4 = coord(57.013816424744924, 9.987992305095972)
    
    
    
    pointList = [point1, point2, point3]
    """
    point1 = coord(57.04820107772273, 9.84233233749568)
    point2 = coord(57.0482001539734, 9.842662769261473)
    point3 = coord(57.048379651092354, 9.842663907366893)
    point4 = coord(57.04838102754971, 9.842001532430896)
    point5 = coord(57.04802100188279, 9.841998936629103)
    point6 = coord(57.04801877387538, 9.842991744476215)
    point7 = coord(57.04855868820584, 9.843003816712589)
    point8 = coord(57.048572655319006, 9.84168160759072)
    point9 = coord(57.047853135424475, 9.841652225867474)
    point10 = coord(57.04782990557305, 9.843305091622234)
    
    pointList = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10]
    """
    return pointList