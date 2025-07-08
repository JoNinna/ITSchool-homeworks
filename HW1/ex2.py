#1. Citește o variabila cu numele “parolă” introdusă de utilizator, folosind metoda input()
parola_introdusa = input("Introduceti parola: ")

#2. Verifica dacă variabila are aceeași valoare ca o variabila de mediu cu numele PAROLA_SECRETA
import os
os.environ["PAROLA_SECRETA"] = "admin"     #seteaza variabila de mediu PAROLA_SECRETA
parola = os.environ.get("PAROLA_SECRETA")  #atribuie variabila de mediu unei variabile folosite pentru comparare

#3. Dacă are aceeași valoare, printati “Parola corecta”, în caz contrar afișați parola greșită
if parola_introdusa == parola:
    print("Ati introdus parola corecta!")
else:
    print("Ati introdus parola gresita!")
