#!/bin/bash

path_to_data=$1
extension=$2

if [ -z "$path_to_data" -o -z '$extension' ]; then
    echo 'Usage: ./get_pic.sh <path to cifar-10 dataset> <image extension, e.g.: png> <optional: if not empty, class names will not be used.>'
fi
if [  -z "$(ls ${path_to_data})" ]; then
    echo "No dataset found in \'$path_to_data\'."
fi


if [ ! -d $extension ]; then
    echo "Making directory for extension \'.$extension\'."
    mkdir -p $extension/train $extension/test
    if [ -z $3 ]; then          # use class name if no parameter $3
        names=('airplane' 'automobile' 'bird' 'cat' 'deer' 'dog' 'frog' 'horse' 'ship' 'truck')
        for ((i=0;i<10;i++)); do
            mkdir $extension/train/${names[i]}
            mkdir $extension/test/${names[i]}
        done
    else
        for ((i=0;i<10;i++)); do
            mkdir $extension/train/$i
            mkdir $extension/test/$i
        done
    fi
fi

python3 ./torch_get_pic.py $1 $2 $3