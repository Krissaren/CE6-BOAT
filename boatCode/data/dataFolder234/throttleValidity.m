clear
clc
close all
txtname = ('extraDataCleaned.csv');
%f = importdata(txtname);
f = readtable(txtname);
velocity = f.Var9;
distance = rmmissing(f.Var2);
encoderThrottle = f.Var15;
for i=1:length(distance)
    velocityError(i) = 2.46 - velocity(i);
    distanceError(i) = distance(i);
    if distance(i)*0.059<2.46
        velocityError(i) = 2.46*0.059*distance(i) - velocity(i);
        distanceError(i) = 0.059*distance(i);
    end
end

start = 1;
slut = length(distance);
figure(1)
plot(velocity(start:slut))
hold on
plot(velocityError(start:slut))
plot(encoderThrottle(start:slut)./10000)
plot(distance(start:slut)/100)
legend('Velocity', 'Velocity error', 'Desired throttle encoder value 10^-^4', 'Distance to point 10^-^2')
grid minor
%ylim([0 3.2])
hold off

figure(2)
plot(distanceError)
hold on
plot(distance)
ylim([0 40])
grid minor
hold off