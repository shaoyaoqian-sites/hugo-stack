---
title: "心肌主动收缩力模型"
description: 
slug: active-stress
date: 2025-05-28T19:43:56+08:00
image: 
math: true
license: 
hidden: false
comments: true
---

## 时变弹性模型


德宝[^1]经常使用的 Time-varying Elastance 模型 [^2][^3]，计算主动张力 ($T_{\mathrm{a}}$) 
这是一个很成熟的模型。

$$
T_{\mathrm{a}}(t,l) = \frac{T_{\mathrm{max}}}{2} \frac{\mathrm{Ca}_{0}^{2}}{\mathrm{Ca}_{0}^{2} + \mathrm{ECa}_{50}^{2}(l)} (1 - \cos(\omega(t,l)))\tag{2.8}
$$

其中， 
1. $T\_{\mathrm{max}}$ 是最大等长主动张力；
2. $\mathrm{Ca}\_{0}$ 是细胞内钙离子的峰值浓度
3. 长度相关的钙敏感性 $ECa\_{50}(l)$ 定义为

$$
\mathrm{ECa}_{50}(l) = \frac{\mathrm{Ca}_{0\mathrm{max}}}{\sqrt{e^{B(l-l_{0})} - 1}}
$$
其中 $B$ 和 $\mathrm{Ca}\_{0\mathrm{max}}$ 是常数;
$l_0$ 是能产生主动应力的最小肌节长度
$l$ 是变形后的肌节长度，由下式给出：

$$
l = l_{r} \sqrt{2E_{\mathrm{ff}} + 1}
$$

其中， $l_{r}$ 是无应力状态下的肌节长度,
$E_{\mathrm{ff}}$ 是肌纤维方向的拉格朗日应变
收缩开始后用于描述时间变化的函数 (2.8) 为

$$
\omega(t,l) = \left\{
\begin{array}{ll}
\pi \frac{t}{t_{0}} & \text{for } 0 \leqslant t \leqslant t_{0} \\
\pi \frac{t - t_{0} + t_{r}(l)}{t_{r}} & \text{for } t_{0} < t \leqslant t_{0} + t_{r} \\
0 & \text{for } t > t_{0} + t_{r}
\end{array}
\right.
$$

$t_{0}$ 为张力达到峰值的时间, $t_{r}$ 为肌肉舒张的持续时间。

$$
t_{r}(l) = ml + b
$$

$m$ 和 $b$ 为常数. 最后, 采用**主动应力法**计算心肌总Cauchy应力. 

$$
\sigma = \mathbb{F} \frac{\partial \Psi}{\partial \mathbb{F}} + \sigma^{\mathrm{a}} - p \mathbb{I}
$$

其中，$p$ 为Lagrange乘子(施加不可压性质), $\mathbb{I}$ 为单位矩阵。


<!-- ## 力电耦合模型
### FitzHugh-Nagumo电生理模型 
### Ten Tusscher-Panfilov模型 -->

<!-- ## 基于应力-应变关系的本构模型
### Niederer-Hunter-Smith模型
### Land-Ginzburg模型

## 肌纤维收缩模型 

(Fiber Contraction Model)

### Hill三元素模型
### Huxley横桥动力学模型 -->

[^1]: J. M. Guccione, A. D. McCulloch, Mechanics of active contraction in cardiac muscle: Part I—constitutive relations for fiber stress that describe deactivation, J. Biomech. Eng., 115 (1993), 72–81. https://doi.org/10.1115/1.2895473


[^2]: K. L. Sack, E. Aliotta, D. B. Ennis, J. S. Choy, G. S. Kassab, J. M. Guccione, et al., Construction and validation of subject-specific biventricular finite-element models of healthy and failing swine hearts from high-resolution dt-mri, Front. Physiol., 9 (2018). https://doi.org/10.3389/fphys.2018.00539

[^3]: Effects of dispersed fibres in myocardial mechanics, Part II: active response
