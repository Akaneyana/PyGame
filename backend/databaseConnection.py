import mysql.connector
from mysql.connector import Error
import hashlib
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def get_connection():
    """
    Establish a connection to the database using parameters from the .env file.
    Returns:
        A MySQL database connection object.
    """
    try:
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_DATABASE")
        
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",  # Ensure MariaDB-compatible character set
            collation="utf8mb4_general_ci"  # Use a compatible collation
        )
    except Error as err:
        print(f"Error connecting to the database: {err}")
        raise

def verify_user_credentials(email, password):
    """
    Verify the user's credentials against the database.
    
    Args:
        email (str): The user's email.
        password (str): The user's plain-text password.
    
    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    try:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = get_connection()
        cursor = db.cursor()

        query = "SELECT Password_hash FROM Users WHERE Email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if not result:
            return False

        return result[0] == hashed_password

    except Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

def register_user(name, password, email, phone):
    """
    Register a new user by inserting the provided details into the database.
    
    Args:
        name (str): The user's name.
        password (str): The user's plain text password.
        email (str): The user's email address.
        phone (str): The user's phone number.
    """
    try:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = get_connection()
        cursor = db.cursor()

        query = """
            INSERT INTO Users (Name, Password_hash, Email, Phone)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, hashed_password, email, phone))
        db.commit()

        print("User registered successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

def save_reaction_time(user_id, reaction_time):
    """
    Save a reaction time score into the database.
    
    Args:
        user_id (int): The ID of the user.
        reaction_time (float): The reaction time score in milliseconds.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        query = """
            INSERT INTO ReactionTime (User_Id, Reaction_Time_ms)
            VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, reaction_time))
        db.commit()
        print("Reaction time saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

def save_wpm_score(user_id, words_per_minute):
    """
    Save a typing speed score into the database.

    Args:
        user_id (int): The ID of the user.
        words_per_minute (float): The user's WPM score.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        query = """
            INSERT INTO TypingGame (User_Id, Words_Per_Minute)
            VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, words_per_minute))
        db.commit()
        print("WPM score saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
