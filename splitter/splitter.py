from utils import helpers, dbloader, data_dir, db_path
import logging
from pathlib import Path
from models.classes import Group, Participant

logging.basicConfig(
level=logging.DEBUG,  # Capture all levels of logs
format='%(asctime)s - %(levelname)s - %(message)s',  # Log format with timestamp
handlers=[
    logging.FileHandler("logfile.log"),  # Log to a file
    logging.StreamHandler()              # Log to console
    ]
)
if __name__ == "__main__":
    part1 = Participant("john", "had")