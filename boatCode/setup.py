import numpy as np

#Setup code for the rudder and the throt

 
class coord:
    lat = np.float64    
    lon = np.float64

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

def createPointList():
    #Code for the path planning and returns a list with all the points (lon,lat)
    global pointList
    point3 = coord(57.01496190200841, 9.985619452030704)
    point2 = coord(57.01519426174039, 9.985622228858869)
    point1= coord(57.015404106322286, 9.985628478480402)
    
    
    
    pointList = [point1, point2, point3]
    
    return pointList