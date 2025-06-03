import mysql.connector
from mysql.connector import Error
import hashlib
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_connection():
    """
    Establish a connection to the database using parameters from the .env file.
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
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )
    except Error as err:
        print(f"Error connecting to the database: {err}")
        raise

def verify_user_credentials(email, password):
    """
    Verify the user's credentials and return the user ID if successful.
    """
    try:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = get_connection()
        cursor = db.cursor()

        query = "SELECT User_Id FROM Users WHERE Email = %s AND Password_hash = %s"
        cursor.execute(query, (email, hashed_password))
        result = cursor.fetchone()

        if result:
            user_id = result[0]
            update_last_logged_in(user_id)
            return user_id
        return None

    except Error as err:
        print(f"Error: {err}")
        return None
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

def update_last_logged_in(user_id):
    """
    Update the Users table to store the last logged-in user's timestamp.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        query = """
            UPDATE Users 
            SET Last_Logged_In = NOW()
            WHERE User_Id = %s
        """
        cursor.execute(query, (user_id,))
        db.commit()
        print(f"User {user_id} marked as last logged in.")

    except Error as err:
        print(f"Error updating last logged-in user: {err}")
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

def save_wpm_score(user_id, final_wpm):
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
        cursor.execute(query, (user_id, final_wpm))
        db.commit()
        print("WPM score saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
