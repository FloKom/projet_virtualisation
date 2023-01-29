#!/bin/bash

ssh florian@192.168.234.180 <<EOF
cd /home/florian
mkdir -p logFiles
EOF
python3 /home/florian/features.py
scp /home/florian/features_list.json florian@192.168.234.180:/home/florian/logFiles/features_list.json
cd /home/florian/postgresql-12.0
mkdir -p /home/florian/logFiles
make check > /home/florian/logFiles/log
scp /home/florian/logFiles/log florian@192.168.234.180:/home/florian/logFiles/log
whoami > /home/florian/testFloY
