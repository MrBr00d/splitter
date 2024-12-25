import sqlite3
from utils import db_path, data_dir
import logging

logger = logging.getLogger(__name__)

def list_groups(filepath=db_path) -> dict:
    '''Loads in the groups and returns a dictionary with keys group_name and values group_id.'''
    try:
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM groups;")
        rows = cursor.fetchall()
        conn.close()
        logger.info("Group listing OK.")
    except sqlite3.Error as e:
        logger.error(f"SQLite error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
    
    group_dict = {}
    for row in rows:
        group_dict[row[1]] = row[0]
    return group_dict

def load_group(group_id:int, filepath=db_path):
    '''Return al the value needed to create a group class.
    Checks first if group exists, if the group does not exist it will be created.'''
    try:
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("SELECT group_name FROM groups WHERE group_id=?;", (group_id,))
        group_data = cursor.fetchone()

        cursor.execute("SELECT participant_name, balance FROM participants WHERE group_id = ?", (group_id,))
        participant_data = cursor.fetchall()
    
        conn.close()
        logger.info("Group loading OK.")
    except sqlite3.Error as e:
        logger.error(f"SQLite error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
    return group_data, participant_data

def create_group(group_name:str, filepath=db_path):
    try:
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO groups (group_name) VALUES (?);", (group_name,))
        conn.commit()
        conn.close()
        logger.info(f"Creation group {group_name} OK")
    except sqlite3.Error as e:
        logger.error(f"SQLite error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")

def delete_group(group_name:str, filepath=db_path):
    respose = input(f"Are you sure you want to remove {group_name} [Y/n]")
    if respose == "Y" or respose == "y":
        try:
            conn = sqlite3.connect(filepath)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM groups WHERE group_name = ?;", (group_name,))
            conn.commit()
            conn.close()
            logger.info(f"Delete group {group_name} OK")
        except sqlite3.Error as e:
            logger.error(f"SQLite error occurred: {e}")
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")

def load_participants(group_id:int, filepath=db_path) -> list:
    '''Loads all participants from the database. This function requires the group id which should be either displayed in the CLI
    or in a GUI should be selected by clicking on a group name. The following list will contain only the name of each participant. Names should be unique.'''
    try:
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("SELECT participant_name FROM participants WHERE group_id = ?", (group_id,))
        rows = cursor.fetchall()
        conn.close()
        logger.info(f"Participant loading for group {group_id} OK")
    except sqlite3.Error as e:
        logger.error(f"SQLite error occured: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occured: {e}")
    return rows
