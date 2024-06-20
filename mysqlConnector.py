import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prnv2005",
        database="eventDBMS"
    )

    cursor = conn.cursor()

except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)