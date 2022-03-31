clear;
clc;
enc = [10000 11000 12000 13000 14000 15000 16000 17000 18000 19000 20000]
t1 = [0 304.42 520.46 726.68 854.34 991.82 1080.2 1129.3 1178.4 1207.86 1227.5]
t2 = [49.1 294.6 500.82 697.22 854.34 1001.64 1070.38 1109.66 1139.12 1178.4 1227.5]

% %Regression1
% X = [ones(size(enc)) enc];
% b = X \ t1
% scatter(enc,t1)
% hold on
% plot(enc, X*b)
% title('y = \beta_0 + \beta_1 x', 'FontSize',18)
% hold off
beta = mvregress(enc,t1)
x,y = zeros(enc)
y=beta(1)*x+beta(0)
plot(x,y)
%plot(enc,t1,'-o',enc,t2,'-o')
%legend({'First test', 'Second test'}, 'Location','southeast')
