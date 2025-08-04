import os
import logging

logs_folder = os.mkdir("logs", exist_ok=True)
path_to_folder = "logs/dapp.log"

# Log to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(path_to_folder),
        logging.StreamHandler()
    ]
)

logging.debug("Debug info")
logging.info("General info")
logging.warning("Something might be wrong")
logging.error("An error happened")
