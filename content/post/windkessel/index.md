---
title: "Windkessel模型"
description: 
slug: windkessel
date: 2025-05-27 17:29:35
image: 
math: true
license: 
hidden: false
comments: true
---


## 左心室
### open loop

主要参考了关德宝、王英杰的博士毕业论文。



困难之处:


用的不是



我是蔡力教授课题组的学生王璇，我们正在构建左心室动态收缩的数值模型，高老师建议参考您的论文，我门在数值模拟过程中遇到了几个问题，想向您请教。



![image-20250527221405212](https://githubimages.pengfeima.cn/images/202505272214311.png)



### close loop

我们计划通过通过 Windkessel 模型求解下面图中的六个未知量：

![image-20250527221042424](https://githubimages.pengfeima.cn/images/202505272210680.png)

联立下面六个方程组：

1. 主动脉电容方程：

$$
C_{AOR} \frac{dP_{AOR}}{dt} = Q_{AV} - \frac{P_{AOR} - P_{LA}}{R_{SYS}}
$$

2. 左心房电容方程：

$$
C_{LA} \frac{dP_{LA}}{dt} = \frac{P_{AOR} - P_{LA}}{R_{SYS}} - Q_{MV}
$$

3. 系统流量：

$$
Q_{\text{Sys}}=\frac{P_{\text{AOR}}-P_\text{LA}}{R_\text{Sys}}
$$

4. 主动脉瓣（AV）流量：

$$
Q_{AV} = 
\begin{cases}
\frac{P_{LV} - P_{AOR}}{R_{AV}}, & \text{if } P_{LV} > P_{AOR} \ (\text{瓣膜开放}) \\
0, & \text{otherwise}
\end{cases}
$$

5. 二尖瓣（MV）流量：

$$
Q_{MV} = 
\begin{cases}
\frac{P_{LA} - P_{LV}}{R_{MV}}, & \text{if } P_{LA} > P_{LV} \ (\text{瓣膜开放}) \\
0, & \text{otherwise}
\end{cases}
$$

6. 左心室容积变化方程（通过力学方程反馈）：

$$
\frac{dV_{LV}}{dt} = Q_{MV} - Q_{AV}
$$

