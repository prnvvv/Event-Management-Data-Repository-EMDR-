import mysql.connector
from mysql.connector import Error

def Cursor():
    try:
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",       # The hostname of the database server
            user="root",            # The username to access the database
            password="your_password",    # The password to access the database
            database="your_database_name"    # The name of the database to connect to
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Return both the connection and cursor object
        return conn, cursor
    
    except Error as e:
        # Handle any errors that occur during the connection process
        print(f"Error connecting to MySQL: {e}")
        exit(1)  # Exit the program if the connection fails
