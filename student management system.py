import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course"])


# Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    # Check if ID already exists
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == sid:
                print("Student ID already exists.")
                return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course])

    print("Student added successfully.")


# View All Students
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        rows = list(reader)

        if len(rows) <= 1:
            print("No student records found.")
            return

        print("\nStudent Records")
        print("-" * 40)

        for row in rows[1:]:
            print("ID     :", row[0])
            print("Name   :", row[1])
            print("Age    :", row[2])
            print("Course :", row[3])
            print("-" * 40)


# Search Student
def search_student():
    sid = input("Enter Student ID to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == sid:
                print("\nStudent Found")
                print("ID     :", row[0])
                print("Name   :", row[1])
                print("Age    :", row[2])
                print("Course :", row[3])
                return

    print("Student not found.")


# Update Student
def update_student():
    sid = input("Enter Student ID to Update: ")

    updated = False
    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            if row[0] == sid:
                print("Current Details")
                print("Name   :", row[1])
                print("Age    :", row[2])
                print("Course :", row[3])

                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")

                students.append([sid, name, age, course])
                updated = True
            else:
                students.append(row)

    if updated:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(header)
            writer.writerows(students)

        print("Student updated successfully.")
    else:
        print("Student ID not found.")


# Delete Student
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    deleted = False
    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            if row[0] == sid:
                deleted = True
            else:
                students.append(row)

    if deleted:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(header)
            writer.writerows(students)

        print("Student deleted successfully.")
    else:
        print("Student ID not found.")


# Main Menu
def main():
    create_file()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Program
main()
