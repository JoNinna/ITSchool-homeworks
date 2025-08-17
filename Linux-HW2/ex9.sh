#! /bin/bash

# Faceți un script ce dă restart la serviciul de sshd dacă este oprit. Puneți scriptul in crontab sa ruleze la fiecare minut. 
# Note:
# Cronjon-ul a fost definit prin: sudo crontab -e
# * * * * * /path/to/ex9.sh

check_status=$( systemctl status sshd | grep Active: | awk '{print $2}' )

if [ $check_status == "inactive" ]; then
    echo "Serviciul sshd va fi restartat!"
    systemctl start sshd
    recheck=$( systemctl status sshd | grep Active: | awk '{print $2}' )
    if [ $recheck == "active" ]; then
        echo "Serviciul sshd a fost restartat cu succes!"
        echo "$(date) Scriptul a rulat cu succes!" >> /home/ninna/work/ITSchool-homeworks/Linux-HW2/ex9.log
    fi
fi