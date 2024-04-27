#!/usr/bin/env bash
while :
do
   fio --name=fiotest --ioengine=libaio --size 1Gb --rw=read --bs=1M --direct=1 --numjobs=4 --iodepth=8 --runtime=60 --startdelay=60 --group_reporting
   rm fiotest*
   sleep 5s
done
