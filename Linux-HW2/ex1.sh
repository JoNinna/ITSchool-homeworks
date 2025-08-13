#! /bin/bash

# De adaugat exit codes si validari
# Faceți un script ce așteaptă (la nesfarsit) după un fisier pe disk sa fie creat (ce fișier doriti). 
# După ce fișierul a fost create scriptul afișează un mesaj și iese cu succes.
# Bonus (dificultate medie): Modificați scriptul să nu aștepte la nesfarsit ci maxim 1 minut. 
# Dar daca fisierul este create mai devreme de 1 minut scriptul trebuie sa se termine mai devreme.

nume_fisier="ex1.txt"
timeout=60
passed=0

while [ $passed -lt $timeout ]; do
    if [ -f $nume_fisier ]; then
        echo "Fisierul a fost creat pe disk!"
        exit 0
    fi 
    sleep 1
    passed=$((passed+1))
done

echo "Fisierul nu a fost creat in timpul acordat!"
exit 1

