#! /bin/bash

# Faceti un script de shell cu numele group-copy.sh 
# ce copiaza userii dintr-un grup in altul.
# Scriptul primește 2 parametrii obligatorii și diferiți: 
# grupul sursa și grupul destinatie (in ordinea aceasta). 

GRUP_SURSA=$1
GRUP_DEST=$2

users=$(cat /etc/group | grep -e "$GRUP_SURSA:" | awk -F':' '{print $4}' | tr ',' ' ')

for user in $users; do
    echo "Utilizatorul $user din grupul $GRUP_SURSA va fi copiati in grupul $GRUP_DEST"
    sudo usermod -a -G "$GRUP_DEST" "$user"
done