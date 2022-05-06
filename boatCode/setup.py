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
    
    point1 = coord(57.056534073904686, 9.869477638599093)
    point2 = coord(57.05877432742965, 9.872404241980814)
    point3 = coord(57.059179209484505, 9.871792035211508)
    point4 = coord(57.058504403606584, 9.869988507161391)
    point5 = coord(57.057784597150466, 9.871295651344504)
    point6 = coord(57.05871134537982, 9.873595563261626)
    point7 = coord(57.059836008759575, 9.871725850695908)
    
    pointList = [point1, point2, point3, point4, point5, point6, point7]
    
    return pointList