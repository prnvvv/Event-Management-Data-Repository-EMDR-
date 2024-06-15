import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd

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

class Event:

    def __init__(self, eventName, date, location):
        self.eventName = eventName
        self.date = date
        self.location = location

    def CreateTable(self):
        try:
            eventTable = """
            CREATE TABLE IF NOT EXISTS Event(
            EventID INT AUTO_INCREMENT PRIMARY KEY,
            EventName VARCHAR(255) NOT NULL,
            Date DATE NOT NULL,
            Location VARCHAR(255) NOT NULL)"""
            cursor.execute(eventTable)
            conn.commit()
        except Error as e:
            print(f"Error creating Event table: {e}")

    def AddValues(self):
        try:
            insertData = """
            INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
            """
            data = (self.eventName, self.date, self.location)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding Event values: {e}")

    def ModifyValues(self, option):
        try:
            if option == 1:
                neventName = input("Enter the new Event Name : ")
                modifyData = "UPDATE Event SET EventName = %s WHERE EventName = %s"
                cursor.execute(modifyData, (neventName, self.eventName))
                self.eventName = neventName
                conn.commit()
            elif option == 2:
                neventDate = input("Enter the new Event Date (YYYY-MM-DD) : ")
                modifyData = "UPDATE Event SET Date = %s WHERE Date = %s"
                cursor.execute(modifyData, (neventDate, self.date))
                self.date = neventDate
                conn.commit()
            elif option == 3:
                nLocation = input("Enter the new Event Location : ")
                modifyData = "UPDATE Event SET Location = %s WHERE Location = %s"
                cursor.execute(modifyData, (nLocation, self.location))
                self.location = nLocation
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Event: {e}")

    def DeleteValues(self, option):
        try:
            if option == 1:
                deventName = input("Enter the Event Name : ")
                deleteData = "DELETE FROM Event WHERE EventName = %s"
                cursor.execute(deleteData, (deventName,))
                conn.commit()
            elif option == 2:
                deventDate = input("Enter the Event Date (YYYY-MM-DD) : ")
                deleteData = "DELETE FROM Event WHERE Date = %s"
                cursor.execute(deleteData, (deventDate,))
                conn.commit()
            elif option == 3:
                dLocation = input("Enter the Event Location : ")
                deleteData = "DELETE FROM Event WHERE Location = %s"
                cursor.execute(deleteData, (dLocation,))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error deleting Event: {e}")
    
    def PrintData(self, option):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Event")
                rows = cursor.fetchall()

                tableArray = []
                tableArray = np.array(tableArray)
                for row in rows:
                    tableArray.append(row)
                
                print(pd.DataFrame(tableArray))
            if option == 2:
                eventName = input("Enter the Event Name")
                query = "SELECT * FROM Event WHERE EventName = %s"
                cursor.execute(query, (eventName))

                event = cursor.fetchone()

                if event:
                    print(f"EventID: {event[0]}")
                    print(f"EventName: {event[1]}")
                    print(f"Date: {event[2]}")
                    print(f"Location: {event[3]}")
                else:
                    print(f"No event found with name '{eventName}'")
            if option == 3:
                eventDate = input("Enter the Event Date")
                query = "SELECT * FROM Event WHERE Date = %s"
                cursor.execute(query, (eventDate))

                events = cursor.fetchall()

                for index, event in enumerate(events):
                    if event:
                        print(f"{index}.")
                        print(f"EventID: {event[0]}")
                        print(f"EventName: {event[1]}")
                        print(f"Date: {event[2]}")
                        print(f"Location: {event[3]}")
                    else:
                        print(f"No event found with name '{eventName}'")




                



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


class Registration:

    def CreateTable(self):
        try:
            registrationTable = """
            CREATE TABLE IF NOT EXISTS Registration(
            RegistrationID INT AUTO_INCREMENT PRIMARY KEY,
            EventID INT,
            AttendeeID INT,
            EventName VARCHAR(255),
            AttendeeName VARCHAR(255),
            FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE,
            FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE)"""
            cursor.execute(registrationTable)
            conn.commit()
        except Error as e:
            print(f"Error creating Registration table: {e}")

    def AddRegistration(self, eventID, attendeeID, eventName, attendeeName):
        try:
            insertData = """
            INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%s, %s, %s, %s)
            """
            data = (eventID, attendeeID, eventName, attendeeName)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding registration: {e}")

