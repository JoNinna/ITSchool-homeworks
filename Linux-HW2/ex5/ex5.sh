#!/bin/bash

# De rulat in CLI:
# BACKUP_FILE_PATH="/path/to/backup_file.txt" BACKUP_DIR="/path/to/backup_dir" ./ex5.sh

# 1. Verificare BACKUP_FILE_PATH
if [ -z "$BACKUP_FILE_PATH" ]; then
    echo "Error! Variabila BACKUP_FILE_PATH nu a fost setată!"
    exit 1
fi

# 2. Director backup cu valoare implicită
BACKUP_DIR="${BACKUP_DIR:-backup}"
mkdir -p "$BACKUP_DIR"

# 3. Date și nume fișier
timestamp=$(date +"%Y-%m-%d-%H-%M-%S")
filename=$(basename "$BACKUP_FILE_PATH")
name="${timestamp}-${filename}"

# 4. Hash fișier original
sha1=$(sha256sum "$BACKUP_FILE_PATH" | awk '{print $1}')

# 5. Comparare cu fișiere existente
found=0
for filetocompare in "$BACKUP_DIR"/*; do
    [ -e "$filetocompare" ] || continue  # evită eroarea dacă directorul e gol
    sha2=$(sha256sum "$filetocompare" | awk '{print $1}')
    if [[ "$sha1" == "$sha2" ]]; then
        mv "$filetocompare" "$BACKUP_DIR/$name"
        found=1
        break
    fi
done

# 6. Dacă nu s-a găsit backup identic, copiază
if [[ $found -eq 0 ]]; then
    cp "$BACKUP_FILE_PATH" "$BACKUP_DIR/$name"
fi
