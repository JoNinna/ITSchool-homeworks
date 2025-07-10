# Vrei să monitorizezi timpul de răspuns al unui site web pentru a verifica dacă serverul răspunde rapid. 
# Scriptul va trimite cereri HTTP la fiecare 2 secunde și va afișa timpul de răspuns în milisecunde.

import time
import requests

import urllib3

# Dezactiveaza warning-urile SSL 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. Scrieți o funcție ce primește ca parametru un url și întoarce timpul de răspuns al paginii (cat dureaza sa primim un răspuns)
def raspuns(url):
    call_time = time.time()
    call = requests.get(url,verify=False)
    response_time = (time.time() - call_time) * 1000
    return response_time

# 2. Adaugati încă o funcție ce primește doi parametrii (un url si un numar de repetari)
def apel(url, iteratii):
    # Funcția va face într-un for un număr de cal-uri către url și va memora timpurile de răspuns într-o listă (folosind prima metoda)
    listaTimpRaspuns = []
    for iterator in range(int(iteratii)):
        iterator = raspuns(url)
        print(f"Timpul de raspuns pentru site-ul {url} este: {iterator:.2f} milisecunde")
        listaTimpRaspuns.append(iterator)
        time.sleep(2)

    # Si va face o medie și va întoarce într-un tuplu 3 valori în următoarea ordine: (min, media, max)
    media = sum(listaTimpRaspuns)/len(listaTimpRaspuns)
    minimum = min(listaTimpRaspuns)
    maximum = max(listaTimpRaspuns)
    return (minimum, media, maximum)

url = input("Introduceti adresa url: ")
iteratii = input("Introduceti numarul de iteratii: ")
print(f"Minimul, media si maximum-ul de valori de raspuns sunt: {apel(url, iteratii)}")
