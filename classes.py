import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prnv2005",
    database="eventDBMS"
)

cursor = conn.cursor()

def createTriggers():
    trigger_eventUpdate_p1 = """
    CREATE TRIGGER IF NOT EXISTS after_eventUpdate
    AFTER UPDATE ON Event
    FOR EACH ROW
    BEGIN
        UPDATE Registration
        SET EventName = NEW.EventName
        WHERE EventID = OLD.EventID;
    END;"""

    trigger_attendeesUpdate_p1 = """
    CREATE TRIGGER IF NOT EXISTS after_attendeesUpdate
    AFTER UPDATE ON Attendees
    FOR EACH ROW
    BEGIN
        UPDATE Registration
        SET AttendeeName = NEW.AttendeeName
        WHERE AttendeeID = OLD.AttendeeID;
    END;"""

    cursor.execute(trigger_eventUpdate_p1)
    cursor.execute(trigger_attendeesUpdate_p1)
    conn.commit()


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

            deleteRegData = "DELETE FROM Registration WHERE EventName = %s"
            cursor.execute(deleteRegData, (deventName,))
            conn.commit()
    
        elif option == 2:
            deventDate = input("Enter the Event Date (YYYY-MM-DD) : ")
            deleteData = "DELETE FROM Event WHERE Date = %s"
            cursor.execute(deleteData, (deventDate,))
            conn.commit()

            deleteRegData = "DELETE FROM Registration WHERE EventName = %s"
            cursor.execute(deleteRegData, (deventName,))
            conn.commit()

        elif option == 3:
            dLocation = input("Enter the Event Location : ")
            deleteData = "DELETE FROM Event WHERE Location = %s"
            cursor.execute(deleteData, (dLocation,))
            conn.commit()

            deleteRegData = "DELETE FROM Registration WHERE EventName = %s"
            cursor.execute(deleteRegData, (deventName,))
            conn.commit()

        else:
            print("Invalid Option")


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

            deleteRegData = "DELETE FROM Registration WHERE AttendeeName = %s"
            cursor.execute(deleteRegData, (dattendeeName))
            conn.commit()

        elif option == 2:
            demail = input("Enter the Attendee Email : ")
            deleteData = "DELETE FROM Attendees WHERE AttendeeEmail = %s"
            cursor.execute(deleteData, (demail,))
            conn.commit()
        else:
            print("Invalid Option")


class Registration(Event, Attendees):

    def __init__(self, eventName, date, location, attendeeName, email):
        Event.__init__(self, eventName, date, location)
        Attendees.__init__(self, attendeeName, email)

    def CreateTable(self):
        registrationTable = """
        CREATE TABLE IF NOT EXISTS Registration(
        RegistrationID INT AUTO_INCREMENT PRIMARY KEY,
        EventID INT,
        AttendeeID INT,
        EventName VARCHAR(255),
        AttendeeName VARCHAR(255),
        FOREIGN KEY (EventID) REFERENCES Event(EventID),
        FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID))"""
        cursor.execute(registrationTable)
        conn.commit()

    def AddValues(self):
        Event.AddValues(self)
        Attendees.AddValues(self)

        cursor.execute("SELECT EventID FROM Event WHERE EventName = %s AND Date = %s AND Location = %s",
                       (self.eventName, self.date, self.location))
        EventID = cursor.fetchone()[0]

        cursor.execute("SELECT AttendeeID FROM Attendees WHERE AttendeeName = %s AND AttendeeEmail = %s",
                       (self.attendeeName, self.email))
        AttendeeID = cursor.fetchone()[0]

        insertData = """
        INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insertData, (EventID, AttendeeID, self.eventName, self.attendeeName))
        conn.commit()


# Uncomment to test functionality
'''
event = Event("Conference", "2023-06-01", "New York")
attendee = Attendees("John Doe", "john.doe@example.com")
registration = Registration("Conference", "2023-06-01", "New York", "John Doe", "john.doe@example.com")

event.CreateTable()
attendee.CreateTable()
registration.CreateTable()
createTriggers()

event.AddValues()
attendee.AddValues()
registration.AddValues()
'''
