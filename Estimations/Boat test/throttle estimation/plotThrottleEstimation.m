clear 
clc 
 
k =20000; 
tau= 1.301; 
s = tf('s'); 
G = k/(tau*s+1) 
[B, t] = step(G); 
 
A1=load('step5000.txt'); 
A2=load('step10000.txt'); 
A3=load('step15000.txt'); 
A4=load('step20000.txt'); 
 
figure(1) 
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)) 
hold on 
plot(t,B) 
xlabel('Time [s]')  
ylabel('Encoder value')  
grid on 
xlim([0 9]) 
hold off 
 
figure(2)
hold on 
plot((A1(:,2)-A1(1,2))/1000,A1(:,1)/5000)
plot((A2(:,2)-A2(1,2))/1000,A2(:,1)/10000) 
plot((A3(:,2)-A3(1,2))/1000,A3(:,1)/15000) 
plot((A4(:,2)-A4(1,2))/1000,A4(:,1)/20000) 
xlabel('Time [s]')  
ylabel('Amplitude')  
grid on 
xlim([0 7]) 
ylim([0 1.2]) 
legend({'Step = 5000','Step = 10000', 'Step = 15000', 'Step = 20000'},'Location','southeast') 
hold off