---
title: "主动脉瓣程序运行说明"
slug: revise-cmame-1
date: 2025-06-24T22:09:18+08:00
lastmod: 2025-06-24T22:09:18+08:00
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
投稿CMAME的论文返回了修改意见，需要重新跑一些程序，顺便增加一些features。

- [x] 加密主动脉管道的网格密度，以及固定位移的惩罚系数，以观察压强的斑点是否减少。
- [x] 增加背景网格密度，重新跑程序
- [x] 用V100、P100重新跑一遍，比较不同模块的时间
- [x] 为网格创建modelscope仓库
- [x] 添加swanlab功能
- [x] 将flowrate上传到swanlab
- [x] 时间统计采用浮点数

----

### 分支 cmame-1

此分支从`Commit: 5a67c5d6262fb745af53c89a7005956ee25bd767`创建，目的是为了文章的修改意见修改一部分代码。

```bash
source .bashrc # 激活环境
cd build  && cmake .. && make -j # 编译
python3 ../demos/demo_3392.py  # 生成配置文件
taskset -c 101 nohup ./gfem_main_av config/test101.json > log/gfem-101.out & # 后台运行程序
git archive --format=zip --output=cmame-1.zip cmame-1 
```



现在创建分支cmame-1，需要进行分析。将所有文件放到同一个中运行。

在分支中运行。



### 网格

网格文件放在哪一直是一个令人头疼的问题。

#### 加密主动脉管道的网格：

1. 网格现在同一放到hugging face 的私有仓库中，需要添加密钥才能下载。
   `git clone git@hf.co:datasets/mapengfei/mesh-cardiology`

2. 网格文件通过 `gzip mesh.xda` 命令压缩后上传。

3. 生成瓣膜叶的`xdmf`网格，之后按次序执行四个程序。

   ` python3 1.mesh_data.py`

4. `gunzip -k *.gz` 解压gz文件，但是不删除它们



### 在 P100 和 V100 上的运行

需要在 P100 和 V100 两种设备上重新运行主动脉瓣膜的流固耦合程序。更多信息请参见：[Release PAPER-CMAME-2025 · npuheart/npuheart](https://github.com/npuheart/npuheart/releases/tag/v0.1.7-post1)。在运行之前，请先确认 `cat ~/spack/var/spack/environments/kokkos/spack.yaml` 文件的内容，确保依赖的安装正确，然后再编译运行程序。

```bash
spack env activate -p kokkos
spack concretize -f
spack install
```

```yaml
# spack-0.22.3.tar.gz
spack:
  specs:
  - kokkos-kernels@4.3.00 +cuda cuda_arch=70 %gcc@11.4.0
  - kokkos@4.3.00 ~openmp +cuda +cuda_lambda +cuda_constexpr +wrapper cuda_arch=70 cxxstd=20
  # FEniCS
  - fenics@2019.1.0.post0 +zlib build_type=Release cflags="-O3"
  - petsc@3.14.0 +mumps +hdf5
  - boost@1.71.0
  - openmpi@4.0.6 +cuda
  - python@3.10.10 +optimizations
  - py-matplotlib
  - py-cython@0.29.36
  # NPUHeart
  - muparser # 2.3.4
  - fmt@10.1.1
  - nlohmann-json@3.11.2
  - py-pip
  - spdlog
  - pugixml
  view: true
  concretizer:
    unify: true

  packages:
    all:
      compiler: [gcc@11.4.0]
```





### features

流体求解器需要作为插件，独立于整个流固耦合系统，可以独立切换。

现在的时间统计结果：

<img src="https://githubimages.pengfeima.cn/images/ed7b55393b801bb9009eb4f0578a89f8.png" alt="ed7b55393b801bb9009eb4f0578a89f8" style="zoom: 50%;" />