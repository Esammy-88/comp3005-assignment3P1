# Student Database Management Application

A Python application that connects to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on student records.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Database Setup](#database-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Application Functions](#application-functions)
- [Project Structure](#project-structure)
- [Video Demonstration](#video-demonstration)

## ✨ Features

- **View All Students**: Display all student records in a formatted table
- **Add Student**: Insert new student records with validation
- **Update Email**: Modify student email addresses
- **Delete Student**: Remove student records with confirmation
- **Error Handling**: Comprehensive error handling for database operations

## 🔧 Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **PostgreSQL 12 or higher** - [Download PostgreSQL](https://www.postgresql.org/download/)
- **pip** (Python package installer) - Usually comes with Python

## 🗄️ Database Setup

### Step 1: Create the Database

1. Open pgAdmin or use the PostgreSQL command line (psql)
2. Create a new database named `students_db`:

```sql
CREATE DATABASE students_db;
```

### Step 2: Create the Table and Insert Data

1. Connect to the `students_db` database
2. Run the SQL script provided in `database_scripts/database_setup.sql`:
   - In pgAdmin: Open Query Tool and execute the script
   - In psql: `\i path/to/database_setup.sql`

The script will:
- Create the `students` table with the required schema
- Insert the initial three student records
- Verify the data was inserted correctly

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/student-database-app.git
cd student-database-app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the required package directly:

```bash
pip install psycopg2-binary
```

## ⚙️ Configuration

### Update Database Connection Parameters

Before running the application, open `student_database.py` and update the database connection parameters in the `main()` function:

```python
# Database connection parameters
DB_HOST = "localhost"        # Your PostgreSQL host (usually localhost)
DB_NAME = "students_db"      # Your database name
DB_USER = "postgres"         # Your PostgreSQL username
DB_PASSWORD = "password"     # Your PostgreSQL password
```

**Security Note**: For production use, consider using environment variables or a configuration file to store credentials instead of hardcoding them.

## 🚀 Running the Application

### Method 1: Using Python directly

```bash
python student_database.py
```

### Method 2: Using Python3 (on some systems)

```bash
python3 student_database.py
```

## 📖 Application Functions

### 1. `getAllStudents()`
**Purpose**: Retrieves and displays all student records from the database.

**Usage**: Select option 1 from the main menu.

**Output**: Displays a formatted table with all student information including ID, name, email, and enrollment date.

### 2. `addStudent(first_name, last_name, email, enrollment_date)`
**Purpose**: Inserts a new student record into the database.

**Usage**: Select option 2 from the main menu and provide:
- First name
- Last name
- Email (must be unique)
- Enrollment date (YYYY-MM-DD format)

**Example**:
```
Enter first name: Alice
Enter last name: Johnson
Enter email: alice.johnson@example.com
Enter enrollment date (YYYY-MM-DD): 2024-01-15
```

### 3. `updateStudentEmail(student_id, new_email)`
**Purpose**: Updates the email address for a specific student.

**Usage**: Select option 3 from the main menu and provide:
- Student ID
- New email address

**Example**:
```
Enter student ID: 1
Enter new email: john.newemail@example.com
```

### 4. `deleteStudent(student_id)`
**Purpose**: Deletes a student record from the database.

**Usage**: Select option 4 from the main menu and provide:
- Student ID
- Confirmation (type "yes" to confirm)

**Example**:
```
Enter student ID to delete: 3
Are you sure you want to delete student ID 3? (yes/no): yes
```

## 📁 Project Structure

```
Student-database-app/
│
├── database_scripts/
│   └── database_setup.sql      # SQL script to create table
├── src/
│   └── student_database.py     # Main application file
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎥 Video Demonstration

**Video Link**: https://youtu.be/9-7yv0C5TPU

The demonstration video shows:
1. Database setup using the provided schema
2. Initial data insertion
3. Execution of `getAllStudents()` function
4. Execution of `addStudent()` function with verification in pgAdmin
5. Execution of `updateStudentEmail()` function with verification in pgAdmin
6. Execution of `deleteStudent()` function with verification in pgAdmin


### Getting Help

If you encounter other issues:
1. Check the error message displayed by the application
2. Verify your database connection settings
3. Ensure PostgreSQL is running and accessible
4. Check PostgreSQL logs for more detailed error information


## 📝 Database Schema

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);
```

## 📊 Initial Data

The application comes with three pre-populated student records:
- John Doe (john.doe@example.com) - Enrolled: 2023-09-01
- Jane Smith (jane.smith@example.com) - Enrolled: 2023-09-01
- Jim Beam (jim.beam@example.com) - Enrolled: 2023-09-02


## 📄 License

This project is created for educational purposes as part of a database programming assignment.

## 👤 Author

SAMMY EYONGOROCK

## 📅 Last Updated

November 2025

---

**Note**: Remember to update the database connection parameters before running the application, and ensure your PostgreSQL server is running!
