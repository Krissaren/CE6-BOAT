
clc
clear

f = fopen('throt11150rud132652.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];

Secs = seconds(Time - Time(1));

CourseAngle = [VTG(:).TrueCourseAngle];
CourseAngle(end) = [];

%Efter 315 + 360 til alt
CourseAngleNew = CourseAngle(1:315);
CourseAngleNew1 = CourseAngle(316:end) + 360;

CourseAngleFinal = [CourseAngleNew CourseAngleNew1];

CourseAngleFinalFinal = [ones(size(CourseAngleFinal')) CourseAngleFinal'];

Vel = gradient(CourseAngleFinal)./0.05

AngleVel = regress(Secs', CourseAngleFinalFinal)

smth = mean(Secs)-AngleVel*mean(CourseAngleFinalFinal);
fx2 = @(xf) smth(4)+AngleVel(1)*xf;

fplot(fx2)
hold on 
plot(CourseAngleFinalFinal)

