# #! /bin/bash

# Log rotation: 
# Faceți un script ce face log rotation la un fisier de loguri primit ca argument. 
# Pentru simplitate log rotation-ul se face automat la un numar de secunde primit 
# ca argument. Cand se face log rotation se copiază fișierul curent într-un nou fișier 
# cu același nume ca fișierul original + un timestamp iar fișierul original se golește. 
# Fisierele de log rotation se și arhivează pentru a ocupa mai puțin spațiu.
# Faceți un script simplu ce printeaza la nesfarsit in loguri pentru a testa scriptul de 
# log rotation (vedeti hello.sh de la curs). 

log_file=$1
rotation_time=$2

timestamp=$(date +"%Y-%m-%d-%H-%M-%S")
name=$(basename "$log_file" ".log")
new_name="${name}-${timestamp}.log"

# Pentru ca de fiecare data cand ruleaza scriptul, se creaza un nou fisier de rotatie,
# am folosit trap pentru a capta keyboard interrupt si inainte de exit, ruleaza arhivarea 
trap "tar -cvf logs-archive.tar logs-*; exit" INT

while true; do
    cat "${log_file}" >> "$new_name"
    > "$log_file"
    sleep "$rotation_time"
done


