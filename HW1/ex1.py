#1. Defineste cate o variabila din fiecare tip invatat

nume = "Ana Popescu"
varsta = 25
student = True
observatii = None
cursuri = ["istorie", "chimie", "geografie"]
prioritati = {"examene", "voluntariat", "job"}
note = {
    "istorie": 10,
    "chimie": 10,
    "geografie": 10
}
parcurs_cariera = ("voluntar", "student", "angajat")

#2. Pentru fiecare variabila afișați valoarea și tipul ei folosind metoda print
print(f"Variabila {nume} este de tip: {type(nume)}")
print(f"Variabila {varsta} este de tip: {type(varsta)}")
print(f"Variabila {student} este de tip: {type(student)}")
print(f"Variabila {observatii} este de tip: {type(observatii)}")
print(f"Variabila {cursuri} este de tip: {type(cursuri)}")
print(f"Variabila {prioritati} este de tip: {type(prioritati)}")
print(f"Variabila {note} este de tip: {type(note)}")
print(f"Variabila {parcurs_cariera} este de tip: {type(parcurs_cariera)}")

#3. Creați o alta variabila cu numele documentație de tip string pe mai multe linii
documentatie = """
Variabila X1 este de tipul Y1 si are valoare Z1
Variabila X2 este de tipul Y2 si are valoare Z2
"""

#4. Afisati si acest string documentatie in consola
print(documentatie)





