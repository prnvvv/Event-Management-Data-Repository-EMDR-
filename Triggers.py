from mysqlConnector import Cursor  # Import the custom Cursor function
from mysql.connector import Error  # Import the Error class from mysql.connector
import numpy as np  # Import numpy for numerical operations if needed
import pandas as pd  # Import pandas for data manipulation if needed

# Get the connection and cursor object from the Cursor function
conn, cursor = Cursor()

def CreateTriggers():
    """
    Function to create triggers for event and attendee modifications in the database.
    Ensures referential integrity by cascading updates and deletes to the Registration table.
    """
    try:
        # Trigger to delete related registrations before deleting an event
        create_event_trigger = """
        CREATE TRIGGER before_event_delete
        BEFORE DELETE ON Event
        FOR EACH ROW
        BEGIN
            DELETE FROM Registration WHERE EventID = OLD.EventID;
        END
        """
        cursor.execute(create_event_trigger)
        conn.commit()

        # Trigger to delete related registrations before deleting an attendee
        create_attendee_trigger = """
        CREATE TRIGGER before_attendee_delete
        BEFORE DELETE ON Attendees
        FOR EACH ROW
        BEGIN
            DELETE FROM Registration WHERE AttendeeID = OLD.AttendeeID;
        END
        """
        cursor.execute(create_attendee_trigger)
        conn.commit()

        # Trigger to update related registrations before updating an event
        create_event_update_trigger = """
        CREATE TRIGGER before_event_update
        BEFORE UPDATE ON Event
        FOR EACH ROW
        BEGIN
            UPDATE Registration SET EventName = NEW.EventName WHERE EventID = OLD.EventID;
        END
        """
        cursor.execute(create_event_update_trigger)
        conn.commit()

        # Trigger to update related registrations before updating an attendee
        create_attendee_update_trigger = """
        CREATE TRIGGER before_attendee_update
        BEFORE UPDATE ON Attendees
        FOR EACH ROW
        BEGIN
            UPDATE Registration SET AttendeeName = NEW.AttendeeName WHERE AttendeeID = OLD.AttendeeID;
        END
        """
        cursor.execute(create_attendee_update_trigger)
        conn.commit()

    except Error as e:
        # Handle any errors that occur during the trigger creation process
        print(f"Error creating triggers: {e}")

# Call the function to create triggers
CreateTriggers()

# Close the cursor and connection to free resources
cursor.close()
conn.close()
