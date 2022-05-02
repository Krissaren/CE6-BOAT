clear
clc
close all

txtname = ('throt11937rud189212.log');
f = fopen(txtname);
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];
%ms = milliseconds(Time - Time(1));
secs = seconds(Time - Time(1));
%secs(end+1) = secs(end)+0.05; %Time vector is sometimes is 1 smaller, so here's fix
%secs(end) = []; %Time vector is sometimes is 1 larger, so here's fix
AngPos = [VTG(:).TrueCourseAngle];

m = length(AngPos);
for n = 1:3 %if there is more than one jump
    for i = 1:1:m-1 %Removes 360°->0°
        if (AngPos(i)-AngPos(i+1))>300
            AngPos(i+1) = AngPos(i+1)+360;
        end
        if (AngPos(i)-AngPos(i+1))<-300
            AngPos(i+1) = AngPos(i+1)-360;
        end
    end 
end

%for i = 1:length(AngPos)-1
for i = 1:length(AngPos)-1 %Angular velocity. Could use gradient()
    AngSpeed(i) = (AngPos(i+1)-AngPos(i))/(secs(i+1)-secs(i));
end

AngPosMean = movmean(AngPos,35); %1515151515
%AngSpeedGradient = gradient(AngPosMean)./0.050;
for i = 1:length(AngPosMean)-1 %MEAN Angular velocity. Could use gradient()
    AngSpeedMean(i) = (AngPosMean(i+1)-AngPosMean(i))/(secs(i+1)-secs(i));
end

for i = 1:length(AngSpeed)-1 %Angular acceleration
    AngAcc(i) = (AngSpeed(i+1)-AngSpeed(i))/(secs(i+1)-secs(i));
end
for i = 1:length(AngSpeedMean)-1 %MEAN Angular acceleration
    AngAccMean(i) = (AngSpeedMean(i+1)-AngSpeedMean(i))/(secs(i+1)-secs(i));
end
%AngAccMean2 = movmean(AngAcc,50) 
rudderConst = 0.00036320754;
rudderEnc = 60000;
rudderAng = rudderConst * rudderEnc;

disp(txtname)
throttleEnc = 12000;
throttleForce = throttleEnc*0.1747-1631.5;
disp(['Force = ',num2str(throttleForce)]);
tau = throttleForce*sind(16)*1.2; %32° for rud = 0... 1.2m from motor to CoR
disp(['Tau = ',num2str(tau)]);

X1 = 47.45;
Y1 = -16.0267;
X2 = 48.65;
Y2 = 0.4;

disp(['X1: ', num2str(X1), ' ', 'Y1: ', num2str(Y1), ' ', 'X2: ', num2str(X2), ' ', 'Y2: ', num2str(Y2)]) 
readAccel = abs((Y2-Y1)/(X2-X1)); %From AngSpeed plot
disp(['Accel = ',num2str(readAccel)]);
%accel = 163; %From AngAcc plot

inertia = tau/readAccel;
disp(['Inertia = ',num2str(inertia)]);
%inertiaCase = tau/163.733 %Peak acceleration in AngAcc plot at shut-off
%inertiaCaseRad = tau/1.35786616;

%AngSpeed = gradient(AngPos);

%plot(secs,AngPos,'LineWidth',2)
plot(secs(1:length(AngSpeedMean)),AngSpeedMean,'LineWidth',2)
%plot(secs(1:length(AngAcc)),AngAcc)
hold on
grid
grid minor
ylabel('Angular velocity [°/s]');
xlabel('Time [s]');
legend(txtname);
plot(secs,AngPos)
%plot(secs(1:length(AngAccMean)),AngAccMean)
%plot(secs(1:length(AngSpeed)),AngSpeed)
hold off

%% PLOTTING RESULTS
clear
clc
close all

%k encoder, clockwise rotation
twecw16 = [11.2543 11.2334; 16 16];
fifcw16 = [17.197 14.3837; 16 16];
twecw32 = [12.1346 12.7795; 32 32];
fifcw32 = [14.7309 12.3606; 32 32];

tweccw16 = [10.2204 13.2868; 16 16];
fifccw16 = [17.3082 15.2931; 16 16];
tweccw32 = [10.7249 10.5249; 32 32];
fifccw32 = [12.6699 10.5414; 32 32];

mean16 = mean([twecw16(1,:) fifcw16(1,:) tweccw16(1,:) fifccw16(1,:)]);
mean32 = mean([twecw32(1,:) fifcw32(1,:) tweccw32(1,:) fifccw32(1,:)]);
mean12k = mean([twecw16(1,:) twecw32(1,:) tweccw16(1,:) tweccw32(1,:)]);
mean15k = mean([fifcw16(1,:) fifcw32(1,:) fifccw16(1,:) fifccw32(1,:)]);
mean = mean([twecw16(1,:) fifcw16(1,:) tweccw16(1,:) fifccw16(1,:)...
    twecw32(1,:) fifcw32(1,:) tweccw32(1,:) fifccw32(1,:)])

width = 2;
plot(twecw16(2,:),twecw16(1,:),'o','LineWidth',width)
hold on
plot(fifcw16(2,:),fifcw16(1,:),'o','LineWidth',width)
plot(twecw32(2,:),twecw32(1,:),'o','LineWidth',width)
plot(fifcw32(2,:),fifcw32(1,:),'o','LineWidth',width)
plot(tweccw16(2,:),tweccw16(1,:),'o','LineWidth',width)
plot(fifccw16(2,:),fifccw16(1,:),'o','LineWidth',width)
plot(tweccw32(2,:),tweccw32(1,:),'o','LineWidth',width)
plot(fifccw32(2,:),fifccw32(1,:),'o','LineWidth',width)
legend('465N, clockwise', '989N, clockwise', '465N, clockwise', '989N, clockwise',...
    '465N, counter-clockwise', '989N, counter-clockwise', '465N, counter-clockwise', '989N, counter-clockwise')
grid
grid minor
xlabel('Absoloute angle of rudder [°]')
ylabel('Inertia [kg*m^2]')
xlim([10 40])
ylim([5 25])
hold off
