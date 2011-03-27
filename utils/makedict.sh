#!/bin/bash
#normline="^[0-9 aáäbcčdďeěéfghiíjklľĺmnňoôópqrřŕsštťuúůvwxyýzž.-]*$" 
normline="^[aáäbcčdďeěéfghiíjklľĺmnňoôópqrřŕsštťuúůvwxyýzž.-]*$" 
corpf="corp.txt" 
echo "" > $corpf
for file in /home/xhresko/diplomka/data/pages/*.mod; do
    cat $file | sed '$d' | cut -f 1 | grep "$normline"  >> $corpf
done     
cat $corpf | sort | uniq -c | sort -rn > dict.txt
cat dict.txt |  grep -v " [0-9] " > cleandict.txt
