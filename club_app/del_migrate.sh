#! /bin/bash
base_dir=$(pwd)
# dirs= $(ls -d */)
# echo base_dir = $base_dir
# echo dirs = $dirs
# echo $(ls -d */)

for dir in $(ls -d */)
do
    if [ -d $dir/migrations/ ]
    then
        echo $dir/migrations/
    else
        continue
    fi
    cd $dir/migrations/
    # echo $(pwd)
    # echo $(ls -df * | grep -v __init__.py)
    ls -df * | grep -v __init__.py | xargs rm -r
    cd $base_dir
done