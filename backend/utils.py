import os

def check_if_db_available():
    """
    Check if the database is available.
    """
    if os.path.exists("database.db"):
        return True
    return False