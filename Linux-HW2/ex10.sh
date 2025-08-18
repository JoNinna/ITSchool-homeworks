#! /bin/bash

# Adaugati in variabila de mediu PATH directorul cu calea ~/bin-itschools/ doar dacă acesta exista. 
# Faceți acest lucru în mod automat de fiecare data cand se porneste o sesiune cu login pentru userul curent. 
# Adaugati un script în acel director și încercați să-l executați de oriunde.

# Scriptul este adaugat direct in ~/.bashrc, si verifica ca bin-itschools exista
to_run='
if [ -d "$HOME/bin-itschools" ]; then
    export PATH="$PATH:$HOME/bin-itschools";
fi
'

echo $to_run >> "$HOME/.bashrc"
echo "[OK] calea ~/bin-itschools/ a fost adaugata cu succes in PATH"
