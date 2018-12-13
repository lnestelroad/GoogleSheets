#!/bin/bash

echo "Working"
dir=$(pwd)
ip=$(/sbin/ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
/usr/local/bin/python3 /Users/liam/Documents/Code_Projects/Raspberry_Pi/AutoIP/quickstart.py $ip $dir > /tmp/pyLogs.txt
