# Faceți un script de python ce muta unul cate unul fisierele dintr-un director în celalat. 
# După fiecare mutare de fișier scriptul doarme un numar random de secunde intre 1 si 5 (pentru a simula un long running process). 
# Directorul sursa este primul argument al scriptului iar destinatie al doilea. 
# Incercati sa porniti in acelasi timp 2 instante ale scriptului și verificati ca ambele funcționează corect.
# Hint:
# os.makedirs(dest_dir, exist_ok=True)
# src_path = os.path.join(source_dir, filename)
# os.rename(src_path, lock_path)
# time.sleep(random.randint(1, 5))
# shutil.move(lock_path, dest_path)

import os
import sys
import time
import shutil
import random

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

print(f"Fisierele din folderul {source_dir} vor fi mutate in folderul {dest_dir}")

os.makedirs(dest_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    src_path = os.path.join(source_dir, filename)
    # Fisierul primeste .lock pentru a semneala ca este locked, blocat temporal
    lock_path = os.path.join(source_dir, filename + ".lock")
    
    try:
        # Fisierul este redenumit temporal in folderul sursa pentru a bloca un alt proces
        os.rename(src_path, lock_path)
    except FileNotFoundError:
        print("Fisierele nu sunt disponibile pentru a fi mutate!")
        continue
    except PermissionError:
        print("Nu aveti permisiunile necesare!")
        continue
    except OSError:
        print("Fisierele sunt deja procesate!")
        continue

    dest_path = os.path.join(dest_dir, filename)

    print(f"Fisierul {filename} va fi mutat in {dest_path}")

    shutil.move(lock_path, dest_path)
    
    time.sleep(random.randint(1, 5))
