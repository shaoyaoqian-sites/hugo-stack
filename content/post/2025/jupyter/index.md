---
title: "Jupyter"
slug: python-juputer
date: 2025-06-09T22:24:48+08:00
lastmod: 2025-06-09T22:24:48+08:00
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

我最近想搭个 Jupyter Lab, 主要出于这几个原因：

1. 调试 Windkessel 模型：需要一个方便画图、能轻松分享结果的环境（受够了在本地画完图还要到处传文件😂）
2. 学习 Pyvista 可视化：想在网页上直接展示计算结果，pyvista 的 3D 可视化效果很酷炫，以后通过代码可重复画图
3. 学习 FEniCSx ：正在学这个有限元分析工具，Jupyter 的交互特性很适合边学边试

## 安装 Jupyter 和 pyvista

```bash
pip install 'jupyterlab>=3' ipywidgets 'pyvista[all,trame]'
pip install notebook
jupyter notebook password
jupyter notebook --port=9202 --ip=0.0.0.0
```

然后设置外网访问[^1][^2], 需要注意, 在 Nginx Proxy Manager 打开 Websocket Support 才能执行代码，否则只能写代码。
![image-20250518173009001](https://githubimages.pengfeima.cn/images/202505181730334.png)

## 运行pyvista

可以选择前端显示或者后端显示。

![image-20250518113614370](https://githubimages.pengfeima.cn/images/202505181136541.png)

## Jupyter执行环境切换


```bash
python -m venv circadapt

```
```bash
# 假设已经激活 python 环境
pip3 install ipykernel
python -m ipykernel install --user --name=spack_fenics --display-name="FEniCSx Spack"
jupyter kernelspec uninstall fenics_spack
```





## 系统默认启动

> 我通过ssh登陆命令执行脚本，尽可能与命令行执行命令的环境相同

```bash
sudo vi /etc/systemd/system/manyservices.service
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
sudo systemctl enable manyservices.service 
# sudo systemctl daemon-reload
sudo systemctl restart manyservices.service 
sudo journalctl -u manyservices.service -n 100
```

```bash
ssh fenics@localhost "export DISPLAY=:99.0 && source ~/pyvenv/bin/activate && jupyter notebook --port=9202 --ip=0.0.0.0 --notebook-dir=/home/fenics/jupyter"
```

```ini
[Unit]
Description=many services
After=network.target syslog.target
Wants=network.target

[Service]
Type=simple
# 指定运行用户和组
User=fenics
Group=fenics
# 启动命令
Restart=on-failure    
RestartSec=5s
ExecStart=/bin/bash /home/fenics/start_services.sh

[Install]
WantedBy=multi-user.target
```









[^1]: http://talk.pengfeima.cn/t/topic/278/4?u=merryjingle
[^3]: https://tutorial.pyvista.org/tutorial/00_jupyter/index.html
[^2]: https://jupyter.pengfeima.cn
