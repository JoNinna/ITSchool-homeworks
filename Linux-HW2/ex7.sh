#! /bin/bash

# Faceți un script de shell numit group-list.sh 
# ce imi afiseaza toți userii ce se afla într-un grup separati prin spațiu. 
# Scriptul primește ca argument obligatoriu numele grupului. 
# Dacă nu este niciun user în grup nu afișează nimic.
# Hint: folositi o comanda similară cu aceasta: 
# cat /etc/group | grep -e "sudo:" | awk -F':' '{print $4}' | tr ',' ' '

NUME_GROUP=$1

cat /etc/group | grep -e "$NUME_GROUP:" | awk -F':' '{print $4}' | tr ',' ' '

