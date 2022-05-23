import numpy as np

class coord:
    lat = np.float64    
    lon = np.float64

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

def createPointList(): # Code for the path planning and returns a list with all the points (lon,lat)
    global pointList

    # From 1 to 10 for inside-out pattern, from 10 to 1 fro outside-in pattern
    point1 = coord(57.05674761452483, 9.869521301832231)
    point2 = coord(57.05656095876593, 9.869522767231796)
    point3 = coord(57.05656189018057, 9.869174395743482)
    point4 = coord(57.056923103724536, 9.86918784303395)
    point5 = coord(57.05691977619669, 9.86985469104046)
    point6 = coord(57.05638009013941, 9.869852008475654)
    point7 = coord(57.05638201454456, 9.868854384768735)
    point8 = coord(57.057102979388915, 9.868870516287982)
    point9 = coord(57.05710443697757, 9.870190921928982)
    point10 = coord(57.05619920893293, 9.870182826282743)

    pointList = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10]
    return pointList