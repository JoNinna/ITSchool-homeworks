import os
import time
import logging

os.makedirs("/log", exist_ok=True)

# Log to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/log/app.log"),
        logging.StreamHandler()
    ]
)

while True:
    logging.info("Log generat automat din container")
    time.sleep(1)

