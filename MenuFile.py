from Triggers import CreateTriggers
from EventsClass import Event 
from AttendeesClass import Attendees
from RegistrationClass import Registration

print()
print("Welcome to Event Database Management System")
print()

while True:
    print("MENU FOR ACCESSING:")
    print("1. Events")
    print("2. Attendees")
    print("3. Registrations")
    print("4. Exit")
    print()

    options = int(input("Enter your desired option: "))
    print()

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

        eventOption = int(input("Enter your desired option: "))
        print()

        event = Event()

        if eventOption == 1:
            event.CreateTable()
        elif eventOption == 2:
            nEvents = int(input("Enter the number of events you want to add: "))
            for i in range(nEvents):
                eventName = input("Enter the Event Name: ")
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                eventLocation = input("Enter the Event Location: ")
                event.AddValues(eventName, eventDate, eventLocation)
        elif eventOption == 3:
            print("MODIFY MENU")
            print()
            print("1. To update Event Name")
            print("2. To update Event Date")
            print("3. To update Event Location")
            print("4. Back to Events Menu")
            print()

            modifyEventOption = int(input("Enter the desired option: "))
            print()

            if modifyEventOption == 1:
                eventName = input("Enter the current Event Name: ")
                event.ModifyValues(1, eventName)
            elif modifyEventOption == 2:
                eventDate = input("Enter the current Event Date (YYYY-MM-DD): ")
                event.ModifyValues(2, eventDate)
            elif modifyEventOption == 3:
                eventLocation = input("Enter the current Event Location: ")
                event.ModifyValues(3, eventLocation)
        
        elif eventOption == 4:
            deleteOption = int(input("Enter the option to delete by:\n1. Event Name\n2. Event Date\n3. Location\n"))
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
            print("PRINT DATA MENU")
            print()
            print("1. Print all events")
            print("2. Print event by name")
            print("3. Print events by date")
            print("4. Print events by location")
            print("5. Back to Events Menu")
            print()

            printOption = int(input("Enter your desired option: "))
            print()

            if printOption == 1:
                event.PrintData(1)
            elif printOption == 2:
                eventName = input("Enter the Event Name: ")
                event.PrintData(2, eventName)
            elif printOption == 3:
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                event.PrintData(3, eventDate)
            elif printOption == 4:
                eventLocation = input("Enter the Event Location: ")
                event.PrintData(4, eventLocation)

        elif eventOption == 6:
            continue

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

        attendeeOption = int(input("Enter your desired option: "))
        print()

        attendee = Attendees()

        if attendeeOption == 1:
            attendee.CreateTable()
        elif attendeeOption == 2:
            nAttendees = int(input("Enter the number of attendees you want to add: "))
            for i in range(nAttendees):
                attendeeName = input("Enter the Attendee Name: ")
                attendeeEmail = input("Enter the Attendee Email: ")
                attendee.AddValues(attendeeName, attendeeEmail)
        elif attendeeOption == 3:
            attendeeID = int(input("Enter the Attendee ID to modify: "))
            attendeeName = input("Enter the new Attendee Name: ")
            attendeeEmail = input("Enter the new Attendee Email: ")
            attendee.ModifyValues(attendeeID, attendeeName, attendeeEmail)
        elif attendeeOption == 4:
            attendeeID = int(input("Enter the Attendee ID to delete: "))
            attendee.DeleteValues(attendeeID)
        elif attendeeOption == 5:
            attendee.PrintData()

        elif attendeeOption == 6:
            continue

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

        registrationOption = int(input("Enter your desired option: "))
        print()

        registration = Registration()

        if registrationOption == 1:
            registration.CreateTable()
        elif registrationOption == 2:
            eventID = int(input("Enter the Event ID for Registration: "))
            attendeeID = int(input("Enter the Attendee ID for Registration: "))
            registration.AddValues(eventID, attendeeID)
        elif registrationOption == 3:
            registrationID = int(input("Enter the Registration ID to modify: "))
            eventID = int(input("Enter the new Event ID for Registration: "))
            attendeeID = int(input("Enter the new Attendee ID for Registration: "))
            registration.ModifyValues(registrationID, eventID, attendeeID)
        elif registrationOption == 4:
            registrationID = int(input("Enter the Registration ID to delete: "))
            registration.DeleteValues(registrationID)
        elif registrationOption == 5:
            registration.PrintData()

        elif registrationOption == 6:
            continue

    elif options == 4:
        print("Exiting Event Database Management System. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a valid option from the menu.")
