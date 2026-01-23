# 安装并启用 clash，其中，ENC_PASSWORD为配置文件的解密密码
export ENC_PASSWORD="xxxxxx"

wget http://www.pengfeima.cn/cdn/other/clash.zip && unzip clash.zip && rm clash.zip && cd clash && \
wget http://www.pengfeima.cn/config/clash.yml.enc && openssl enc -d -aes-256-cbc -pbkdf2 -in clash.yml.enc -out clash.yml -pass pass:${ENC_PASSWORD} && rm clash.yml.enc && \
chmod +x ./clash

# 后台运行clash
nohup ./clash -d . -f clash.yml &

# 使用代理访问谷歌
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
wget https://www.google.com.hk