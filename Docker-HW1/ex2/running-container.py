# Scriptul are ca scop afisarea proceselor din containerul creat
import subprocess

running_time = input("Introduceti cat timp doriti ca containerul sa fie up: ")

subprocess.run(["docker", "run", "-d", "--rm", "--name", "busy", "busybox", "sleep", running_time])
procese_container = subprocess.check_output(["docker", "exec", "busy", "ps"], text=True)

print(f"Procesele din container sunt: {procese_container}")
