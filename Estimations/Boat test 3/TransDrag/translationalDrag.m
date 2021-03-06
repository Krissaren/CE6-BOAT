clear
clc
close all

txtname = ('throt15006(4).log');
throttleEnc = 15000; %CHANGE TO ENCODER VALUE
f = fopen(txtname);
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Speed = [VTG(:).GroundSpeed];
%Speed = rmmissing([VTG(:).GroundSpeed]); %removes NaN from data

Time = [GGA(:).UTCTime];
secs = seconds(Time - Time(1));
secsHomemade = [0:1:length(Speed)-1]*0.05;

MeanSpeed = mean(Speed)
MeanHeading = mean(rmmissing([VTG(:).TrueCourseAngle]))

Force = throttleEnc*0.1747-1631.5
DragConst = Force/(0.5*MeanSpeed^2)

figure(1)
plot(secsHomemade,Speed)
hold on
grid
ylim([0 max(Speed)+0.1*max(Speed)])
xlabel('Time [s]')
ylabel('Velocity [m/s]')
legend(txtname)

figure(2) %Plotting heading to check validity of data
plot(secsHomemade, rmmissing([VTG(:).TrueCourseAngle]))
grid
ylim([0 360])
xlabel('Time [s]')
ylabel('Heading [°]')
legend(txtname)
hold off


%% Plotting results
clear
clc
close all

%Encoder value - rough heading - 1st or 2nd = MeanSpeed; DragConst
K11E1 = [1.9435; 153.6593];
K11E2 = [2.0737; 134.9693];
K11W1 = [2.8887; 69.5542];
K11W2 = [2.9581; 66.3278];
K13E1 = [2.2450; 253.8106];
K13E2 = [2.1379; 279.8870];
K13W1 = [3.1057; 132.6247];
K13W2 = [3.1224; 131.2077];
K15E1 = [2.5350; 307.8076];
K15E2 = [2.5377; 307.1545];
K15W1 = [3.1957; 193.6841];
K15W2 = [3.2076; 192.2536];

EastSpeeds = [K11E1(1); K11E2(1); K13E1(1); K13E2(1); K15E1(1); K15E2(1)];
EastDrags = [K11E1(2); K11E2(2); K13E1(2); K13E2(2); K15E1(2); K15E2(2)];
WestSpeeds = [K11W1(1); K11W2(1); K13W1(1); K13W2(1); K15W1(1); K15W2(1)];
WestDrags = [K11W1(2); K11W2(2); K13W1(2); K13W2(2); K15W1(2); K15W2(2)];

SpeedsCheat = [(K11E1(1)+K11E2(1)+K11W1(1)+K11W2(1))/4;...
    (K13E1(1)+K13E2(1)+K13W1(1)+K13W2(1))/4;...
    (K15E1(1)+K15E2(1)+K15W1(1)+K15W2(1))/4;]

Forces = [290.2000; 639.6000; 989];
DragsCheat = [Forces(1)/(0.5*SpeedsCheat(1)^2);...
    Forces(2)/(0.5*SpeedsCheat(2)^2);...
    Forces(3)/(0.5*SpeedsCheat(3)^2)]

width = 2;
figure(1)
plot(SpeedsCheat,DragsCheat,'LineWidth',width)
hold on
grid
legend('Averaged')
ylabel('Drag constant')
xlabel('Velocity [m/s]')
hold off

figure(2)
plot(EastSpeeds,EastDrags,'LineWidth',width-1)
hold on
plot(WestSpeeds,WestDrags,'LineWidth',width-1)
plot(EastSpeeds,EastDrags,'o','LineWidth',width);
plot(WestSpeeds,WestDrags,'o','LineWidth',width);
legend('East','West')
ylabel('Drag constant')
xlabel('Velocity [m/s]')
grid
hold off

ForcesForAvg = [290.2000; 290.2000; 639.6000; 639.6000; 989; 989];
figure(3)
plot(EastSpeeds,EastDrags,'LineWidth',width-1)
hold on
%plot(ForcesForAvg,EastDrags,'LineWidth',width-1)
plot(WestSpeeds,WestDrags,'LineWidth',width-1)
plot(SpeedsCheat,DragsCheat,'LineWidth',width-1)
plot(EastSpeeds,EastDrags,'o','LineWidth',width);
plot(WestSpeeds,WestDrags,'o','LineWidth',width);
plot(SpeedsCheat,DragsCheat,'o','LineWidth',width);
%plot(ForcesForAvg,WestDrags,'LineWidth',width)
%plot(Forces,DragsCheat,'LineWidth',width)
legend('East','West','Averaged')
ylabel('Drag constant')
xlabel('Velocity [m/s]')
%xlabel('Force [N]')
grid
hold off