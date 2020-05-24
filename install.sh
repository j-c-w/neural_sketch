#!/bin/bash

set -u

if [[ $# -ne 2 ]]; then
	echo "Expected Usage: $0 <installation directory> <data directory>"
	exit 1
fi

eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa

git checkout working-mnye
git submodule update --init --recursive
install_dir="$1"
data_dir="$2"
mkdir -p $data_dir

echo "Getting dataset...."
(
cd data
tar -xvf DeepCoder_data.tar.bz2 -C $data_dir
) > /dev/null &

pushd $data_dir
echo "Getting python...."
(wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
tar -xvf Python-3.7.6.tgz
cd Python-3.7.6
./configure --prefix=$install_dir
make && make install -j 4
cd ..) > /dev/null &
popd

wait

export PATH=$install_dir/bin:$PATH
pip3 install torch==1.4.0 numpy dill matplotlib
cd program_synthesis
pip3 install -e .
cd ..

rm data/DeepCoder_data
ln -s $data_dir/DeepCoder_data data/DeepCoder_data

echo "Done! Run:"
echo "export PATH=$install_dir/bin:\$PATH"
echo "Data is in $data_dir"
