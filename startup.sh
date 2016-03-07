#!/bin/bash
export DISPLAY=:99

while true; do
    python pucauto_de.py
    echo $(date +"%D %T") "Restarting..."
    killall firefox.real
    #killall firefox
    rm -rf /tmp/tmp*
    sleep 3
done
