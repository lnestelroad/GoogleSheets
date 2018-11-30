#!/bin/bash

echo "Working"
dir=$(pwd)
ip=$(/sbin/ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
python3 quickstart.py $ip $dir
