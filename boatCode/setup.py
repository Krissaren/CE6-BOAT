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
    
    point1 = coord(57.01540473658004, 9.985802806479333)
    point2 = coord(57.01540803844199, 9.986588222563874)
    point3 = coord(57.01539648192391, 9.987255371361554)
    
    pointList = [point1, point2, point3]
    
    return pointList