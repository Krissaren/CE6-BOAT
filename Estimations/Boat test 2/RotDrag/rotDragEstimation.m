
clc
clear

f = fopen('throt14957rud82295.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];

CourseAngle = [VTG(:).TrueCourseAngle];
CourseAngle(end) = [];

CourseAngleNew = CourseAngle(1:93);
CourseAngleNew1 = CourseAngle(94:422) + 360;
CourseAngleNew2 = CourseAngle(423:end) + 720;

CourseAngleFinal = [CourseAngleNew CourseAngleNew1 CourseAngleNew2];


CourseAngleFinalFinal = [ones(size(CourseAngleFinal')) CourseAngleFinal'];

%{
Vel = gradient(CourseAngleFinal)./0.05

AngleVel = regress(Secs', CourseAngleFinalFinal)

smth = mean(Secs)-1.21*mean(CourseAngleFinal);
fx2 = @(xf) smth+AngleVel(1)*xf;

fplot(fx2)
hold on 
plot(CourseAngleFinalFinal)



plot(CourseAngleFinalFinal)

X = [ones(size(x)) x];

beta = regress(CourseAngleFinalFinal,)
%}

plot(CourseAngleFinal)

%%

EQs = [11150 132652 1.163; 11174 82295 0.7784; 11260 44290 0.5752; 13344 82276 0.9275;
    13381 44260 0.6614; 14193 126931 1.503; 14736 132652 1.987; 14941 44358 0.6218; 14957 82295 1.094]; %Throttle, rudder and beta for their regressions

ThrottleForce = EQs(1:9,1)*0.1747 - 1631.5

RudderAng = sind((EQs(1:9,2)*0.00036320754) - 3.1802);

RigtigVinkel = EQs(1:9,2)*0.00036320754 - 3.1802

tau = (RudderAng.* ThrottleForce) * 1.2 

Drag = 2*tau./EQs(1:9,3)

plot(Drag)
hold on
plot(RigtigVinkel)
plot(ThrottleForce)
