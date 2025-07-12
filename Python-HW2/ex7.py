# Faceti un script de python care primeste ca argument un string base64 si un nume de fisier. 
# Scriptul o sa creeze pe disk un fișier cu numele primit ca argument și o sa ii puna ca și conținut stringul 
# decodat din base64.

import sys
import utils

nume_string_byte = sys.argv[1]
nume_fisier = sys.argv[2]

with open(nume_fisier, "w") as file:
    file.write(utils.decode_base64(nume_string_byte))



