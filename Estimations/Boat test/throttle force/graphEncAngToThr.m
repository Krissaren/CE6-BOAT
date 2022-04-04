clear;
clc;
close all;

enc = [10000; 11000; 12000; 13000; 14000; 15000; 16000; 17000; 18000; 19000; 20000]; %Encoder values
t1 = [0; 304.42; 520.46; 726.68; 854.34; 991.82; 1080.2; 1129.3; 1178.4; 1207.86; 1227.5]; %Results of test 1 in N
t2 = [49.1; 294.6; 500.82; 697.22; 854.34; 1001.64; 1070.38; 1109.66; 1139.12; 1178.4; 1227.5]; %Results of test 2 in N

% tests = [0; 304.42; 520.46; 726.68; 854.34; 991.82; 1080.2; 1129.3; 1178.4; 1207.86; 1227.5; ...
%     49.1; 294.6; 500.82; 697.22; 854.34; 1001.64; 1070.38; 1109.66; 1139.12; 1178.4; 1227.5]; %Combination of both tests

testsX = [0 49.1; 304.42 294.6; 520.46 500.82; 726.68 697.22; 854.34 854.34; 991.82 1001.64; ...
    1080.2 1070.38; 1129.3 1109.66; 1178.4 1139.12; 1207.86 1178.4; 1227.5 1227.5;]; %Matrix combination of both tests

% encs = [10000; 11000; 12000; 13000; 14000; 15000; 16000; 17000; 18000; 19000; 20000; ...
%     10000; 11000; 12000; 13000; 14000; 15000; 16000; 17000; 18000; 19000; 20000]; 

% encsX = [10000 10000; 11000 11000; 12000 12000; 13000 13000; 14000 14000; 15000 15000; ...
%     16000 16000; 17000 17000; 18000 18000; 19000 19000; 20000 20000];

hold on
plot(enc,t1,'-o',enc,t2,'-o');
legend({'First test', 'Second test','Lower values regression line','Higher values regression line'}, 'Location','southeast');
ylabel('Force[N]');
xlabel('Encoder values');
grid on
hold off
%%
means = zeros(size(enc));
for i = 1:(size(enc))
    means(i) = mean(testsX(i,:));
end

%Lower values regression line
means1=means(1:7);
enc1=enc(1:7);
x1 = [ones(size(enc1)) enc1];
beta1 = regress(means1,x1);
alpha1 = mean(means1)-beta1*mean(x1);
fx1 = @(xf) alpha1(4)+beta1(2)*xf;

%Higher values regression line
means2=means(6:11);
enc2=enc(6:11);
x2 = [ones(size(enc2)) enc2];
beta2 = regress(means2,x2);
alpha2 = mean(means2)-beta2*mean(x2);
fx2 = @(xf) alpha2(4)+beta2(2)*xf;

plot(enc,means,'-o');
hold on
xlim([10000 20000]);
ylim([0 1500]);
fplot(fx1);
fplot(fx2);
legend({'Tests mean','Lower values regression line','Higher values regression line'}, 'Location','southeast');
xlabel('Encoder values');
ylabel('Force[N]');
grid on
hold off

% %Lower values regression line
% X1 = [ones(length(enc(1:7)),1) enc(1:7)];
% b1 = X1\means(1:7);
% yCalc1 = X1*b1;
% 
% %Higher values regression line
% X2 = [ones(length(enc(6:11)),1) enc(6:11)];
% b2 = X2\means(6:11);
% yCalc2 = X2*b2;

% hold on
% plot(enc,means,'-o',enc(1:7),yCalc1,'--',enc(6:11),yCalc2,'--');
% legend({'First test', 'Second test','Lower values regression line','Higher values regression line'}, 'Location','southeast');
% xlabel('Encoder values');
% ylabel('Force[N]');
% hold off
