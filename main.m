clc; %清除命令窗口的内容，对工作环境中的全部变量无任何影响
clear; %清除工作空间的所有变量
close all; %关闭所有的Figure窗口 

%% 参变量、初始值
h = 0.2;   %步长
t = 0:h:2;  %节点 
n = length(t); %节点数
u0 = 1;     %初值
%% 分配存储空间
uexa = exp(-t)+t;  %准确解
numu = zeros(1,n); %数值解
numu(1) = u0;

%% 欧拉法计算
for i=1:n-1
    f = -numu(i)+t(i)+1;    % 微分方程 du/dt=-u+t+1 的右端函数
    numu(i+1) = euler1(numu(i),h,f);
end

%% 绘图
figure;
plot(t,uexa,'r-','linewidth',1);
hold on;
plot(t,numu,'b.','linewidth',1);
xlabel('t');
grid on;
title('Euler法');
ylabel('u(t)');
legend('真解','Euler法','location','northwest');
wucha_euler = (numu-uexa).^2;
disp('Euler法误差平方:');
wucha_euler
