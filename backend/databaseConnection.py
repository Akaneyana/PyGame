import mysql.connector
from mysql.connector import Error  # Import the Error class for better error handling
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
        # Retrieve database connection parameters
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_DATABASE")

        # Establish and return the database connection
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except Error as err:
        print(f"Error connecting to the database: {err}")
        raise  # Re-raise the exception for debugging or logging purposes

def save_reaction_time(user_id, reaction_time):
    """
    Save a reaction time score into the database.
    Args:
        user_id (int): The ID of the user (if applicable).
        reaction_time (float): The reaction time score in milliseconds.
    """
    try:
        # Establish the database connection
        db = get_connection()
        cursor = db.cursor()

        # Insert the reaction time score into the ReactionTime table
        query = """
            INSERT INTO ReactionTime (User_id, Reaction_Time_ms)
            VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, reaction_time))

        # Commit the transaction
        db.commit()

        print("Reaction time score saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure the cursor and connection are closed even if an error occurs
        if cursor:
            cursor.close()
        if db:
            db.close()
