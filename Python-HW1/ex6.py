# Vrei să monitorizezi aplicatia ex6-script.sh și să te asiguri că procesul rulează continuu. 
# Dacă procesul se oprește, codul python va încerca să îl pornească din nou

import subprocess
import time

# 5. Numele procesului ce trebuie monitorizat este hardcodat într-o variabila la începutul scriptului
process_name = "ex6-script.sh"

# 1. Folosește o buclă while pentru a monitoriza în mod continuu procesul.
while True:
    # 2. Verifică dacă procesul este activ folosind comanda pgrep
    process_check = subprocess.run(["pgrep", "-f", process_name], capture_output=True, text=True)
    
    # 3. Dacă procesul nu este găsit, pornește aplicația din nou
    if process_check.returncode != 0:
        subprocess.run(["./ex6-script.sh > /dev/null 2>&1 &"],shell=True)
        # 4. Afișează un mesaj de avertizare de fiecare dată când procesul este repornit
        print("Scriptul a fost repornit cu succes!")
    else:
        time.sleep(2)
        print("Scriptul ruleaza cu succes!")
