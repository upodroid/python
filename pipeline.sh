#!/bin/bash
cp -r $WORKSPACE/* /home/jenkins
python /home/jenkins/app.py &
sleep 10s
ps -ef | grep python
echo
netstat -tulpn4
echo
kill $(ps aux | grep app.py | awk '{print $2}')
rm -rf /home/jenkins/*

 
