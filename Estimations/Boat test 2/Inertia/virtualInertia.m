clear
clc
close all

txtname = ('throt12967rud60000.txt');
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
for i = 1:1:m-1 %Removes 360°->0°
    if (AngPos(i)-AngPos(i+1))>350
        AngPos(i+1) = AngPos(i+1)+360;
    end
    if (AngPos(i)-AngPos(i+1))<-350
        AngPos(i+1) = AngPos(i+1)-360;
    end
end 
AngPos = movmean(AngPos,20);

for i = 1:length(AngPos)-1 %Angular velocity. Could use gradient()
    AngSpeed(i) = (AngPos(i+1)-AngPos(i))/(secs(i+1)-secs(i));
end

for i = 1:length(AngSpeed)-1 %Angular acceleration
    AngAcc(i) = (AngSpeed(i+1)-AngSpeed(i))/(secs(i+1)-secs(i));
end

throtConst = 0.00036320754;
rudderEnc = 60000;
rudderAng = throtConst * rudderEnc;

throttleEnc = 13000;
tau = throttleEnc*0.1747-1631.5

readAccel = (14.39+3.67)/(abs(28.45-29.1))

inertia = tau/readAccel

%AngSpeed = gradient(AngPos);

plot(secs(1:744),AngSpeed)
%plot(secs(1:743),AngAcc)
hold on
grid
ylabel = ('Degrees [°]');
xlabel = ('Time [s]');
legend = (txtname);
%plot(secs,AngPos)
%plot(secs(1:743),AngAcc)
hold off