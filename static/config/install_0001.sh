# 安装指定版本的spack
wget https://github.com/spack/spack/releases/download/v0.22.3/spack-0.22.3.tar.gz && tar -zxf spack-0.22.3.tar.gz
rm spack-0.22.3.tar.gz && mv spack-0.22.3 spack
echo ". ~/spack/share/spack/setup-env.sh" >> ~/.bashrc && source .bashrc
. ~/spack/share/spack/setup-env.sh

# 先安装gcc11.4.0，再在指定的虚拟环境中安装fenics以及其他组件
spack install -j80 gcc@11.4.0 && spack load gcc@11.4.0 && spack compiler find && spack env create kokkos && \
  wget https://www.pengfeima.cn/config/spack_0001.yaml -O spack.yaml && mv spack.yaml ~/spack/var/spack/environments/kokkos && \
  spack env activate -p kokkos && spack concretize -f && spack install -j80

