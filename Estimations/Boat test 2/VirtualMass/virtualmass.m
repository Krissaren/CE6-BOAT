clear
clc
close all

f = fopen('throt11866E.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];
%ms = milliseconds(Time - Time(1));
secs = seconds(Time - Time(1));
%secs(end+1) = secs(end)+0.05; %Time vector is sometimes is 1 smaller, so here's fix
%secs(end) = []; %Time vector is sometimes is 1 larger, so here's fix
Speed = [VTG(:).GroundSpeed];
TOPFART = max(abs(Speed))

Accel = gradient(Speed)./0.050;
SpeedFiltered = movmean(Speed,10);
AccelFiltered = gradient(SpeedFiltered)./0.050;

readAccel = (2.94519-2.38188)/(abs(18.1-18.15))

max(abs(Accel));
virtualMass = 500/readAccel % 500 N at 12000 encoder value
%virtualMass = 995/readAccel % 1000 N at 15000 encoder value
figure(1)
plot(secs,Speed)
hold on;
xlabel('Time [s]')
%ylabel('Acceleration [m/s^2]')
ylabel('Velocity [m/s]')
legend('throt11984W')
grid
%plot(secs,AccelFiltered)
hold off;
%ylim([0 0.1])