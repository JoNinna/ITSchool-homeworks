#! /bin/bash

# De adaugat exit codes si validari
# Faceți un script ce așteaptă (la nesfarsit) după un fisier pe disk sa fie creat (ce fișier doriti). 
# După ce fișierul a fost create scriptul afișează un mesaj și iese cu succes.

while true; do
    sleep Infinity
    if [ -e $1 ]; then
        echo "Fisierul exista deja pe disk!"
    else
        echo >> $1
        exit 0
    fi 
done

# Bonus (dificultate medie): Modificați scriptul să nu aștepte la nesfarsit ci maxim 1 minut. 
# Dar daca fisierul este create mai devreme de 1 minut scriptul trebuie sa se termine mai devreme.