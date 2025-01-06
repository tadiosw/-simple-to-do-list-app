# Code with Comments:
# Simple to-do list app with basic add, view, and delete functionality.

def add_task():
    task_desc = input("Enter task description: ")  # Prompt the user for task description
    due_date = input("Enter task due date (YYYY-MM-DD): ")  # Prompt the user for task due date
    tasks.append({"description": task_desc, "due_date": due_date})  # Add task to the list
    print(f"Task '{task_desc}' added with due date {due_date}.")

def view_tasks():
    if not tasks:
        print("No tasks available.")  # If no tasks, show message
    else:
        for task in tasks:  # Loop through the list of tasks and print each one
            print(f"Task: {task['description']}, Due: {task['due_date']}")

def delete_task():
    task_desc = input("Enter task description to delete: ")  # Ask the user for the task to delete
    task_found = False
    for task in tasks:
        if task_desc == task["description"]:
            tasks.remove(task)  # Remove the task from the list
            task_found = True
            print(f"Task '{task_desc}' deleted.")
            break
    if not task_found:
        print("Task not found.")  # If task doesn't exist, show message

def main():
    print("Welcome to your to-do list app!")  # Greet the user
    while True:
        print("\nMenu: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid inputs

tasks = []  # List to hold tasks

if __name__ == "__main__":
    main()  # Start the program
