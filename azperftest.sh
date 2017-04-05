#!/bin/bash

TIMEFORMAT="%5R %5U %5S"

tmpfile=$(mktemp /tmp/azperf_cloudlist.XXXXXX.txt)
echo ${tmpfile}

for i in {0..100..1}
do
    { time az cloud list > /dev/null ; } # 2>> ${tmpfile}
done

cat ${tmpfile}
rm ${tmpfile}

