#! /bin/bash

# Faceti un script cu numele which.sh ce:
# Parseaza variabila PATH și pune într-un array toate căile.

# Itereaza cu un for pe acest array de cai și pentru fiecare cale:
# cauta dacă acea cale contine un fisier executabil cu numele primit ca argument la script 
# (de exemplu ./which.sh ls)
# afișează toate căile ce conțin acel executabil.
# Dacă nu a găsit nicio cale ce contine acel executabil afișați în mesaj de eroare 
# și terminati scriptul cu un cod de eroare.

varpath=$(echo $PATH)

# Internal Field Separator folosit pentru a separa stringul varpath dupa : si salveaza fiecare cale in lista
IFS=":" read -ra listpaths <<< "$varpath"

filetosearch=$1
flag=0

for path in "${listpaths[@]}"; do
    if [ -x "$path/$filetosearch" ]; then
        echo "$filetosearch a fost gasit la locatia: $path"
        flag=1
    fi
done

if [[ ! "$flag" -eq 1 ]]; then
    echo "Fisierul nu a fost gasit!"
    exit 1
fi
