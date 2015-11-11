#!/bin/bash
#retarded

mkdir imgdeps;

for i in *; do
    b=${#i}
    a=$(( b - 4 ))
    ext=${i:a:b}
    if [[ ${ext} =~ '.png' ]]; then
        cp "${i}" -t ./imgdeps
    fi
done
        
