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

主要参考：关德宝、王英杰的博士毕业论文。

## 左心室
### 开环系统

主要参考关德宝、王英杰的博士毕业论文，构建左心室动态收缩的数值模型。根据高老师的建议，初步采用三元素Windkessel模型与左心室进行耦合建模，形成一个开环系统。

1. 使用主动脉压力近似左心室压力
2. 在舒张期结束时接入Windkessel模型
3. 以左心室容积变化作为模型输入
4. 通过模型反馈获取左心室压力参数

当前遇到的主要技术难点在于压力过渡过程的模拟：

左心室舒张末期的压强为8mmHg，需上升至80mmHg后方可应用现有模型。因此需要
采用经验性线性函数描述压力跃升过程，或寻求其他更合理的建模方法。关德宝说这个过程可能会遇到一个问题，
如果压强的变化和主动收缩力不匹配，那么会出现左心室扩张过大或者剧烈收缩的现象，导致求解失败。

{{< myfigure src="https://githubimages.pengfeima.cn/images/202505272214311.png" title="开环系统" percent="30%">}}



### 闭环系统

下图修改自德宝论文[^1]的补充材料。

[^1]: Modelling of fibre dispersion and its effects on cardiac mechanics from diastole to systole

{{< myfigure src="https://githubimages.pengfeima.cn/images/202505272210680.png" title="闭环系统" percent="60%">}}

输入物理量：左心室流量 $Q_{LV}$, 输出物理量：左心室压力 $P_{LV}$. 通过Windkessel模型联立六个方程，求解以下六个关键血流动力学物理量：

| 参数类型 | 符号表示  | 物理意义     |
| :------- | :-------- | :----------- |
| 流量     | $Q_{AV}$  | 主动脉瓣流量 |
|          | $Q_{MV}$  | 二尖瓣流量   |
|          | $Q_{SYS}$ | 体循环流量   |
| 压强     | $P_{LV}$  | 左心室压力   |
|          | $P_{AO}$  | 主动脉压力   |
|          | $P_{LA}$  | 左心房压力   |

1. 文献中采用的Windkessel等效电路模型参数不能直接移植使用。






六个方程分别为：

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

