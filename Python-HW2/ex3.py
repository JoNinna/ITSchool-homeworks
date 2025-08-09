# Faceti un script de python ce face backup la un fisier (doar dacă acesta a fost modificat). 
# Calea catre fișierul la care face backup este primita ca argument. 
# Puneti scriptul de python in crontab sa ruleze automat la fiecare minut.
# Hint: 
# hashlib.sha256(f.read()).hexdigest() (reutilizati metoda de la ex2)
# os.listdir(backup_dir)
# os.path.isfile(file_path)
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# shutil.copy2(file_path, backup_name)

# pentru a rula crontab din terminal:
# crontab - e
# * * * * * /cale/python-installed /cale/catre/script.py /cale/catre/fisierul/backup

import os
import sys
import ex2utils
import shutil
from datetime import datetime

# Numele fișierul la care face backup este primit ca argument si construim calea fisierului pentru backup 
fisier = sys.argv[1]

nume_fisier, extensie_fisier = os.path.splitext(os.path.basename(fisier)) #nume_fisier = test si extensie_fisier = .txt
fisier_pt_backup = os.path.abspath(fisier) #Returneaza calea absoluta a fisierului pasat 

# Definim numele fisierului in care urmeaza sa salvam hash-ul initial, ATENTIE, NU hash-ul actual
fisier_hash = f"hash_{nume_fisier}.txt"

# Se foloseste functia hash_fisier din fisierul ex2utils pentru a genera hash-ul actual si ulterior pentru a fi comparat cu hash-ul initial cu scopul de a veadea daca fisierul a suferit modificari 
hash_actual = ex2utils.hash_fisier(fisier_pt_backup)

hash_initial = None

# Daca exista fisierul fisier_hash, inseamna ca fisierul pasat a fost modificat
if os.path.exists(fisier_hash):
    with open(fisier_hash, "r") as file:
        hash_initial = file.read().strip() #citim hash-ul si eliminam spatiile redundante

if hash_actual != hash_initial:
    print("Fisierul a fost modificat, se face backup pentru ultima versiune...")

    backup_dir = "backup "
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime. now().strftime("%Y%m%d_%H%M%S")
    nume_backup = f"{nume_fisier}-{timestamp}{extensie_fisier}"

    cale_pt_backup = os.path.join(backup_dir,nume_backup)

    shutil.copy2(fisier_pt_backup,cale_pt_backup)

    # Scriem in fisierul de evidenta hash, noul hash, pentru a-l avea salvat pentru comparatii viitoare in caz de alte modificari asupra fisierului pasat
    with open(fisier_hash, "w") as file:
        file.write(hash_actual)
else:
    print("Fisierul nu a fost modificar, prin urmare nu se face backup!")








