#1. Importa libraria sys
import sys
import os

#2. Dacă nu au fost pasati parametrii, aruncati o exceptie
try:
    numeUtilizator = sys.argv[1]
    varstaUtilizator = sys.argv[2]
except IndexError:
    print("Nu ati introdus nici un paramentru!")
    print("Exemplu: \npython3 path/to/file.py NumeUtilizator VarstaUtilizator")

#3.a. printati mesajul “Au fost pasati <n> parametrii”
if len(sys.argv) > 0:
    print(f"Au fost pasati {len(sys.argv)} parametrii")

#3.b. daca varsta este mai mare de 18 ani, creati un subdirector pe disk cu numele utilizatorului
if int(varstaUtilizator) >= 18:
    cale = os.path.join(os.getcwd(), numeUtilizator)
    os.makedirs(cale, 0o777, exist_ok=False)
    print(f"Subdirectorul {numeUtilizator} a fost creat cu succes!")