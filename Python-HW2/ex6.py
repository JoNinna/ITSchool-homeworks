# Faceți un modul de utils (sau adaugati in modulul creat la exercițiile precedente) in care adaugati 2 metode: 
# una care face encode base64 la un text si alta care face decode base64 la text. 
# Testați aceste metode de utils dintr-un alt script de python.

import utils

text_encoding = input("Introduceti textul dorit pentru codare: ")

print(f"Textul dvs. {text_encoding} a fost codat in: {utils.encode_base64(text_encoding)}")

text_decoding = input("Introduceti textul dorit pentru decodare: ")

print(f"Textul dvs. {text_decoding} a fost decodat in: {utils.decode_base64(text_decoding)}")
