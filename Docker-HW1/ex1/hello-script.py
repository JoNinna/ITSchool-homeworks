# Scriptul are ca scop crearea, afisarea statusului sau stergerea unui container in functie de optiuni
import subprocess

print("Meniul este:\nOptiune 1- Rulaza imaginea hello-world intr-un container\nOptiune 2 - Verifica daca containerul hello-world ruleaza\nOptiune 3 - Sterge imaginea hello-world")

optiune = int(input("Introduceti o optiune: "))

if optiune == 1:
    subprocess.run(["docker", "run", "--name", "hello-workd", "hello-world"])
    subprocess.run(["docker", "logs", "hello-workd"])
elif optiune == 2:
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    if "hello-workd" in result.stdout:
        print("Containerul hello-world ruleaza!")
    else:
        print("Containerul nu ruleaza!")
elif optiune == 3:
    subprocess.run(["docker","stop", "hello-workd"])
    subprocess.run(["docker", "rm", "hello-workd"])
else: 
    exit()

