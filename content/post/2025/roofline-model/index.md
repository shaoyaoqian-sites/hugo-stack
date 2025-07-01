---
title: "Roofline Model"
slug: roofline-model
date: 2025-06-27T01:37:26+08:00
lastmod: 2025-06-27T01:37:26+08:00
math: true
draft: false
hidden: false
comments: true
readingTime: true
image:
categories:
tags:
toc: true
---





**Roofline 模型**可以帮助我们估算：当一个模型的计算量为 A、访存量为 B，部署在一个算力为 C、内存带宽为 D 的计算平台上时，其理论性能上限 E 应该是多少。画出 **Roofline 图** 后，如下所示，其中三个最关键的参数为：

* **Memory Bound**（$\beta_\text{max}$，单位：Byte/s）：平台的最大内存访问带宽。
* **Compute Bound**（$\pi_\text{max}$，单位：FLOPs/s）：平台的最大浮点运算能力。
* **Operational Intensity**（$I_\text{max}$，单位：FLOPs/Byte）：即计算强度，表示每字节内存传输对应的浮点运算次数。在该平台上，\$I\_\text{max}\$ 表示单位内存访问最多可以支持的计算次数。

在 Roofline 图中，横轴表示计算强度（Operational Intensity），纵轴表示计算性能（Performance）。图中的**斜线**代表受内存带宽限制的上界（memory-bound），**横线**代表受计算能力限制的上界（compute-bound）。我们希望通过访存优化，使程序的性能点尽可能靠近或达到横线，意味着浮点计算资源得到了充分利用，系统运行接近峰值性能。每个kernel有三个数据，即每一行的三个点，分别表示浮点计算次数除以L1内存操作次数、L2内存操作次数、HBM内存操作次数得出的结果，三个点各自不能超过三条斜线。

<img src="https://githubimages.pengfeima.cn/images/202506241112772.jpg" alt="img" style="zoom: 50%;" />


## Nsight Compute
Nsight Compute 是 CUDA Toolkit 提供的性能分析工具。对我来说，它的基本使用流程是在 Ubuntu 系统上运行程序，下载结果到本地，再在 Windows 系统上查看结果。若需更有针对性的分析，可通过 Python 进行绘图。
### 安装

1. 在 Windows 系统上安装 CUDA Toolkit 时，NVIDIA Nsight Compute 会随之安装。
2. 在 Ubuntu 系统上，NVIDIA Nsight Compute CLI 可以通过以下命令直接安装：
    ```bash
    sudo apt install nsight-compute
    ```

### 使用

编译 CUDA 程序并运行 profiling 命令后，生成的文件可以拷贝到 Windows 系统，使用 **ncu-ui (NVIDIA Nsight Compute 的用户界面工具)** 打开。

1. **Nsight Compute 提供内置的 Roofline 配置**：通过 `--set roofline`，可以自动收集构建 Roofline 模型所需的性能指标。

2. **命令行示例**：使用以下命令运行 GPU 程序并生成分析报告：

   ```bash
   ncu --set roofline -o profile_roofline --target-processes all ./gpu_run
   ```

3. **查看 Roofline 图**：生成的 `profile_roofline.ncu-rep` 文件可以通过 `ncu-ui` 图形界面打开，在 “Roofline” 标签页中直观查看各个 kernel 的性能表现和瓶颈。

### 更详细的metrics



## Examples

#### 1. 编译









--------------

https://zhuanlan.zhihu.com/p/34204282

https://zhuanlan.zhihu.com/p/567938328

Nsight Compute profiling guide https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html

National Energy Research Scientific Computing Center https://gitlab.com/NERSC/roofline-on-nvidia-gpus/-/tree/roofline-hackathon-2020

https://gitlab.com/NERSC/roofline-on-nvidia-gpus
