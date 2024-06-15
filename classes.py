import mysql.connector

# Establish MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="eventDBMS"
)

cursor = conn.cursor()

# Define Event class
class Event:

    def __init__(self, eventName, date, location):
        self.eventName = eventName
        self.date = date
        self.location = location

    def CreateTable(self):
        eventTable = """
        CREATE TABLE IF NOT EXISTS Event(
        EventID INT AUTO_INCREMENT PRIMARY KEY,
        EventName VARCHAR(255) NOT NULL,
        Date DATE NOT NULL,
        Location VARCHAR(255) NOT NULL)"""
        cursor.execute(eventTable)
        conn.commit()

    def AddValues(self):
        insertData = """
        INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
        """
        data = (self.eventName, self.date, self.location)
        cursor.execute(insertData, data)
        conn.commit()

    def ModifyValues(self, option):
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

    def DeleteValues(self, option):
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


# Define Attendees class
class Attendees:

    def __init__(self, attendeeName, email):
        self.attendeeName = attendeeName
        self.email = email

    def CreateTable(self):
        attendeeTable = """
        CREATE TABLE IF NOT EXISTS Attendees(
        AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
        AttendeeName VARCHAR(255) NOT NULL,
        AttendeeEmail VARCHAR(255) NOT NULL)"""
        cursor.execute(attendeeTable)
        conn.commit()

    def AddValues(self):
        insertData = """
        INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
        """
        data = (self.attendeeName, self.email)
        cursor.execute(insertData, data)
        conn.commit()

    def ModifyValues(self, option):
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

    def DeleteValues(self, option):
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


# Define Registration class
class Registration:

    def CreateTable(self):
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

    def AddRegistration(self, eventID, attendeeID, eventName, attendeeName):
        insertData = """
        INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%s, %s, %s, %s)
        """
        data = (eventID, attendeeID, eventName, attendeeName)
        cursor.execute(insertData, data)
        conn.commit()


event = Event("Conference", "2023-06-01", "New York")
event.CreateTable()
event.AddValues()

attendee = Attendees("John Doe", "john.doe@example.com")
attendee.CreateTable()
attendee.AddValues()

registration = Registration()
registration.CreateTable()

cursor.execute("SELECT EventID FROM Event WHERE EventName = %s", ("Conference",))
eventID = cursor.fetchone()[0]

cursor.execute("SELECT AttendeeID FROM Attendees WHERE AttendeeName = %s", ("John Doe",))
attendeeID = cursor.fetchone()[0]

registration.AddRegistration(eventID, attendeeID, "Conference", "John Doe")

event.DeleteValues(1)  # Delete by Event Name

attendee.DeleteValues(1)  # Delete by Attendee Name

cursor.close()
conn.close()
