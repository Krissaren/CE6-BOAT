clear
clc
%distance
R = 6372.8*10^3;
%Fredrik Bajers Vej 7 til Idrætsbyen
rLon1 = 9.986583*pi/180;
rLat1 = 57.01485*pi/180;
%rLon2 = 9.958233*pi/180;
%rLat2 = 57.0262*pi/180;
%
rLon2 = 10.029733*pi/180;
rLat2 = 57.008766*pi/180;

deltaRLat = (rLat2 - rLat1);
deltaRLon = (rLon2 - rLon1);
a = sin(deltaRLat/2)^2+cos(rLat1)*cos(rLat2)*sin(deltaRLon/2)^2;
c = 2 * sin(sqrt(a));
distance = R*c

%bearing
y = sin(deltaRLon)*cos(rLat2);
x = cos(rLat1)*sin(rLat2)-sin(rLat1)*cos(rLat2)*cos(deltaRLon);
theta = atan2(y, x)*180/pi;
bearing = mod(theta+360,360)