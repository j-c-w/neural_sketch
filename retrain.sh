#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 <output directory>"
	exit 1
fi

output_directory="$1"
rm -rf saved_models $output_directory
mkdir -p $output_directory
ln -s $output_directory saved_models

python3 train/main_supervised_deepcoder.py --pretrain
