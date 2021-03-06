clear
clc
%11kE
f = fopen('throt10751E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed11kE = [VTG(:).GroundSpeed];
avgSpeed11kE = mean(Speed11kE);
maxSpeed11kE = max(Speed11kE);
minSpeed11kE = min(Speed11kE);
maxDeviation11kE = max([mean(abs(avgSpeed11kE-maxSpeed11kE)) mean(abs(avgSpeed11kE-minSpeed11kE))]);
percDeviation11kE = maxDeviation11kE/avgSpeed11kE*100
    
%11kW
f = fopen('throt10773W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed11kW = [VTG(:).GroundSpeed];
avgSpeed11kW = mean(Speed11kW);
maxSpeed11kW = max(Speed11kW);
minSpeed11kW = min(Speed11kW);
maxDeviation11kW = max([mean(abs(avgSpeed11kW-maxSpeed11kW)) mean(abs(avgSpeed11kW-minSpeed11kW))]);
percDeviation11kW = maxDeviation11kW/avgSpeed11kW*100

%13kE
f = fopen('throt13142E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed13kE = [VTG(:).GroundSpeed];
Speed13kE = Speed13kE(1:750); % There is huge drop in speed at the end because the motor is turned off, hence that data is not used
avgSpeed13kE= mean(Speed13kE);
maxSpeed13kE= max(Speed13kE);
minSpeed13kE = min(Speed13kE);
maxDeviation13kE = max([mean(abs(avgSpeed13kE-maxSpeed13kE)) mean(abs(avgSpeed13kE-minSpeed13kE))]);
percDeviation13kE = maxDeviation13kE/avgSpeed13kE*100

%13kW
f = fopen('throt12819W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed13kW = [VTG(:).GroundSpeed];
avgSpeed13kW= mean(Speed13kW);
maxSpeed13kW= max(Speed13kW);
minSpeed13kW = min(Speed13kW);
maxDeviation13kW = max([mean(abs(avgSpeed13kW-maxSpeed13kW)) mean(abs(avgSpeed13kW-minSpeed13kW))]);
percDeviation13kW = maxDeviation13kW/avgSpeed13kW*100

%15kE
f = fopen('throt15065E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed15kE = [VTG(:).GroundSpeed];
avgSpeed15kE= mean(Speed15kE);
maxSpeed15kE= max(Speed15kE);
minSpeed15kE = min(Speed15kE);
maxDeviation15kE = max([mean(abs(avgSpeed15kE-maxSpeed15kE)) mean(abs(avgSpeed15kE-minSpeed15kE))]);
percDeviation15kE = maxDeviation15kE/avgSpeed15kE*100

%15kW
f = fopen('throt15065W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);
Speed15kW = [VTG(:).GroundSpeed];
avgSpeed15kW= mean(Speed15kW);
maxSpeed15kW= max(Speed15kW);
minSpeed15kW = min(Speed15kW);
maxDeviation15kW = max([mean(abs(avgSpeed15kW-maxSpeed15kW)) mean(abs(avgSpeed15kW-minSpeed15kW))]);
percDeviation15kW = maxDeviation15kW/avgSpeed15kW*100
