clear
clc

f = fopen('backwind.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];
Speed = [VTG(:).GroundSpeed];


figure(1)
plot(Time,Speed)
grid
ylim([0 4])

