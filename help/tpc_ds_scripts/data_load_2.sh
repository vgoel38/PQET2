#!/bin/bash

for i in `ls *.dat`; do
 table=${i/.dat/}
 echo "Loading $table..."
 #sed -e 's/\(.*\).$/\1/g' $i > ./../10gb-temp/$i
 cd /home/dsladmin/pqet/postgres-11.4/bin
 ./psql tpc-ds-10 -q -c "TRUNCATE $table"
 ./psql tpc-ds-10 -c "copy $table FROM '/home/dsladmin/pqet/tpc-ds-kit/10gb-temp/$i' CSV DELIMITER '|'"
 cd /home/dsladmin/pqet/tpc-ds-kit/10gb-temp/
done
