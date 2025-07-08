# 1. Folosește o buclă for pentru a parcurge fiecare linie din fișier.
with open("logs.txt","r") as log_file:
    numar_line = 1
    for line in log_file:
        #2. Verifică dacă linia conține cuvântul ERROR
        if "ERROR" in line:
            #3. Afișează linia și numărul acesteia dacă conține ERROR
            print(f"Cuvantul ERROR a fost gasit in log-ul: \n{line} \nAnume linia {numar_line}")
        numar_line += 1