# Faceți un script de python ce verifica dacă nivelul de ocupare al discului este mai mare de un prag (configurable printr-o variabila de mediu - implicit 90%). 
# În cazul în care ocuparea discului este mai mare de acest prag printeaza un mesaj de alertă în consola.
# Puneti acest script sa ruleze in ~/.bashrc

import os
import psutil

os.environ["PRAG_CPU"] = "90"
prag_cpu = os.getenv("PRAG_CPU")

disk_cpu = psutil.disk_usage("/")
disk_cpu_total = disk_cpu.total
disk_cpu_total_gb = disk_cpu_total/(1024**3)
 
if disk_cpu_total_gb >= int(prag_cpu):
    print(f"Atentie! Disk-ul depaseste pragul de ocupare de {prag_cpu}%, fiind la {disk_cpu_total_gb:.2f} GB din memorie!")

