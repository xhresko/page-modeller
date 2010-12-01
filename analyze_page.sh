#!/bin/bash

echo Retrieving page from $1 ...

wget $1 -q -O temp.txt

if [ $? = 0 ]; then
    echo Download succesfull ...
    echo Trying to resolve encoding ... 
    #python3 encutils.py temp.txt
    python3 textfromweb.py temp.txt
    rm temp.txt
else
    echo Download failed ...
fi     

