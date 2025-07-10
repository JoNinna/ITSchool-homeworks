# Folosiți libraria facuta de voi pentru a genera un sha256 hash pentru un fisier de pe disk si comparati-l cu valoarea obtinuta ruland comanda de linux sha256sum.

import utils
import subprocess
import os

nume_string = "test123"
fisier = "/Python-HW2/ex1.py"
nume_fisier = os.path.join(os.getcwd() + fisier)

def verificare():
    print(f"Hash-ul pentru valoarea string este: {utils.hash_string(nume_string)}")

    #Salvez hash-ul generat de tip bytes
    hash_f = utils.hash_fisier(nume_fisier)
    print(f"Hash-ul pentru fisierul {nume_fisier} este: {hash_f}")

    # Generez hash prin comanda sha254sum si captez output-ul
    comanda_shell = subprocess.run(["sha256sum", nume_fisier], capture_output=True) 
    # Outputul returnat si salvat in comanda_shell este de tip bytes, si trebuie decodat in string
    output = comanda_shell.stdout.decode() 
    # Din output-ul de tip string, luam primul argument, adica hash code-ul
    hash_shell = output.split()[0]
    print(f"Hash-ul generat de comanda sha256sum este: {hash_shell}")
    if hash_f == hash_shell:
        print("Hash-ul obtinut prin modul utils este acelasi cu cel obtinut prin comanda sha256sum!")

verificare()




