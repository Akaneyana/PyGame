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
            database=database
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
        # Hash the provided password
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Establish the database connection
        db = get_connection()
        cursor = db.cursor()

        # Query to fetch the user's data based on the email
        query = "SELECT Password_hash FROM Users WHERE Email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # If no result is found, the email doesn't exist
        if not result:
            return False

        # Check if the hashed password matches the one in the database
        stored_password_hash = result[0]
        if stored_password_hash == hashed_password:
            return True
        else:
            return False

    except Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def register_user(name, password, email, phone):
    """
    Register a new user by inserting the provided details into the database.
    The password will be hashed before saving to the database.
    
    Args:
        name (str): The user's name.
        password (str): The user's plain text password.
        email (str): The user's email address.
        phone (str): The user's phone number.
    """
    try:
        # Hash the password
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Establish the database connection
        db = get_connection()
        cursor = db.cursor()

        # Insert the user data into the Users table
        query = """
            INSERT INTO Users (Name, Password_hash, Email, Phone)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, hashed_password, email, phone))

        # Commit the transaction
        db.commit()

        print("User registered successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def save_reaction_time(user_id, reaction_time):
    """
    Save a reaction time score into the database.
    Args:
        user_id (int): The ID of the user (if applicable).
        reaction_time (float): The reaction time score in milliseconds.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        # Insert the reaction time into the ReactionTime table
        query = """
            INSERT INTO ReactionTime (User_id, Reaction_Time_ms)
            VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, reaction_time))

        db.commit()
        print("Reaction time saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
