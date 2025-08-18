#! /bin/bash

# Adauga automat hasbang in fisierele de sh in care nu este prezent. 
# Scriptul verifica toate scripturile sh dintr-un director primit ca parametru.

check_folder=$1

for file in $check_folder/*; do
    name=$(basename "$file")
    check_extension="${name##*.}"
    if [ $check_extension == "sh" ]; then
        if [[ -z $(grep "#! /bin/bash" "$file") ]]; then
            sed -i '1i#! /bin/bash' $file
            echo "In fisierul $file a fost adaugata linia de shebang!"
        else
            echo "Fisierul $file are linia de shebang!"
        fi
    fi
done
