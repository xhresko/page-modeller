#!/bin/bash
#set -e
FILES=/home/xhresko/diplomka/data/pages/*.html
counter=0
for file in $FILES; do
  let counter+=1 
  testit=`expr $counter % 100`
  if [ $testit -eq 0 ]; then
      echo "Processing file $file"
  fi    
  cat $file |./data2utf.py |  enconv -x utf-8 | ./tag2row.sh | ./gen_model.py > $file.mod 
done
