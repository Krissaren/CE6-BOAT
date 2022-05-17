import math
import string
import time as t
import numpy as np

class msg_gpgga:
    time = np.uint64 
    message_id = string
    utc_seconds = np.float64 # UTC seconds from midnight
    lat = np.float64
    lon = np.float64
    lat_dir = string
    lon_dir = string

    def __init__(self,time,message_id,utc_seconds,lat,lon,lat_dir,lon_dir):
        self.time = time
        self.message_id = message_id
        self.utc_seconds = utc_seconds
        self.lat = lat
        self.lon = lon
        self.lat_dir = lat_dir
        self.lon_dir = lon_dir


class coord:
    lat = np.float64    
    lon = np.float64

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon


def refDistance(lat1, lon1, lat2, lon2): #haversine
    R = 6372.8*math.pow(10,3) #earth's radius in metres
    rLat1 = math.radians(lat1)
    rLat2 = math.radians(lat2)
    rLon1 = math.radians(lon1)
    rLon2 = math.radians(lon2)
    deltaRLat = (rLat2 - rLat1)
    deltaRLon = (rLon2 - rLon1)

    a = math.pow(math.sin(deltaRLat/2),2) + (math.cos(rLat1) * math.cos(rLat2) * math.pow(math.sin(deltaRLon/2),2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def refBearing(lat2, lon2, lat1, lon1):
    rLat1 = math.radians(lat1)
    rLat2 = math.radians(lat2)
    rLon1 = math.radians(lon1)
    rLon2 = math.radians(lon2)
    deltaRLon = (rLon2 - rLon1)

    y = math.sin(deltaRLon) * math.cos(rLat2)
    x = math.cos(rLat1) * math.sin(rLat2) - math.sin(rLat1) * math.cos(rLat2) * math.cos(deltaRLon)
    theta = math.degrees(math.atan2(y, x))
    return math.fmod((theta + 360), 360)

def gpgga(data):
    #string = data.decode('UTF-8') #it's already decoded
    string = data

    index1 = 0
    index2 = string.find(",")
    time = int(round(t.time() * 1000))
    message_id = string[index1:index2]

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        utc_seconds = float(0)
    else:
        utc_seconds = float(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        lat = str(0)
    else:
        lat = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        lat_dir = str(0)
    else:
        lat_dir = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        lon = str(0)
    else:
        lon = str(string[index1+1:index2])

    index1 = index2
    index2 = string.find(",", index2+1)
    if string[index1+1:index2] == "":
        lon_dir = str(0)
    else:
        lon_dir = str(string[index1+1:index2])

    return msg_gpgga(time,message_id,utc_seconds,lat,lon,lat_dir,lon_dir)

def NMEAtoDec(lat, lat_dir, lon, lon_dir): #DDMM.MMMMM
    DDlat = int(float(lat)/100)
    MMlat = float(lat) - DDlat * 100
    DEClat = DDlat + MMlat/60
    if lat_dir == "S":
        DEClat *= -1
    varLat = DEClat

    DDlon = int(float(lon)/100)
    MMlon = float(lon) - DDlon * 100
    DEClon = DDlon + MMlon/60
    if lon_dir == "W":
        DEClon *= -1
    varLon = DEClon
    
    return coord(varLat,varLon)
    
def obtainValues(data,ref):
    #packet1 = "$GPGGA,092826.030,5700.891,N,00959.195,E,1,12,1.0,0.0,M,0.0,M,,*60"
    #packet2 = "$GPGGA,092826.035,5700.526,N,01001.784,E,1,12,1.0,0.0,M,0.0,M,,*67"
    
    #refmsgNMEA = gpgga(ref) #sorts the data
    #refmsgDec = NMEAtoDec(refmsgNMEA.lat,refmsgNMEA.lat_dir,refmsgNMEA.lon,refmsgNMEA.lon_dir) #converts lat and lon from NMEA to decimal coordinates
    refmsgDec = ref
    
    msgNMEA = gpgga(data)
    msgDec = NMEAtoDec(msgNMEA.lat,msgNMEA.lat_dir,msgNMEA.lon,msgNMEA.lon_dir)
      
    distance = refDistance(refmsgDec.lat, refmsgDec.lon, msgDec.lat, msgDec.lon) #2698.09m from nmeagenerator
    bearing = refBearing(refmsgDec.lat, refmsgDec.lon, msgDec.lat, msgDec.lon) #98.06° from nmeagenerator
    
    #print('Reference point in decimal coordinates: ', refmsgDec.lat, refmsgDec.lon)
    #print('Current point in decimal coordinates: ', msgDec.lat, ' ', msgDec.lon)
    #print('Distance in meters: ', distance)
    #print('Bearing relative to north in degrees: ', bearing)
    
<<<<<<< Updated upstream
    return distance, bearing
=======
packet1 = "$GPGGA,092826.030,5700.741,N,00954.640,E,1,12,1.0,0.0,M,0.0,M,,*60"
packet2 = "$GPGGA,092826.035,5700.747,N,00954.640,E,1,12,1.0,0.0,M,0.0,M,,*63"
refmsgNMEA = gpgga(packet1) #sorts the data
refmsgDec = NMEAtoDec(refmsgNMEA.lat,refmsgNMEA.lat_dir,refmsgNMEA.lon,refmsgNMEA.lon_dir) #converts lat and lon from NMEA to decimal coordinates
msgNMEA = gpgga(packet2)
msgDec = NMEAtoDec(msgNMEA.lat,msgNMEA.lat_dir,msgNMEA.lon,msgNMEA.lon_dir)

distance = refDistance(refmsgDec.lat, refmsgDec.lon, msgDec.lat, msgDec.lon) #2698.09m from nmeagenerator
bearing = refBearing(refmsgDec.lat, refmsgDec.lon, msgDec.lat, msgDec.lon) #98.06° from nmeagenerator
print('Reference point in decimal coordinates: ', refmsgDec.lat, refmsgDec.lon)
print('Current point in decimal coordinates: ', msgDec.lat, ' ', msgDec.lon)
print('Distance in meters: ', distance)
print('Bearing relative to north in degrees: ', bearing)
>>>>>>> Stashed changes




