clear
clc
close all
txtname = ('extraData.txt');
%f = importdata(txtname);
f = readtable(txtname);
bearingError = f.Var22;
bearing = f.Var4;
refBearing = f.Var7;
encoderRudder = f.Var19;
angRudderRad = encoderRudder*6.363*10^-6%*(180/pi)
angRudderDeg = encoderRudder*0.3646*10^-3
plot(bearingError)
hold on
plot(angRudderDeg)
plot(bearing)
plot(refBearing)
legend('Bearing error', 'Desired rudder angle', 'Bearing', 'Reference bearing')
grid minor

