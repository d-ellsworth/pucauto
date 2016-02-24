#!/bin/bash

while true; do
    python pucauto.py
    echo $(date +"%D %D") "Restarting..."
    killall firefox
    killall firefox.real
    sleep 3
done
