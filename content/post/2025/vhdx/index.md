---
title: "Ventoy "
description: 便携式系统
date: 2025-06-01T18:36:21+08:00
image: 
math: 
license: 
tags: [ventoy, vhdx]
hidden: false
comments: true
---


安装移动系统的目的就是让你把系统装到移动硬盘的VHDX虚拟磁盘里，这样配合Ventoy之类的工具，就能随身带着自己的系统到处用，换电脑也不用重装系统。启动方式有两种：一种是直接在原来电脑的启动菜单里加个引导项，用EasyBCD改一下就行；另一种更简单，直接把VHDX文件扔进Ventoy的目录，开机从Ventoy选择系统就能进，连引导分区都不用操心。两种方法都能用，看你喜欢哪种了。

## 将系统安装到VHDX磁盘文件中

创建VHDX文件，用 WinNTSetup 工具和windows系统 iso 文件，首次创建可以小一点，因为可以扩容很简单但缩小比较困难。
https://blog.csdn.net/weixin_73636162/article/details/132497661

https://www.ventoy.net


## 扩大VHDX文件的容量


EasyBCD

https://www.ventoy.net/cn/plugin_vhdboot.html


## 为本地计算机添加引导
![](https://githubimages.pengfeima.cn/images/202501031610489.png)


## VHDX 文件扩容
![](https://githubimages.pengfeima.cn/images/202501031606869.png)
