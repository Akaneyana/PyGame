import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_connection():
    # Retrieve database connection parameters from environment variables
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    
    # Establish the connection to the MySQL database
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def save_reaction_time(user_id, reaction_time):
    """
    Save a reaction time score into the database.
    :param user_id: The ID of the user (if applicable).
    :param reaction_time: The reaction time score (in milliseconds).
    """
    try:
        # Get database connection
        db = get_connection()
        cursor = db.cursor()

        # Insert reaction time score into the ReactionTime table
        cursor.execute("""
            INSERT INTO ReactionTime (User_id, RT_Score)
            VALUES (%s, %s)
        """, (user_id, reaction_time))

        # Commit the transaction
        db.commit()

        # Close the database connection
        cursor.close()
        db.close()

        print("Reaction time score saved successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
