"""
Student Assignment Tracker
IS 3020 Final Project
Delayshia Sturghill
"""

assignments = []
def add_assignment():
    name = input("Assignment name: ")
    course = input("Course: ")
    due_date = input("Due date: ")

    assignment = {
        "name": name,
        "course": course,
        "due_date": due_date
    }

    assignments.append(assignment)
    print("Assignment added successfully!")

def view_assignments():
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        for assignment in assignments:
            print("------------------------")
            print("Assignment:", assignment["name"])
            print("Course:", assignment["course"])
            print("Due Date:", assignment["due_date"])


def display_menu():
    print("\nStudent Assignment Tracker")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()