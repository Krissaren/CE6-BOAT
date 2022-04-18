clear
clc


%enc = [10000 11000 12000 14000 16000 20000] % Encoder values used in test

%t1 = [0 304.42 520.46 854.34 1080.2 1227.5]; % Test 1
%t2 = [49.1 294.6 500.82 854.34 1070.38 1227.5]; % Test 2


%Test 11kE
f = fopen('throt10751E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time11kE = [GGA(:).UTCTime];
Speed11kE = [VTG(:).GroundSpeed];

[n m] = size(Speed11kE); % Finding amount of speed measurements. 

AvgEnc11kE = sum(Speed11kE)/m % Average velocity for the vessel.

%Test 11kW
f = fopen('throt10773W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time11kW = [GGA(:).UTCTime];
Speed11kW = [VTG(:).GroundSpeed];

[n m] = size(Speed11kW); % Finding amount of speed measurements. 

AvgEnc11kW = sum(Speed11kW)/m % Average velocity for the vessel.

%Test 13kW
f = fopen('throt12819W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time13kW = [GGA(:).UTCTime];
Speed13kW = [VTG(:).GroundSpeed];

[n m] = size(Speed13kW); % Finding amount of speed measurements. 

AvgEnc13kW = sum(Speed13kW)/m % Average velocity for the vessel.

%Test 13kE
f = fopen('throt13142E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time13kE = [GGA(:).UTCTime];
Speed13kE = [VTG(:).GroundSpeed];

Speed13kE1 = Speed13kE(1:700)

[n m] = size(Speed13kE1); % Finding amount of speed measurements. 

AvgEnc13kE = sum(Speed13kE1)/(m) % Average velocity for the vessel.


%Test 15kE
f = fopen('throt15065E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time15kE = [GGA(:).UTCTime];
Speed15kE = [VTG(:).GroundSpeed];

[n m] = size(Speed15kE); % Finding amount of speed measurements. 

AvgEnc15kE = sum(Speed15kE)/m % Average velocity for the vessel.

%Test 15kW
f = fopen('throt15065W.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time15kW = [GGA(:).UTCTime];
Speed15kW = [VTG(:).GroundSpeed];

[n m] = size(Speed15kW); % Finding amount of speed measurements. 

AvgEnc15kW = sum(Speed15kW)/m % Average velocity for the vessel.

%%%%
%enc = [11000; 13000; 15000; 0; 19000; 20000]; %Encoder values
%t1 = [520.46; 854.34; 1080.2]; %Results of test 1 in N
%t2 = [500.82; 854.34; 1070.38];

forceTest11k = (304.42 + 294.6)/2 % Calculate average propulsion force from the two tests.
forceTest13k = (726.68 + 697.22)/2 % Calculate average propulsion force from the two tests.
forceTest15k = (991.82 + 1001.64)/2 % Calculate average propulsion force from the two tests.

dragConstant11kE = 2*forceTest11k/AvgEnc11kE^2
dragConstant11kW = 2*forceTest11k/AvgEnc11kW^2
dragConstant13kE = 2*forceTest13k/AvgEnc13kE^2
dragConstant13kW = 2*forceTest13k/AvgEnc13kW^2
dragConstant15kE = 2*forceTest15k/AvgEnc15kE^2
dragConstant15kW = 2*forceTest15k/AvgEnc15kW^2



%totSpeed = [AvgEnc11kE AvgEnc11kW AvgEnc13kE AvgEnc13kW AvgEnc15kE AvgEnc15kW] 

%dragConstants = [dragConstant11kE dragConstant11kW dragConstant13kE dragConstant13kW dragConstant15kE dragConstant15kW]

totSpeedE = [AvgEnc11kE AvgEnc13kE AvgEnc15kE] 

dragConstantsE = [dragConstant11kE dragConstant13kE dragConstant15kE]

totSpeedW = [AvgEnc11kW AvgEnc13kW AvgEnc15kW] 

dragConstantsW = [dragConstant11kW dragConstant13kW dragConstant15kW]



figure(1)
plot(totSpeedE, dragConstantsE, '-o')
hold on 
xlabel('Velocity [m/s]')  
ylabel('Drag constant')  
grid on 
xlim([1.8 5]) 
ylim([40 500]) 

figure(2)
plot(totSpeedW, dragConstantsW, '-o')
hold on 
xlabel('Velocity [m/s]')  
ylabel('Drag constant')  
grid on 
xlim([1.8 3.5]) 
ylim([40 500]) 
hold off

