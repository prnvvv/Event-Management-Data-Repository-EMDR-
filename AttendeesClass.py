from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

class Attendees:

    def __init__(self, attendeeName, email):
        self.attendeeName = attendeeName
        self.email = email

    def CreateTable(self):
        try:
            attendeeTable = """
            CREATE TABLE IF NOT EXISTS Attendees(
            AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
            AttendeeName VARCHAR(255) NOT NULL,
            AttendeeEmail VARCHAR(255) NOT NULL)"""
            cursor.execute(attendeeTable)
            conn.commit()
        except Error as e:
            print(f"Error creating Attendees table: {e}")

    def AddValues(self):
        try:
            insertData = """
            INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
            """
            data = (self.attendeeName, self.email)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding Attendees values: {e}")

    def ModifyValues(self, option):
        try:
            if option == 1:
                nattendeeName = input("Enter the new Attendee Name : ")
                modifyData = "UPDATE Attendees SET AttendeeName = %s WHERE AttendeeName = %s"
                cursor.execute(modifyData, (nattendeeName, self.attendeeName))
                self.attendeeName = nattendeeName
                conn.commit()
            elif option == 2:
                nattendeeEmail = input("Enter the new Attendee Email : ")
                modifyData = "UPDATE Attendees SET AttendeeEmail = %s WHERE AttendeeEmail = %s"
                cursor.execute(modifyData, (nattendeeEmail, self.email))
                self.email = nattendeeEmail
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Attendees: {e}")

    def DeleteValues(self, option):
        try:
            if option == 1:
                dattendeeName = input("Enter the Attendee Name : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(deleteData, (dattendeeName,))
                conn.commit()
            elif option == 2:
                demail = input("Enter the Attendee Email : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(deleteData, (demail,))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error deleting Attendees: {e}")

    def PrintData(self, option):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Attendees")
                rows = cursor.fetchall()

                tableArray = np.array(rows)
                print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
            if option == 2:
                attendeeName = input("Enter the Attendee Name: ")
                query = "SELECT * FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(query, (attendeeName,))
                attendee = cursor.fetchone()

                if attendee:
                    tableArray = np.array([attendee])
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendee found with name '{attendeeName}'")
            if option == 3:
                attendeeEmail = input("Enter the Attendee Email: ")
                query = "SELECT * FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(query, (attendeeEmail,))
                attendees = cursor.fetchall()

                if attendees:
                    tableArray = np.array(attendees)
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendees found with email '{attendeeEmail}'")
        except Error as e:
            print(f"Error while printing data: {e}")
