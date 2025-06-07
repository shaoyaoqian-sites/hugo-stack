---
title: "附录0002"
description: 
slug: appendix-0002
date: 2025-06-03T22:08:06+08:00
image: 
hidden: true
math: true
license: 
hidden: false
comments: true
---

本文是 [《windkessel 模型》](/p/windkessel/)的附录。

## 设计开环系统




>{{< myfigure src="https://githubimages.pengfeima.cn/images/202506051622227.svg" title="收缩期的开环windkessel模型" percent="60%">}}





本文提出的winkessel模型中，由于二极管的存在，只有在射血阶段左右两边的电路是联通的，其他情况下，两边的电路都是断开的。因此，在此模型中，假设了**截断**的左心室模型和电容 $C_{LV}$ 中容纳的血液为左心室的总容积，它的变化可以通过流过$R_\text{AO}$的电流计算，在等容收缩期**截断**的左心室模型的容积发生了变化，但是我们认为左心室的容积并没有发生变化，这是符合生理常识的。

### 预加载阶段

在预加载阶段，左心室压力（$P_\text{LV}$）上升至 8 mmHg，达到舒张末期，无主动收缩模型，无windkessel模型。(0.3s)

### 等容收缩期


在等容收缩期，此时左心室开始收缩，$P_\text{LV}$ 从 8 mmHg 逐渐升高，主动脉压力（$P_\text{AO}$）从 $80\text{mmHg}$ 逐渐降低，直至两者相等。因为二极管的作用，左右两边的电路是断开的。

**左心室压强**：在更复杂的电路模型中，当其他条件保持不变时，左心室顺应性（$C_\text{LV}$） 是最关键的影响因素，其值越大，$P_\text{LV}$ 越低。相比之下，左心室阻力（$R_\text{LV}$） 的影响较弱，但其减小会导致更多电流从电容支路分流，从而进一步降低 $P_\text{LV}$。暂时考虑$R_C$为零，可能有潜在影响，暂时不考虑它。



>{{< myfigure src="https://githubimages.pengfeima.cn/images/202506051622700.svg" title="三元素windkessel模型" percent="60%">}}

**主动脉压强**：在此阶段，主动脉瓣处于关闭状态，主动脉依靠血管顺应性维持对全身的血流灌注。若采用简化电路模型（仅包含一个电容与系统血管阻力$R_\text{SYS}$串联），则主动脉压力（$P_\text{AO}$）随时间呈线性下降。

### 射血期

在射血期，左心室压强大于主动脉压强，左右两边电路连通。需要求解四个方程。

> (WIP)

### 等容舒张期

左心室压强降低到主动脉压强以下，左右电路再次断开，左心室和主动脉压强各自求解，直到周期结束。此过程中，应防止左心室压强降低到0mmHg以下，因为实际情况中，左心房，应当有经过二尖瓣流入。压强可能降到(0.8s)

### 快速充盈、舒张、心房收缩

此阶段移除windkessel模型，移除主动收缩力，内壁压力加载和预加载阶段相同。由于顺应性，主动脉压强逐渐降低。

## 设计闭环系统

>(WIP)
{{< myfigure src="https://githubimages.pengfeima.cn/images/202506051622874.svg" title="接入左心室的闭环系统" percent="60%">}}

> 三种windkessel模型
![11441748957626_.pic](https://githubimages.pengfeima.cn/images/202506032144779.jpg)
![11451748957730_.pic_hd](https://githubimages.pengfeima.cn/images/202506032145032.jpg)
![11461748958030_.pic](https://githubimages.pengfeima.cn/images/202506032144788.jpg)



