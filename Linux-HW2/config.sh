#! /bin/bash

# Acesta este ex4

# Faceti un script cu numele config.sh ce face load în variabilele de mediu la variabilele definite intr-un fisier 
# config.txt ce arată în felul următor:

# DB_USER:admindb
# DB_PASS:12343dsadasdasFDTR!@13
# DB_HOSTNAME:my-db.com 
# DB_PORT:1234

set -a            # Variabilele de mediu vor fi exportate automat si in procesele copii si nu mai e nevoie sa fie setate prin exportare
source /home/ninna/work/ITSchool-homeworks/Linux-HW2/config.txt # Incarca variabilele in shell-ul curent
# Aici am folosit calea absoluta pentru a ajuta bashrc ca gaseasca fisierul config.txt cand ruleaza scriptul o data cu noul terminal.

# Cerințe bonus

# Cum facem ca variabilele setate automat în script să fie disponibile și în sesiunea de shell curentă?
# Ruland source config.sh in consola

# Cum facem ca variabilele să fie disponibile de fiecare dată când deschidem un terminal nou al userului curent?
# In fisierul ~/.bashrc, adaugam linia source /cale/catre/config.sh

# Cum facem să le setam doar dacă nu sunt deja setate?
if [ -z "$DB_USER" ]; then
    export DB_USER="SEF"
fi

