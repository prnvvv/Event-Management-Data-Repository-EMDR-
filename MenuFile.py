from Triggers import CreateTriggers
from EventsClass import Event 
from AttendeesClass import Attendees
from RegistrationClass import Registration

print()
print("Welcome to Event Database Management System")
print()

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main menu loop
while True:
    print("MENU FOR ACCESSING:")
    print("1. Events")
    print("2. Attendees")
    print("3. Registrations")
    print("4. Exit")
    print()

    # Get user choice for main menu with validation
    options = get_integer_input("Enter your desired option: ")
    print()

    # Event management options
    if options == 1:
        print("EVENTS")
        print()
        print("MENU")
        print("1. To create an Events Table (if doesn't exist)")
        print("2. To add an Event")
        print("3. To modify an Event")
        print("4. To delete an event")
        print("5. To print the details of the Event/Events")
        print("6. Back to main menu")
        print()

        # Get user choice for event operations with validation
        eventOption = get_integer_input("Enter your desired option: ")
        print()

        event = Event()

        if eventOption == 1:
            # Create events table
            event.CreateTable()
        elif eventOption == 2:
            # Add new events
            nEvents = get_integer_input("Enter the number of events you want to add: ")
            for i in range(nEvents):
                eventName = input("Enter the Event Name: ")
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                eventLocation = input("Enter the Event Location: ")
                event.AddValues(eventName, eventDate, eventLocation)
        elif eventOption == 3:
            # Modify event details
            print("MODIFY MENU")
            print()
            print("1. To update Event Name")
            print("2. To update Event Date")
            print("3. To update Event Location")
            print("4. Back to Events Menu")
            print()

            modifyEventOption = get_integer_input("Enter the desired option: ")
            print()

            if modifyEventOption == 1:
                # Update event name
                eventName = input("Enter the current Event Name: ")
                event.ModifyValues(1, eventName)
            elif modifyEventOption == 2:
                # Update event date
                eventDate = input("Enter the current Event Date (YYYY-MM-DD): ")
                event.ModifyValues(2, eventDate)
            elif modifyEventOption == 3:
                # Update event location
                eventLocation = input("Enter the current Event Location: ")
                event.ModifyValues(3, eventLocation)
        
        elif eventOption == 4:
            # Delete an event
            deleteOption = get_integer_input("Enter the option to delete by:\n1. Event Name\n2. Event Date\n3. Location\n")
            if deleteOption == 1:
                eventName = input("Enter the Event Name: ")
                event.DeleteValues(1, eventName)
            elif deleteOption == 2:
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                event.DeleteValues(2, eventDate)
            elif deleteOption == 3:
                eventLocation = input("Enter the Event Location: ")
                event.DeleteValues(3, eventLocation)
        elif eventOption == 5:
            # Print event details
            print("PRINT DATA MENU")
            print()
            print("1. Print all events")
            print("2. Print event by name")
            print("3. Print events by date")
            print("4. Print events by location")
            print("5. Back to Events Menu")
            print()

            printOption = get_integer_input("Enter your desired option: ")
            print()

            if printOption == 1:
                # Print all events
                event.PrintData(1)
            elif printOption == 2:
                # Print event by name
                eventName = input("Enter the Event Name: ")
                event.PrintData(2, eventName)
            elif printOption == 3:
                # Print events by date
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                event.PrintData(3, eventDate)
            elif printOption == 4:
                # Print events by location
                eventLocation = input("Enter the Event Location: ")
                event.PrintData(4, eventLocation)

        elif eventOption == 6:
            # Go back to main menu
            continue

    # Attendee management options
    elif options == 2:
        print("ATTENDEES")
        print()
        print("MENU")
        print("1. To create an Attendees Table (if doesn't exist)")
        print("2. To add an Attendee")
        print("3. To modify an Attendee")
        print("4. To delete an Attendee")
        print("5. To print the details of the Attendee/Attendees")
        print("6. Back to main menu")
        print()

        # Get user choice for attendee operations with validation
        attendeeOption = get_integer_input("Enter your desired option: ")
        print()

        attendee = Attendees()

        if attendeeOption == 1:
            # Create attendees table
            attendee.CreateTable()
        elif attendeeOption == 2:
            # Add new attendees
            nAttendees = get_integer_input("Enter the number of attendees you want to add: ")
            for i in range(nAttendees):
                attendeeName = input("Enter the Attendee Name: ")
                attendeeEmail = input("Enter the Attendee Email: ")
                attendee.AddValues(attendeeName, attendeeEmail)
        elif attendeeOption == 3:
            # Modify attendee details
            attendeeID = get_integer_input("Enter the Attendee ID to modify: ")
            attendeeName = input("Enter the new Attendee Name: ")
            attendeeEmail = input("Enter the new Attendee Email: ")
            attendee.ModifyValues(attendeeID, attendeeName, attendeeEmail)
        elif attendeeOption == 4:
            # Delete an attendee
            attendeeID = get_integer_input("Enter the Attendee ID to delete: ")
            attendee.DeleteValues(attendeeID)
        elif attendeeOption == 5:
            # Print attendee details
            attendee.PrintData()

        elif attendeeOption == 6:
            # Go back to main menu
            continue

    # Registration management options
    elif options == 3:
        print("REGISTRATIONS")
        print()
        print("MENU")
        print("1. To create a Registrations Table (if doesn't exist)")
        print("2. To add a Registration")
        print("3. To modify a Registration")
        print("4. To delete a Registration")
        print("5. To print the details of the Registration/Registrations")
        print("6. Back to main menu")
        print()

        # Get user choice for registration operations with validation
        registrationOption = get_integer_input("Enter your desired option: ")
        print()

        registration = Registration()

        if registrationOption == 1:
            # Create registrations table
            registration.CreateTable()
        elif registrationOption == 2:
            # Add new registration
            eventID = get_integer_input("Enter the Event ID for Registration: ")
            attendeeID = get_integer_input("Enter the Attendee ID for Registration: ")
            registration.AddValues(eventID, attendeeID)
        elif registrationOption == 3:
            # Modify registration details
            registrationID = get_integer_input("Enter the Registration ID to modify: ")
            eventID = get_integer_input("Enter the new Event ID for Registration: ")
            attendeeID = get_integer_input("Enter the new Attendee ID for Registration: ")
            registration.ModifyValues(registrationID, eventID, attendeeID)
        elif registrationOption == 4:
            # Delete a registration
            registrationID = get_integer_input("Enter the Registration ID to delete: ")
            registration.DeleteValues(registrationID)
        elif registrationOption == 5:
            # Print registration details
            registration.PrintData()

        elif registrationOption == 6:
            # Go back to main menu
            continue

    # Exit the program
    elif options == 4:
        print("Exiting Event Database Management System. Goodbye!")
        break

    else:
        # Handle invalid main menu options
        print("Invalid option. Please choose a valid option from the menu.")
