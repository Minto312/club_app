#! /bin/bash
base_dir=$(pwd)
dirs= ls -d */

for dir in $dirs
do
    cd $dir/migrations/
    
    cd $base_dir
done