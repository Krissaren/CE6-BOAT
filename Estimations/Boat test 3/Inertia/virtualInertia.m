clear
clc
close all

txtname = ('throt12063rud189212.log');
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
for n = 1:2 %if there is more than one jump
    for i = 1:1:m-1 %Removes 360°->0°
        if (AngPos(i)-AngPos(i+1))>300
            AngPos(i+1) = AngPos(i+1)+360;
        end
        if (AngPos(i)-AngPos(i+1))<-300
            AngPos(i+1) = AngPos(i+1)-360;
        end
    end 
end

AngPosMean = movmean(AngPos,25);

% for i = 1:length(AngPos)-1 %Angular velocity. Could use gradient()
%     AngSpeed(i) = (AngPos(i+1)-AngPos(i))/(secs(i+1)-secs(i))
% end

%AngSpeedGradient = gradient(AngPosMean)./0.050;
for i = 1:length(AngPosMean)-1 %Angular velocity. Could use gradient()
    AngSpeed(i) = (AngPosMean(i+1)-AngPosMean(i))/(secs(i+1)-secs(i));
end

for i = 1:length(AngSpeed)-1 %Angular acceleration
    AngAcc(i) = (AngSpeed(i+1)-AngSpeed(i))/(secs(i+1)-secs(i));
end

rudderConst = 0.00036320754;
rudderEnc = 60000;
rudderAng = rudderConst * rudderEnc;

throttleEnc = 12000;
throttleForce = throttleEnc*0.1747-1631.5;
tau = throttleForce*sin(32)*1.2 %32° for rud = 0... 1.2m from motor to CoR

readAccel = (14.39+3.67)/(abs(28.45-29.1)) %From AngSpeed plot

inertia = tau/readAccel
inertiaCase = tau/77.8
inertiaCaseRad = tau/1.35786616

%AngSpeed = gradient(AngPos);

%plot(secs,AngPos)
plot(secs(1:length(AngSpeed)),AngSpeed)
%plot(secs(1:length(AngAcc)),AngAcc)
hold on
grid
ylabel('Degrees [°]');
xlabel('Time [s]');
legend(txtname);
%plot(secs,AngPos)
plot(secs(1:length(AngAcc)),AngAcc)
%plot(secs(1:length(AngSpeed)),AngSpeed)
hold off