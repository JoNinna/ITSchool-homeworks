# Faceți un modul de utils in care adaugati 2 metode: 
# una care face sha256 hash la un string si alta la un fisier. 
# Testați aceste metode de utils dintr-un alt script de python.
# Hint:
# hashlib.sha256(text.encode()).hexdigest()
# hashlib.sha256(f.read()).hexdigest()

import hashlib

def hash_string(nume_string):
    return hashlib.sha256(nume_string.encode()).hexdigest()

def hash_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


