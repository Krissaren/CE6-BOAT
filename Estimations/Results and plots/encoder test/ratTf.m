clear
clc

k =1;
tau= 1.35;
s = tf('s');
G = k/(tau*s+1)
[B, t] = step(G);

A1=load('rat1.txt');
A2=load('rat2.txt');
A3=load('rat5.txt');

figure(1)
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)/20000)
hold on
plot(t,B)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 7])
ylim([0 1.2])
legend({'Actual step resonse','1st order approximation'},'Location','southeast')
hold off

figure(2)
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/5000)
hold on
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)/20000)
plot((A3(:,2)-A3(1,2))/1000,A3(:,1)/40000)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 7])
ylim([0 1.2])
legend({'Step = 5000','Step = 20000', 'Step = 40000'},'Location','southeast')
hold off