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

def delete_assignment():
            if len(assignments) == 0:
                print("No assignments available to delete.")
                return

            view_assignments()

            try:
                number = int(input("Enter the assignment number to delete: "))

                if 1 <= number <= len(assignments):
                    removed_assignment = assignments.pop(number - 1)
                    print(removed_assignment["name"], "was deleted successfully.")
                else:
                    print("Invalid assignment number.")

            except ValueError:
                print("Please enter a whole number.")


def display_menu():
    print("\nStudent Assignment Tracker")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Delete Assignment")
    print("4. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            delete_assignment()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


main()