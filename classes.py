import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prnv2005",
    database="eventDBMS"
)

cursor = conn.cursor()

def createTriggers():
    trigger_event_update = """
    DELIMITER //

    CREATE TRIGGER after_event_update
    AFTER UPDATE ON Event
    FOR EACH ROW
    BEGIN
        UPDATE Registration
        SET EventName = NEW.EventName
        WHERE EventID = OLD.EventID;
    END//

    DELIMITER ;
    """

    trigger_attendees_update = """
    DELIMITER //

    CREATE TRIGGER after_attendees_update
    AFTER UPDATE ON Attendees
    FOR EACH ROW
    BEGIN
        UPDATE Registration
        SET AttendeeName = NEW.AttendeeName
        WHERE AttendeeID = OLD.AttendeeID;
    END//

    DELIMITER ;
    """
    # Execute the trigger creation statements
    cursor.execute(trigger_event_update)
    cursor.execute(trigger_attendees_update)
    conn.commit()

class Event:

    def __init__(self, eventName, date, location):
        self.eventName = eventName
        self.date = date
        self.location = location
        self.data = [(self.eventName, self.date, self.location)]

    def createTable(self):
        eventTable = """
        CREATE TABLE IF NOT EXISTS Event(
        EventID INT AUTO_INCREMENT PRIMARY KEY,
        EventName VARCHAR(255) NOT NULL,
        Date DATE NOT NULL,
        Location VARCHAR(255) NOT NULL)"""
        cursor.execute(eventTable)
        conn.commit()

    def addValues(self):
        insertData = """
        INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
        """
        for data in self.data:
            cursor.execute(insertData, data)
        conn.commit()

    def ModifyValues(self, option):
        if option == 1:
            neventName = input("Enter the new Event Name : ")
            modifyData = f"UPDATE Event SET EventName = %s WHERE EventName = %s"
            cursor.execute(modifyData, (neventName, self.eventName))
            self.eventName = neventName
            conn.commit()
        elif option == 2:
            neventDate = input("Enter the new Event Date (YYYY-MM-DD) : ")
            modifyData = f"UPDATE Event SET Date = %s WHERE Date = %s"
            cursor.execute(modifyData, (neventDate, self.date))
            self.date = neventDate
            conn.commit()            
        elif option == 3:
            nLocation = input("Enter the new Event Location : ")
            modifyData = f"UPDATE Event SET Location = %s WHERE Location = %s"
            cursor.execute(modifyData, (nLocation, self.location))
            self.location = nLocation
            conn.commit()
        else:
            print("Invalid Option")

class Attendees:

    def __init__(self, attendeeName, email):
        self.attendeeName = attendeeName
        self.email = email
        self.data = [(self.attendeeName, self.email)]

    def createTable(self):
        attendeeTable = """
        CREATE TABLE IF NOT EXISTS Attendees(
        AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
        AttendeeName VARCHAR(255) NOT NULL,
        AttendeeEmail VARCHAR(255) NOT NULL)"""
        cursor.execute(attendeeTable)
        conn.commit()

    def addValues(self):
        insertData = """
        INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
        """
        for data in self.data:
            cursor.execute(insertData, data)
        conn.commit()

    def ModifyValues(self, option):
        if option == 1:
            nattendeeName = input("Enter the new Event Name : ")
            modifyData = f"UPDATE Attendees SET AttendeeName = %s WHERE AttendeeName = %s"
            cursor.execute(modifyData, (nattendeeName, self.attendeeName))
            self.attendeeName = nattendeeName
            conn.commit()
        elif option == 2:
            nattendeeEmail = input("Enter the new Attendee Email : ")
            modifyData = f"UPDATE Attendees SET AttendeeEmail = %s WHERE AttendeeEmail = %s"
            cursor.execute(modifyData, (nattendeeEmail, self.email))
            self.email = nattendeeEmail
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
        Event.addValues(self)
        Attendees.addValues(self)

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
