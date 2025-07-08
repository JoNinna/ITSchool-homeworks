import requests
import urllib3

# Dezactiveaza warning-urile SSL pentru eroarea:
# Eroare pentru url-ul: https://httpstat.us/303, anume HTTPSConnectionPool(host='httpstat.us', port=443): Max retries exceeded with url: /303 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1029)')))
# Acest fix nu a functionat si codul nu returneaza status_code pentru site-urile cu eroare SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#1. Pentru acest exercițiu trebuie creat un fisier pe disk cu numele urls.txt ce conține pe fiecare linie cate o adresa url
urls = [
        "https://www.juniors.ro/jobs",
        "https://itschool.ro/cursuri/curs-web-development-online?gad_source=1&gad_campaignid=22665974053&gclid=EAIaIQobChMI3uGfpc6tjgMV9mWRBR2mqABxEAAYASAAEgInF_D_BwE",
        "https://httpstat.us/201",
        "https://httpstat.us/400",
        "https://httpstat.us/500",
        "https://httpstat.us/404",
        "https://httpstat.us/201",
        "https://httpstat.us/503",
        "https://httpstat.us/200",
        "https://httpstat.us/303"
        ]

try:
    with open("urls.txt","x") as file:
        for url in urls:    
            file.write(url + "\n")
except FileExistsError:
    print("Fisierul urls.txt exista pe disc!")

#2. Citește linie cu line conținutul fișierului urls.txt
with open("urls.txt", "r") as file:
    for line in file:
        #3. Folosește libraria requests pentru a face un call http catre fiecare url
        url = line.strip()
        try:
            url_call = requests.get(url, verify=False)
            print(f"{url} are un status cod de {url_call.status_code}")

            #4. Daca url-ul a intors un status de success (intre 200 si 299) adauga url-ul intr-un fisier cu numele success.txt
            if 200 <= url_call.status_code <= 299:
                with open("success.txt", "a") as file_success:
                    file_success.write(url + "\n")
            #5. Daca url-ul a intors un status de eroare (orice status intre 300 si 599) adauga url-ul intr-un fisier cu numele errors.txt
            elif 300 <= url_call.status_code <= 599:
                with open("errors.txt", "a") as file_error:
                    file_error.write(url + "\n")
            else:
                print("Status cod neobisnuit!")

        except requests.exceptions.RequestException as e:
            print(f"Eroare pentru url-ul: {url}, anume {e}")
        
        