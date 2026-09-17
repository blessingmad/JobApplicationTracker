# Import the sqlite3 module so we can work with the SQLite database
import sqlite3


# This function saves a new job application to the database
def save_application():

    # Ask the user to enter the company name
    company = input("Company name: ")

    # Ask the user to enter the position they applied for
    position = input("Position: ")

    # Ask the user to enter the date they applied
    date_applied = input("Date applied: ")

    # Ask the user to enter the current application status
    status = input("Status: ")

    # Ask the user to enter any additional notes
    notes = input("Notes: ")


    # Connect to the SQLite database
    # If tracker.db does not exist, SQLite will create it
    connection = sqlite3.connect("tracker.db")

    # Create a cursor so we can execute SQL commands
    cursor = connection.cursor()


    # Insert the information entered by the user
    # into the applications table
    cursor.execute("""
        INSERT INTO applications
        (company, position, date_applied, status, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (company, position, date_applied, status, notes))


    # Save the changes to the database
    connection.commit()

    # Close the database connection
    connection.close()


    # Tell the user that the application was successfully saved
    print("\nApplication saved successfully!")





# This function displays all job applications stored in the database
def view_applications():

    # Connect to the database
    connection = sqlite3.connect("tracker.db")

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Get all applications from the applications table
    cursor.execute("SELECT * FROM applications")

    # Store all returned records
    applications = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Check if there are no applications
    if not applications:
        print("\nNo applications found.")
        return

    # Display a heading
    print("\n===== JOB APPLICATIONS =====")

    # Display each application
    for application in applications:
        print(f"\nID: {application[0]}")
        print(f"Company: {application[1]}")
        print(f"Position: {application[2]}")
        print(f"Date Applied: {application[3]}")
        print(f"Status: {application[4]}")
        print(f"Notes: {application[5]}")
# Call the save_application function
# This starts the program and asks the user for information
# Add a new application
save_application()

# Display all saved applications
view_applications()