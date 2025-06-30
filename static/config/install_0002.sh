# 安装并启用 clash
export ENC_PASSWORD="xxxxxx"
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890

wget http://www.pengfeima.cn/cdn/other/clash.zip && unzip clash.zip && rm clash.zip && cd clash && \
wget http://www.pengfeima.cn/config/clash.yml.enc && openssl enc -d -aes-256-cbc -pbkdf2 -in clash.yml.enc -out clash.yml -pass pass:${ENC_PASSWORD} && rm clash.yml.enc && \
chmod +x ./clash
nohup ./clash -d . -f clash.yml &
wget https://www.google.com.hk