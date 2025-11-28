"""
Student Database Management Application
========================================
This application connects to a PostgreSQL database and performs CRUD operations
on the students table.

Requirements:
- Python 3.x
- psycopg2 library (pip install psycopg2-binary)
- PostgreSQL database with students table

Author: Sammy Eyongorock
Date: 3 November 2025
"""

import psycopg2
from psycopg2 import sql, Error
from datetime import datetime


class StudentDatabase:
    """
    A class to manage database operations for student records.

    Attributes:
        connection: PostgreSQL database connection object
        cursor: Database cursor for executing queries
    """

    def __init__(self, host="localhost", database="students_db", user="postgres", password="password"):
        """
        Initialize database connection.

        Args:
            host (str): Database host address
            database (str): Database name
            user (str): Database username
            password (str): Database password
        """
        try:
            # Establish connection to PostgreSQL database
            self.connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            self.cursor = self.connection.cursor()
            print(" Successfully connected to the database")

        except Error as e:
            print(f" Error connecting to PostgreSQL database: {e}")
            raise

    def getAllStudents(self):
        """
        Retrieves and displays all records from the students table.

        This function queries all student records and displays them in a
        formatted table structure.

        Returns:
            list: A list of tuples containing all student records
        """
        try:
            # Execute SELECT query to retrieve all students
            query = "SELECT * FROM students ORDER BY student_id;"
            self.cursor.execute(query)

            # Fetch all results
            students = self.cursor.fetchall()

            # Display results in formatted table
            print("\n" + "=" * 80)
            print("ALL STUDENTS")
            print("=" * 80)
            print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {
                  'Email':<30} {'Enrollment Date':<15}")
            print("-" * 80)

            if students:
                for student in students:
                    student_id, first_name, last_name, email, enrollment_date = student
                    print(f"{student_id:<5} {first_name:<15} {
                          last_name:<15} {email:<30} {enrollment_date}")
                print(f"\nTotal students: {len(students)}")
            else:
                print("No students found in the database.")

            print("=" * 80 + "\n")
            return students

        except Error as e:
            print(f" Error retrieving students: {e}")
            return []

    def addStudent(self, first_name, last_name, email, enrollment_date):
        """
        Inserts a new student record into the students table.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            email (str): Student's email address (must be unique)
            enrollment_date (str): Enrollment date in 'YYYY-MM-DD' format

        Returns:
            int: The student_id of the newly inserted record, or None if failed
        """
        try:
            # Prepare INSERT query with parameterized values to prevent SQL injection
            query = """
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
            """

            # Execute the query with provided values
            self.cursor.execute(
                query, (first_name, last_name, email, enrollment_date))

            # Get the ID of the newly inserted student
            student_id = self.cursor.fetchone()[0]

            # Commit the transaction to save changes
            self.connection.commit()

            print(f" Successfully added student: {
                  first_name} {last_name} (ID: {student_id})")
            return student_id

        except Error as e:
            # Rollback transaction in case of error
            self.connection.rollback()
            print(f" Error adding student: {e}")
            return None

    def updateStudentEmail(self, student_id, new_email):
        """
        Updates the email address for a student with the specified student_id.

        Args:
            student_id (int): The ID of the student to update
            new_email (str): The new email address

        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            # First check if the student exists
            check_query = "SELECT first_name, last_name, email FROM students WHERE student_id = %s;"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()

            if not student:
                print(f" No student found with ID: {student_id}")
                return False

            old_first_name, old_last_name, old_email = student

            # Prepare UPDATE query
            update_query = """
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
            """

            # Execute the update
            self.cursor.execute(update_query, (new_email, student_id))

            # Commit the transaction
            self.connection.commit()

            # Check if any rows were affected
            if self.cursor.rowcount > 0:
                print(f" Successfully updated email for {
                      old_first_name} {old_last_name}")
                print(f"  Old email: {old_email}")
                print(f"  New email: {new_email}")
                return True
            else:
                print(f" No changes made for student ID: {student_id}")
                return False

        except Error as e:
            # Rollback transaction in case of error
            self.connection.rollback()
            print(f" Error updating student email: {e}")
            return False

    def deleteStudent(self, student_id):
        """
        Deletes the record of the student with the specified student_id.

        Args:
            student_id (int): The ID of the student to delete

        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            # First check if the student exists and get their info
            check_query = "SELECT first_name, last_name, email FROM students WHERE student_id = %s;"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()

            if not student:
                print(f" No student found with ID: {student_id}")
                return False

            first_name, last_name, email = student

            # Prepare DELETE query
            delete_query = "DELETE FROM students WHERE student_id = %s;"

            # Execute the deletion
            self.cursor.execute(delete_query, (student_id,))

            # Commit the transaction
            self.connection.commit()

            # Check if any rows were affected
            if self.cursor.rowcount > 0:
                print(f" Successfully deleted student: {first_name} {
                      last_name} (ID: {student_id}, Email: {email})")
                return True
            else:
                print(f" No student deleted with ID: {student_id}")
                return False

        except Error as e:
            # Rollback transaction in case of error
            self.connection.rollback()
            print(f" Error deleting student: {e}")
            return False

    def close(self):
        """
        Closes the database connection and cursor.
        Should be called when done with database operations.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print(" Database connection closed")


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("STUDENT DATABASE MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. View all students")
    print("2. Add a new student")
    print("3. Update student email")
    print("4. Delete a student")
    print("5. Exit")
    print("=" * 60)


def main():
    """
    Main function to run the student database application.
    Provides an interactive menu for performing CRUD operations.
    """
    print("\n" + "*" * 60)
    print("STUDENT DATABASE APPLICATION")
    print("*" * 60)

    # Database connection parameters
    # IMPORTANT: Update these values to match your PostgreSQL setup
    DB_HOST = "localhost"
    DB_NAME = "students_db"
    DB_USER = "postgres"
    DB_PASSWORD = ""  # Your database Password

    try:
        # Initialize database connection
        db = StudentDatabase(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Main application loop
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                # View all students
                db.getAllStudents()

            elif choice == "2":
                # Add a new student
                print("\n--- Add New Student ---")
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                enrollment_date = input(
                    "Enter enrollment date (YYYY-MM-DD): ").strip()

                # Validate date format
                try:
                    datetime.strptime(enrollment_date, '%Y-%m-%d')
                    db.addStudent(first_name, last_name,
                                  email, enrollment_date)
                except ValueError:
                    print(" Invalid date format. Please use YYYY-MM-DD format.")

            elif choice == "3":
                # Update student email
                print("\n--- Update Student Email ---")
                try:
                    student_id = int(input("Enter student ID: ").strip())
                    new_email = input("Enter new email: ").strip()
                    db.updateStudentEmail(student_id, new_email)
                except ValueError:
                    print(" Invalid student ID. Please enter a number.")

            elif choice == "4":
                # Delete a student
                print("\n--- Delete Student ---")
                try:
                    student_id = int(
                        input("Enter student ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete student ID {
                                    student_id}? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        db.deleteStudent(student_id)
                    else:
                        print(" Deletion cancelled.")
                except ValueError:
                    print(" Invalid student ID. Please enter a number.")

            elif choice == "5":
                # Exit application
                print("\nExiting application...")
                break

            else:
                print(" Invalid choice. Please enter a number between 1 and 5.")

            input("\nPress Enter to continue...")

        # Close database connection
        db.close()

    except Exception as e:
        print(f"\n An error occurred: {e}")

    print("\nThank you for using the Student Database Application!")
    print("*" * 60 + "\n")


if __name__ == "__main__":
    main()
