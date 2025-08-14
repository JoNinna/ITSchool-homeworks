#! /bin/bash

# De adaugat exit codes si validari

# Scrieți un script care verifica dacă un site este available (status code între 200 si 399). 
# Scriptul verifică de un număr maxim de ori primit tot ca argument.	
# Hint: Comanda pentru a citi doar status code-ul este:
# curl -o /dev/null -s -w "%{http_code}\n" https://example.com

args=("$@")

site=${args[0]}
nr_interograri=${args[1]}

echo "Site-ul $site va fi interogat de maxim $nr_interograri ori."

for (( i=0; i<$nr_interograri; i++ )); do
    interogare=$(curl -o /dev/null -s -w "%{http_code}\n" $site)
    if [[ $"interogare" -le 399 && $"interogare" -ge 200 ]]; then
        echo "Site-ul este available!"
        exit 0
        break
    fi
done

echo "Site-ul nu este disponibil momentan!"
exit 1