# Job Application Tracker

A simple **Python and SQLite** application for managing and tracking job applications from the terminal.

The application allows users to record important information about jobs they have applied for, including the company, position, application date, status, and notes.

## Features

* Add a new job application
* Store application information in a SQLite database
* View saved job applications
* Track application status
* Add notes about each application
* Automatically create and use a local SQLite database

## Technologies Used

* **Python 3**
* **SQLite**
* **sqlite3** Python module

## Project Structure

```text
JobApplicationTracker/
│
├── database.py       # Creates the SQLite database and applications table
├── main.py           # Main program for entering and managing applications
├── tracker.db        # SQLite database containing saved applications
└── README.md         # Project documentation
```

## Database

The project uses SQLite to store job application information.

The database contains an `applications` table with the following fields:

| Field          | Description                                  |
| -------------- | -------------------------------------------- |
| `id`           | Unique ID for each application               |
| `company`      | Name of the company                          |
| `position`     | Job position applied for                     |
| `date_applied` | Date the application was submitted           |
| `status`       | Current application status                   |
| `notes`        | Additional information about the application |

## Getting Started

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python installation by running:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

### 2. Clone or Download the Project

If the project is on GitHub, clone it using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then move into the project folder:

```bash
cd JobApplicationTracker
```

### 3. Create the Database

Run:

```bash
python database.py
```

This creates the `tracker.db` SQLite database and the `applications` table if they do not already exist.

### 4. Run the Application

Start the application with:

```bash
python main.py
```

The program will ask you to enter information such as:

```text
Company name: Microsoft
Position: Junior Software Developer
Date applied: 2026-09-17
Status: Applied
Notes: Applied through LinkedIn
```

After entering the information, the application will save it to the SQLite database.

## Example

After running the program, you may see:

```text
Company name: ABC Technologies
Position: IT Support Technician
Date applied: 2026-09-17
Status: Applied
Notes: Application submitted through company website

Application saved successfully!
```

The information is stored in:

```text
tracker.db
```

## Viewing Applications

The project can retrieve saved applications from the SQLite database.

Example output:

```text
===== JOB APPLICATIONS =====

ID: 1
Company: ABC Technologies
Position: IT Support Technician
Date Applied: 2026-09-17
Status: Applied
Notes: Application submitted through company website
```

## Possible Application Statuses

You can use statuses such as:

* Applied
* Under Review
* Interview
* Second Interview
* Assessment
* Offer
* Rejected
* Withdrawn

## Future Improvements

The project can be expanded with additional features, including:

* [ ] Add a main menu
* [ ] View all applications
* [ ] Search applications
* [ ] Update application status
* [ ] Delete applications
* [ ] Sort applications by date
* [ ] Filter applications by status
* [ ] Add a Tkinter graphical user interface
* [ ] Add reminders for interviews and follow-ups
* [ ] Export applications to CSV
* [ ] Add application statistics
* [ ] Add edit/update functionality

## What I Learned

This project provides practical experience with:

* Python functions
* User input
* SQLite databases
* SQL `INSERT` and `SELECT` statements
* Database connections
* CRUD operations
* Python file organization
* Basic application development
* Error handling and debugging

## Author

**Blessing Madhuma**

This project was created as a beginner Python portfolio project to practice programming and database development.

## License

This project is available for educational and personal use.
