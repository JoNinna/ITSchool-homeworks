# Faceți un modul de utils in care adaugati 2 metode: 
# una care face sha256 hash la un string si alta la un fisier. 
# Testați aceste metode de utils dintr-un alt script de python.
# Hint:
# hashlib.sha256(text.encode()).hexdigest()
# hashlib.sha256(f.read()).hexdigest()

import hashlib
import base64

def hash_string(nume_string):
    return hashlib.sha256(nume_string.encode()).hexdigest()

def hash_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def encode_base64(text_encoding):
    byte_my_text = text_encoding.encode('utf-8')
    return base64.b64encode(byte_my_text)

def decode_base64(text_decoding):
    return base64.standard_b64decode(text_decoding).decode('utf-8')
