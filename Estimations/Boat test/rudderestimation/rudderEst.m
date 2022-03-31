clear
clc

k =1;
%A1 tau =1
%A2 tau = 0.9
%A3 tau = 1.301
%A4 tau = 2.601
%A5 tau = 5.102
%A6 tau = 7.553

tau= .9;
s = tf('s');
G = k/(tau*s+1)
[B, t] = step(G);

A1=load('step5000.txt');
A2=load('step10000.txt');
A3=load('step20000.txt');
A4=load('step40000.txt');
A5=load('step80000.txt');
A6=load('step120000.txt');

figure(1)
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/10000)
hold on
plot(t,B)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 7])
ylim([0 1.2])
legend({'Actual step resonse','1st order approximation'},'Location','southeast')
hold off
%%
figure(2)
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)/5000)
hold on
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/10000)
plot((A3(:,2)-A3(1,2))/1000,A3(:,1)/20000)
plot((A4(:,2)-A4(1,2))/1000,A4(:,1)/40000)
plot((A5(:,2)-A5(1,2))/1000,A5(:,1)/80000)
plot((A6(:,2)-A6(1,2))/1000,A6(:,1)/120000)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 10])
ylim([0 1.2])
legend({'Step = 5000','Step = 10000', 'Step = 20000', 'Step = 40000', 'Step = 80000', 'Step = 120000'},'Location','southeast')
hold off