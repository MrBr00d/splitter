import sqlite3
from pathlib import Path
import logging
from utils import db_path, data_dir

# Get a logger for this module
logger = logging.getLogger(__name__)

def create_transaction_db(filepath):
    """
    Creates the necessary tables for a transaction database at the specified file location.
    
    Args:
    filepath (str): Path to the SQLite database file.
    """
    logger.info(f"Starting to create the transaction database at {filepath}.")

    try:
        # Connect to the database (this will create the file if it doesn't exist)
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        logger.info(f"Database connected successfully at {filepath}.")

        # Create the groups table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL UNIQUE
        );
        ''')
        logger.info("Groups table created or already exists.")

        # Create the participants table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_name TEXT NOT NULL UNIQUE,
            group_id INTEGER,
            balance NUMERIC DEFAULT 0,
            FOREIGN KEY (group_id) REFERENCES groups(group_id)
        );
        ''')
        logger.info("Participants table created or already exists.")

        # Create the transactions table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            group_id INTEGER NOT NULL,
            FOREIGN KEY (group_id) REFERENCES groups(group_id)
        );
        ''')
        logger.info("Transactions table created or already exists.")

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        logger.info(f"Database tables created successfully at {filepath}.")
    
    except sqlite3.Error as e:
        logger.error(f"SQLite error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")

def make_data(data_folder=data_dir):
    if not data_folder.is_dir():
        data_folder.mkdir(parents=True, exist_ok=False)
        create_transaction_db(data_folder / "transaction.db")
    elif not(data_folder / "transaction.db").exists():
        create_transaction_db(data_folder / "transaction.db")
    else:
        logger.info("Folder and file alreadt exist")
    try:
        conn = sqlite3.connect(data_folder / "transaction.db")
        logger.info("Connection to database succesful")
    except Exception as e:
        logger.error(f"An error eccured while connecting to the database: {e}")
    return conn