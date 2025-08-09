# Faceți un modul de ex2utils (sau adaugati in modulul creat la exercițiile precedente) in care adaugati 2 metode: 
# una care face encode base64 la un text si alta care face decode base64 la text. 
# Testați aceste metode de ex2utils dintr-un alt script de python.

import ex2utils

text_encoding = input("Introduceti textul dorit pentru codare: ")

print(f"Textul dvs. {text_encoding} a fost codat in: {ex2utils.encode_base64(text_encoding)}")

text_decoding = input("Introduceti textul dorit pentru decodare: ")

print(f"Textul dvs. {text_decoding} a fost decodat in: {ex2utils.decode_base64(text_decoding)}")
