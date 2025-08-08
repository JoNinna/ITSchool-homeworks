# Faceți un script de python ce genereaza un log fake. 
# Cerinte:
# - scriptul primește ca argument cate linii de log să genereze
# - fiecare linie este scrisă cu un level de logging random (INFO, WARNING, sau ERROR) 
# - fiecare linie de log contine:
#   un mesaj random dintr-o lista de mesaje predefinite de voi
#   un request id random dintr-o lista fixa de 10 request id-uri generata la începutul scriptului (fiecare request id este un UUID)
#   data și ora la care s-a printat mesajul și nivelul de logging
# Folosiți cateva comenzi de shell sa explorati log-ul generat.
    
# Hint:
# random.choice(my_list)
# uuid.uuid4()
# logging library configurata ca la curs (vezi Comenzi Utile)


import logging
import random
import sys
import uuid

# Scriptul primește ca argument cate linii de log să genereze
numar_linii = sys.argv[1]

request_id_list = []
for _ in range(10):
    request_id_list.append(uuid.uuid4())

# Sintaxa pentru list comprehension:
# request_id_list = [str(uuid.uuid4()) for _ in range(10)]

# Log to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"), # Handler care se ocupa cu scrierea in fisier
        logging.StreamHandler()         # Handler care se ocupa cu scrierea in consola
    ]
)

# Fiecare linie este scrisă cu un level de logging random (INFO, WARNING, sau ERROR) 

# In loc sa apelez functiile de logging, le-am separat intr-o lista de tupluri de tip functie - mesaj
my_logging = [ (logging.debug, "Debug info"), (logging.info, "General info"), (logging.warning, "Something might be wrong"), (logging.error, "An error happened")]

for _ in range(int(numar_linii)):
    # Cele 2 variabile vor primii valori random dintr-un tuplu din lista
    functie, mesaj = random.choice(my_logging)
    # Atribui variabilei random_uuid un id random din lista de mai sus
    random_uuid = random.choice(request_id_list)
    # Apelez functia prin variabila functie, cu parametrul mesaj
    functie(f"{random_uuid} - {mesaj}")
    

