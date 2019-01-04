#!/bin/bash

echo "Working"
ip=$(/sbin/ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
python3 /home/pi/RaspiHeadless/quickstart.py $ip > /tmp/pyLogs.txt
