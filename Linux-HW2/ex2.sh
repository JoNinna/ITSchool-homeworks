#! /bin/bash

# De adaugat exit codes si validari
# Faceți un script ce compara dacă 2 fișiere (primite ca argument) 
# sunt identice ca si continut. (sha256sum).

# args=("$@")
# primulf=${args[0]}
# aldoileaf=${args[1]}

# shaunu=$(sha256sum "$primulf" | awk '{print $1}')
# shadoi=$(sha256sum "$aldoileaf" | awk '{print $1}')

# if [ $shaunu = $shadoi ]; then
#     echo "Fisierele au acelasi continut!"
# else
#     echo "Fisierele au continut diferit!"
# fi


# Bonus (dificultate ridicata):
# În loc de 2 fișiere comparati o lista de oricât de multe fișiere. 
# Dacă oricare 2 fișiere din lista sunt diferite intoarce-ti un mesaj de eroare.  

read -p "Cate fisiere doriti sa comparati? " numarf

echo "Introduceti fisierele de comparat: " 
read -a lista_fisiere

for (( i=0; i<$numarf; i++ )); do
    for (( j=i+1; j<$numarf; j++ )); do
        sha1=$(sha256sum "${lista_fisiere[$i]}" | awk '{print $1}')
        sha2=$(sha256sum "${lista_fisiere[$j]}" | awk '{print $1}')
        if [[  "$sha1" != "$sha2" ]]; then
            echo "Continutul este diferit in fisierele: "
            echo "${lista_fisiere[$j]} si ${lista_fisiere[$i]}" 
            exit 1
        fi
    done
done

echo "Continutul este acelasi in toate fisierele!"
exit 0