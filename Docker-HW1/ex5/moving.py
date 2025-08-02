import os
import shutil
from time import sleep

input = os.path.join(os.getcwd(),'input')  
output = os.path.join(os.getcwd(),'output')  

for fisier in os.listdir(input):
    input_path = os.path.join(input, fisier)

    try:
        shutil.move(input_path,output)
    except FileNotFoundError:
        continue

    sleep(5)
