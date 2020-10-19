#!/bin/bash

# This script should be run IN ADDITION to the install.sh script.
# Also, it ISN'T designed to run on the cluster, but on a local
# machine.

if [[ -f pypy3.6-v7.3.1-linux64.tar.bz2 ]]; then
	rm pypy3.6-v7.3.1-linux64.tar.bz2
fi
if [[ -d pypy3.6-v7.3.1-linux64 ]]; then
	rm -rf pypy3.6-v7.3.1-linux64
fi

wget https://bitbucket.org/pypy/pypy/downloads/pypy3.6-v7.3.1-linux64.tar.bz://downloads.python.org/pypy/pypy3.6-v7.3.2-linux64.tar.bz2 
tar -xvjf pypy3.6-v7.3.1-linux64.tar.bz2
cd pypy3.6-v7.3.1-linux64

echo "Make sure to run the following: "
echo "export PATH=\$PATH:$PWD/bin"
