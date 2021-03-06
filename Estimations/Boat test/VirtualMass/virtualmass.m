clear
clc
close all

f = fopen('headwind.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];
%ms = milliseconds(Time - Time(1));
secs = seconds(Time - Time(1));
Speed = [VTG(:).GroundSpeed];
%Accel = movmean(gradient(Speed)./0.050,5); %Movmean is probably not legal
Accel = gradient(Speed)./0.050;
AccelFiltered = lowpass(gradient(Speed)./0.050,0.1);

virtualMass = (9.82*125)/max(abs(Accel))
figure(1)
plot(secs,Accel)
hold on;
grid
plot(secs,AccelFiltered)
hold off;
%ylim([0 0.1])