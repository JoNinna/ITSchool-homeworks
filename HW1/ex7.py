# Vrei să monitorizezi timpul de răspuns al unui site web pentru a verifica dacă serverul răspunde rapid. 
# Scriptul va trimite cereri HTTP la fiecare 2 secunde și va afișa timpul de răspuns în milisecunde.

import time
import requests

import urllib3

# Dezactiveaza warning-urile SSL 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. Scrieți o funcție ce primește ca parametru un url și întoarce timpul de răspuns al paginii (cat dureaza sa primim un răspuns)
def raspuns_Fisier(url):
    call_time = time.time()
    call = requests.get(url,verify=False)
    response_time = time.time() - call_time
    return f"Timpul de raspuns al site-ului {url} este: {response_time}" 

def raspuns_Lista(url):
    call_time = time.time()
    call = requests.get(url,verify=False)
    response_time = time.time() - call_time
    return response_time

# 2. Adaugati încă o funcție ce primește doi parametrii (un url si un numar de repetari)
def call_outputFisier(url, iteratii):
# Funcția va face într-un for un număr de cal-uri către url și va memora timpurile de răspuns într-un fisier text (folosind prima metoda)
    with open("raspunsuri.txt","a") as file:
        for iterator in iteratii:
            context = raspuns(url)
            file.write(context + "\n")

# Funcția va face într-un for un număr de cal-uri către url și va memora timpurile de răspuns într-o listă (folosind prima metoda)
# Si va face o medie și va întoarce într-un tuplu 3 valori în următoarea ordine: (min, media, max)
def call_outputLista(url, iteratii):
    listaTimpRaspuns = []
    for iterator in iteratii:
        iterator = raspuns_Lista
        listaTimpRaspuns.append(iterator)

url = input("Introduceti adresa url: ")
iteratii = input("Introduceti numarul de iteratii: ")
call_outputLista(url, iteratii)
