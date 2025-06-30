



此路径下的文件可通过 https://www.pengfeima.cn/config/xxx 获取。


# clash


https://www.pengfeima.cn/config

wget http://localhost:1313/config/clash.yml.enc


```
export ENC_PASSWORD="x1xx29"
openssl enc -aes-256-cbc -pbkdf2 -in clash.yml -out clash.yml.enc -pass pass:${ENC_PASSWORD} # 加密
openssl enc -d -aes-256-cbc -pbkdf2 -in clash.yml.enc -out clash.yml -pass pass:${ENC_PASSWORD} # 解密
```

export ENC_PASSWORD="x1xx29"
wget http://localhost:1313/cdn/other/clash.zip && unzip clash.zip && rm clash.zip && cd clash && \
wget http://localhost:1313/config/clash.yml.enc && openssl enc -d -aes-256-cbc -pbkdf2 -in clash.yml.enc -out clash.yml -pass pass:${ENC_PASSWORD} && \
nohup ./clash -d . -f clash.yml & && export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 && \
wget -O- https://www.google.com.hk | cat


