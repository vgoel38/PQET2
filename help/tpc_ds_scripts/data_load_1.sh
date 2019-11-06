#!/bin/bash

for i in `ls *.dat`; do
 table=${i/.dat/}
 echo "Loading $table..."
 sed -e 's/\(.*\).$/\1/g' $i > ./../10gb-temp/$i
done