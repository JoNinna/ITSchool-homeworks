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

# lista_fisiere=()

args=("$@")

read -p "Cate fisiere doriti sa comparati? " numarf

echo "Introduceti fisierele de comparat: " 
read -a lista_fisiere

for index in $numarf; do
    echo "${lista_fisiere[${index}]}"
    i=$((index+1))
    echo "${lista_fisiere[${i}]}"
    # sha1=$(sha256sum "${lista_fisiere[index]}" | awk '{print $1}')
    # sha2=$(sha256sum "${lista_fisiere[index+1]}" | awk '{print $1}')
done

# for $item in $numarf; do  
#     read -p "Introduceti urmatorul fisier de comparat: " urmatorulf
#     urmatorulf=$args[item]
#     echo "$urmatorulf"
#     item=$(item+1)

