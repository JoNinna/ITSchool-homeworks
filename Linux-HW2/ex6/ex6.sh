#! /bin/bash

# Scriptul va face backup la folderul ex6 si v-a salva backup-ul in subfolderul ex6backup
# La rulare: FRECVENTA_BACKUP=5 FOLDER_BACKUP="/path/to/backup/dir" ./ex6.sh ex6

# Faceți un script ce face backup la fiecare 5 secunde la un director 
# (doar la fisierele ce s-au modificat din acel director). Scriptul primește ca argument numele directorului 
# la care trebuie făcut backup. Frecvența la care se face backup este citită dintr-o 
# variabila de mediu cu numele FRECVENTA_BACKUP (cu valoare implicită de 5 secunde). 
# Hint: 
# Folosiți comanda sha256sum pentru a verifica dacă un fișier a fost modificat.


# 1. Setam o valoare implicita pentru variabila de mediu
export FRECVENTA_BACKUP="${FRECVENTA_BACKUP:-5}"

# 2. Numele folderului monitorizat pentru backup este dat prin CLI si salvat intr-o variabila
FOLDER_MONITORED=$1

# 3. Setam folderul de backup ca variabila de mediu si daca nu exista, este creat
export FOLDER_BACKUP="${FOLDER_BACKUP:-./backup}"
mkdir -p "$FOLDER_BACKUP"

while true; do
    for file in "$"FOLDER_MONITORED"/*; do
        # 4. Noul nume al fisierului la care a fost facut backup
        timestamp=$(date +"%Y-%m-%d-%H-%M-%S")
        filename=$(basename "$file")
        name="${timestamp}-${filename}"

        sha1=$(sha256sum "$file" | awk '{print $1}')
        for filetocompare in "$FOLDER_BACKUP"/*; do
            sha2=$(sha256sum "$filetocompare" | awk '{print $1}')
            if [ "$sha1" != "$sha2" ]; then
                cp "$file" "$FOLDER_BACKUP"
            fi
        done
    done
    sleep $FRECVENTA_BACKUP"
done
