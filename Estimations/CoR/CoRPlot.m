clear
clc
close all

acc=load('accImuData6.txt');
gyro=load('gyroImuData6.txt');
accTot=(acc(:,5)+acc(:,6)+acc(:,7)-1);
gyroTot=gyro(:,5)+ gyro(:,6)+ gyro(:,7);
x = linspace(0, 22385, 22385);
yyaxis right
plot(round(x/125,2),round(gyroTot,2))
ylim([-2 4])
ylabel('Incremental angle [°]')
hold on
grid
yyaxis left
plot(round(x/125,2),round(accTot*9.80665,2))
ylim([-2 4])
legend('Acceleration','Incremental angle')
xlim([0 22385/125])
xlabel('Seconds [s]')
ylabel('Acceleration [m/s^2]')
hold off
a1=mean(acc(5804:8909,5)+acc(5804:8909,6)+acc(5804:8909,7)-1)*9.80665
a2=mean(acc(10600:14270,5)+acc(10600:14270,6)+acc(10600:14270,7)-1)*9.80665
a3=mean(acc(15370:19000,5)+acc(15370:19000,6)+acc(15370:19000,7)-1)*9.80665

w1=deg2rad(mean(gyro(5804:8909,5)+ gyro(5804:8909,6)+ gyro(5804:8909,7))*125)
w2=deg2rad(mean(gyro(10600:14270,5)+ gyro(10600:14270,6)+ gyro(10600:14270,7))*125)
w3=deg2rad(mean(gyro(16140:18540,5)+ gyro(16140:18540,6)+ gyro(16140:18540,7))*125)


dist1 = a1/(w1^2)
dist2 = a2/(w2^2)
dist3 = a3/(w3^2)

avgDist=(dist1 + dist2 + dist3)/3
%%
clear
clc
close all

acc=load('accImuData3.txt');
gyro=load('gyroImuData3.txt');
accTot=(acc(:,5)+acc(:,6)+acc(:,7)-1);
gyroTot=(gyro(:,5)+ gyro(:,6)+ gyro(:,7));
yyaxis right
plot(gyroTot)
ylim([-2 3])
ylabel('Incremental angle [°]')
hold on
grid
yyaxis left
plot(accTot*9.80665)
ylim([-2 3])
legend('Acceleration','Incremental angle')
xlabel('Samples')
ylabel('Acceleration [m/s^2]')
hold off

a1=mean(acc(4750:7970,5)+acc(4750:7970,6)+acc(4750:7970,7)-1)*9.80665
w1=deg2rad(mean(gyro(4750:7970,5)+ gyro(4750:7970,6)+ gyro(4750:7970,7))*125)
dist1 = a1/(w1^2)


%%
clear
clc
close all

acc=load('accImuData.txt');
gyro=load('gyroImuData.txt');
accTot=(acc(:,5)+acc(:,6)+acc(:,7)-1);
gyroTot=gyro(:,5)+ gyro(:,6)+ gyro(:,7);
yyaxis right
plot(gyroTot)
ylim([-1.5 5])
ylabel('Incremental angle [°]')
hold on
grid
yyaxis left
plot(accTot*9.80665)
ylim([-1.5 5])
legend('Acceleration','Incremental angle')
xlabel('Samples')
ylabel('Acceleration [m/s^2]')
hold off

a1=mean(acc(5600:7500,5)+acc(5600:7500,6)+acc(5600:7500,7)-1)*9.80665
w1=deg2rad(mean(gyro(5600:7500,5)+ gyro(5600:7500,6)+ gyro(5600:7500,7))*125)
dist1 = a1/(w1^2)

%%
clear
clc
close all

acc=load('accImuData5.txt');
gyro=load('gyroImuData5.txt');
accTot=(acc(:,5)+acc(:,6)+acc(:,7)-1);
gyroTot=gyro(:,5)+ gyro(:,6)+ gyro(:,7);
yyaxis right
plot(gyroTot)
ylim([-1.5 5])
ylabel('Incremental angle [°]')
hold on
grid
yyaxis left
plot(accTot*9.80665)
ylim([-1.5 5])
legend('Acceleration','Incremental angle')
xlabel('Samples')
ylabel('Acceleration [m/s^2]')
hold off

a1=mean(acc(8000:10900,5)+acc(8000:10900,6)+acc(8000:10900,7)-1)*9.80665
w1=deg2rad(mean(gyro(8000:10900,5)+ gyro(8000:10900,6)+ gyro(8000:10900,7))*125)
dist1 = a1/(w1^2)

%%
clear
clc
close all

acc=load('accImuData6.txt');
gyro=load('gyroImuData6.txt');
accTot=(acc(5000:20000,5)+acc(5000:20000,6)+acc(5000:20000,7)-1);
gyroTot=gyro(5000:20000,5)+ gyro(5000:20000,6)+ gyro(5000:20000,7);
x = linspace(0, 15000, 15001);
yyaxis right
plot(x/125,gyroTot)
ylim([-1.5 5])
ylabel('Incremental angle [°]')
hold on
grid
yyaxis left
plot(x/125,accTot*9.80665)
ylim([-1.5 5])
legend('Acceleration','Incremental angle')
xlim([0 15000/125])
xlabel('Seconds [s]')
ylabel('Acceleration [m/s^2]')
hold off