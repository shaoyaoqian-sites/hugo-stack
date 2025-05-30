---
title: 物质点方法
# description: Welcome to Hugo Theme Stack
slug: material-point-method
date: 2024-09-26 15:00:00
# lastmod: 2012-10-09 08:49:00
# image: WechatIMG415.jpg
categories:
tags:
comments: true
math: true
---



<!-- more -->

## 更新形变梯度

根据速度的欧拉描述和拉格朗日描述，
$$
\mathbf{v}(\mathbf{x},t)=\mathbf{V}\left(\chi^{-1}\left(\mathbf{x}, \mathrm{t}\right), \mathrm{t}\right)
\tag{1}
$$

$$
\mathbf{v}\left(\chi\left(\mathbf{X}, \mathrm{t}\right),t\right)=\mathbf{V}\left(\mathbf{X}, \mathrm{t}\right)
\tag{2}
$$

我们可以得到速度与形变梯度的关系:
$$
\frac{\partial}{\partial t} \mathbb{F}\left(\mathbf{X}, t\right)=\nabla_{\mathbf{X}}\mathbf{V}\left(\mathbf{X}, t\right)=\nabla_\mathbf{x} \mathbf{v}(\mathbf{x},t)\mathbb{F}\left(\mathbf{X}, t\right) .
$$

假设我们得到了$t_{n+1}$时刻定义在当前构型$B_{t_{n}}$上的速度为$\mathbf{v}\left(\chi\left(\mathbf{X}, \mathrm{t}\_{n}\right),t\_{n+1}\right)$, (在欧拉网格上求解速度，根据已知的$\chi(\mathbf{X},t_n)$求得), 采用时间离散:
$$
\frac{\partial}{\partial t} \mathbb{F}\left(\mathbf{X}, t_{n+1}\right)=\nabla_\mathbf{x} \mathbf{v}(\chi\left(\mathbf{X}, \mathrm{t}_{n}\right),t_{n+1})\mathbb{F}\left(\mathbf{X}, t_{n}\right) .\tag{6}
$$
将方程 (6) 代入下面式子，
$$
\frac{\partial}{\partial t} \mathbb{F}\left(\mathbf{X}, t^{n+1}\right) \approx \frac{\mathbb{F}^{n+1}-\mathbb{F}^n}{\Delta t}
$$

可以得到
$$
F_p^{n+1}=F_p^n+\Delta t \frac{\partial v^{n+1}}{\partial x}\left(x_p^n\right) F_p^n=\left(I+\Delta t \frac{\partial v^{n+1}}{\partial x}\left(x_p^n\right)\right) F_p^n
$$



and of course if we use the grid based interpolation formula for $\boldsymbol{v}^{\mathfrak{n}+1}$, i.e.,
$$
\begin{aligned}
v^{n+1}(x) & =\sum_i v_i^{n+1} N_i(x) \\
\frac{\partial v^{n+1}}{\partial x}(x) & =\sum_i v_i^{n+1}\left(\frac{\partial N_i}{\partial x}(x)\right)^{\top}
\end{aligned}
$$

then we have

$$
F_p^{n+1}=\left(I+\Delta t \sum_i v_i^{n+1}\left(\frac{\partial N_i}{\partial x}\left(x_p^n\right)\right)^{\top}\right) F_p^n
$$

as the update rule for ${F_p^{\mathfrak{p}}}^{n+1}$ given the $v_i^{n+1}$ and $F_{\mathfrak{p}}^n$.



## 更新位移

## 更新力


Symplectic Euler MPM

1. 计算$m_i^n$和$\mathbf{v}^n_i$

2. 计算出力源项$\mathbf{f}_i^n$
3. 更新速度$\mathbf{v}^{n+1}_i$
4. 更新形变梯度$\mathbb{F}_p^{n+1}$
5. 更新速度$\mathbf{v}_p^{n+1}$和$\mathbf{x}_p^{n+1}$





拉格朗日点
$$
\mathbf{X}_i=\chi^{-1}(\mathbf{x}_i,t)
$$
$\mathbf{x}_i^{n+1}$ 为此拉格朗日点下一时刻的坐标。



## 获取网格上的速度

(与浸没边界法类似)

## 更新力

$$
\begin{equation}
f_i(\boldsymbol{x})=-\frac{\partial e}{\partial x_i}(\boldsymbol{x})=-\sum_p V_p^0\left(\frac{\partial \Psi_p}{\partial F}\left(F_p(x)\right)\right)\left(F_p^n\right)^{\top} \nabla w_{i p}^n .
\end{equation}
$$

$$
\begin{equation}
f_i^n=f_i\left(x_i^n\right)=-\sum_p V_p^0\left(\frac{\partial \Psi_p}{\partial F}\left(F_p^n\right)\right)\left(F_p^n\right)^{\top} \nabla w_{i p}^n,
\end{equation}
$$

## 更新速度



## 更新形变梯度

$$
\begin{equation}
F_p^{n+1}=\left(I+\Delta t \sum_i v_i^{n+1}\left(\nabla w_{i p}^n\right)^{\top}\right) F_p^n
\end{equation}
$$















如果我们想要给出一个类似的定义，我们可以定义一个张量场 \(\Psi\) 对另一个张量场 \(\mathbb{F}\) 的变化率的散度。在数学上，这可以表示为：

$$
\nabla \cdot (\Psi \cdot \nabla \mathbb{F}
$$
这里，\(\nabla \cdot\) 表示散度算子，\(\Psi\) 是一个张量场，\(\nabla \mathbb{F}\) 表示张量场 \(\mathbb{F}\) 的梯度，而 \(\cdot\) 表示张量乘积。

然而，这个表达式与原始问题中的表达式仍然不同，因为原始问题中的表达式是：

\[
\nabla \cdot \left( \frac{\partial \Psi}{\partial \mathbb{F}} \right)
\]

这表示张量场 \(\Psi\) 对张量场 \(\mathbb{F}\) 的偏导数的散度。

如果我们想要定义一个与原始表达式类似的表达式，我们可以考虑定义张量场 \(\Psi\) 对张量场 \(\mathbb{F}\) 的偏导数的散度，并且乘以张量场 \(\mathbb{F}\) 对空间坐标 \(x\) 的偏导数，可以表示为：

\[
\nabla \cdot \left( \frac{\partial \Psi}{\partial \mathbb{F}} \cdot \frac{\partial \mathbb{F}}{\partial x} \right)
\]

这个表达式表示的是张量场 \(\Psi\) 对张量场 \(\mathbb{F}\) 的偏导数与张量场 \(\mathbb{F}\) 对空间坐标 \(x\) 的偏导数的乘积的散度。这与原始表达式不同，因为它包含了散度算子和乘积。