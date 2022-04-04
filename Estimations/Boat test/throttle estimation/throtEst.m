clear
clc

k =1;
%A1 tau = 0.951
%A2 tau = 0.9
%A3 tau = 1.101
%A4 tau = 1.35
tau= 0.9;
s = tf('s');
G = k/(tau*s+1)
[B, t] = step(G);

A1=load('step5000.txt');
A2=load('step10000.txt');
A3=load('step15000.txt');
A4=load('step20000.txt');

figure(1)
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/10000)
hold on
plot(t,B)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 6])
ylim([0 1.2])
legend({'Measured step resonse','1st order approximation'},'Location','southeast')
hold off

%%
figure(2)
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)/5000)
hold on
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/10000)
plot((A3(:,2)-A3(1,2))/1000,A3(:,1)/15000)
plot((A4(:,2)-A4(1,2))/1000,A4(:,1)/20000)
xlabel('Time [s]') 
ylabel('Amplitude') 
grid on
xlim([0 6])
ylim([0 1.2])
legend({'Step = 5000','Step = 10000', 'Step = 15000', 'Step = 20000'},'Location','southeast')
hold off