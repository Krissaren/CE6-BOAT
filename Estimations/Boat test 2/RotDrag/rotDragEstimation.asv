
clc
clear

f = fopen('throt14957rud82295.txt');
unParsedNMEAdata = fread(f);
pnmea = nmeaParser("MessageIDs",["VTG","GGA"]);
[VTG, GGA] = pnmea(unParsedNMEAdata);

Time = [GGA(:).UTCTime];

secs = seconds(Time(1:437) - Time(1))




CourseAngle = [VTG(:).TrueCourseAngle];
CourseAngle(end) = [];

CourseAngleNew = CourseAngle(1:93);
CourseAngleNew1 = CourseAngle(94:422) + 360;
CourseAngleNew2 = CourseAngle(423:437) + 720;



CourseAngleFinal = [CourseAngleNew CourseAngleNew1 CourseAngleNew2];


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

plot(secs, CourseAngleFinal)

%%

EQs = [11260 44290 11.5; 11174 82295 15.57; 11150 132652 23.26; 13381 44260 13.23; 13344 82276 20.55;
    13431 126931 29.97; 14941 44358 12.44; 14957 82295 23.88; 14736 132652 33.86;]; %Throttle, rudder and beta for their regressions


ThrottleForce = EQs(1:9,1)*0.1747 - 1631.5

RudderAng = sind((EQs(1:9,2)*0.00036320754) - 3.1802);

RigtigVinkel = EQs(1:9,2)*0.00036320754 - 3.1802;

tau = (RudderAng.* ThrottleForce) * 1.2 

Drag = 2*tau./(EQs(1:9,3))



figure(1)
plot(EQs(1:3, 3), Drag(1:3,1), 'o')
legend('drag coefficient')
xlabel([char(176),'/s']) 
ylabel('C_{d}_{r}') 

figure(2)
plot(EQs(4:6, 3), Drag(4:6,1), 'o')
legend('drag coefficient')
xlabel([char(176),'/s']) 
ylabel('C_{d}_{r}') 
figure(3)
plot(EQs(7:9, 3), Drag(7:9,1), 'o')
legend('drag coefficient')
xlabel([char(176),'/s']) 
ylabel('C_{d}_{r}') 



