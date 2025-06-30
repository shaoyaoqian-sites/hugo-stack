



此路径下的文件可通过 https://www.pengfeima.cn/config/xxx 获取。


# clash

export ENC_PASSWORD="x1xx29"
openssl enc -aes-256-cbc -pbkdf2 -in clash.yml -out clash.yml.enc -pass pass:${ENC_PASSWORD} # 加密
openssl enc -d -aes-256-cbc -pbkdf2 -in clash.yml.enc -out clash.yml -pass pass:${ENC_PASSWORD} # 解密

./install_0002.sh


# frp

openssl enc -aes-256-cbc -pbkdf2 -in install_0003.sh -out install_0003.sh.enc -pass pass:${ENC_PASSWORD} # 加密
openssl enc -d -aes-256-cbc -pbkdf2 -in install_0003.sh.enc -out install_0003.sh -pass pass:${ENC_PASSWORD} # 解密



./install_0003.sh

