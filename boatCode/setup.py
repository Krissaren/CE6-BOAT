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
    """
    point1 = coord(57.013096790083274, 9.983821443939894)
    point2 = coord(57.013099797274656, 9.983500304319863)
    point3 = coord(57.013252945729576, 9.983524175163934)
    
    
    
    pointList = [point1, point2, point3]
    """
    #far away
    """
    point1 = coord(57.04759547281304, 9.8478156482165)
    point2 = coord(57.04741577335514, 9.847811849885467)
    point3 = coord(57.04741164245177, 9.847470094621764)
    point4 = coord(57.04777517245576, 9.847473890700519)
    point5 = coord(57.0477731058511, 9.84814601610035)
    point6 = coord(57.04724226922041, 9.848157400060707)
    point7 = coord(57.047234007708084, 9.847154922342881)
    point8 = coord(57.04795280587709, 9.847154913714288)
    point9 = coord(57.047959000264726, 9.848483982498717)
    point10 = coord(57.04706050191412, 9.848483961156115)
    """
    #close to harbour
   
    point1 = coord(57.05637859345908, 9.871064075484004)
    point2 = coord(57.05717809801823, 9.872010016373073)
    point3 = coord(57.05779165960832, 9.871440172463997)
    point4 = coord(57.05776067189234, 9.869548290685858)
    point5 = coord(57.05696117987846, 9.868135077791345)
    point6 = coord(57.056242242125876, 9.868089490278619)
    point7 = coord(57.055988131486956, 9.8692747656095)
    point8 = coord(57.05639098900998, 9.871052678605823)
    point9 = coord(57.05653973529816, 9.872010016373073)
    
    pointList = [point1, point2, point3, point4, point5, point6, point7, point8, point9]
    
    
    return pointList