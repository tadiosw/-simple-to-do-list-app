PART 1: Defining Your Problem

Task
In this project, I’m creating a simple to-do list app in Python. The app will allow users to add tasks, view them with deadlines, and delete completed ones. It will help people stay organized and keep track of their tasks. 📅

Requirements
The user will input the task description and the due date.
The app will store these tasks and allow the user to view them later. 📜
Users can also remove tasks that are no longer needed.
When a task is added, the app will show a confirmation message. ✔️
When a task is deleted, the app will notify the user. 🔔

Inspiration
I wanted to build this app because I’ve often struggled with keeping track of the things I need to do. A simple digital list seemed like the perfect solution, and it’s a great way to practice working with lists and user input in Python. 🖥️ The user will enter tasks through the console, and the app will show a list of all tasks and their deadlines. When a task is marked as complete, the user can remove it. Ultimately, the app will help users feel more organized by providing an easy-to-use interface for task management. 🗂️


PART 2: Working Through Specific Examples

Scenario 1: Adding a task
![Screenshot 2025-01-05 220708](https://github.com/user-attachments/assets/8a7be06d-2f65-4fc0-bcfc-19b137d01c35)

The user chooses to add a new task.
The app will ask for a description of the task (e.g., "Finish Python assignment") and the due date (e.g., "2025-01-10"). 📅
The task will be saved in a list, and the app will show a confirmation message: "Task 'Finish Python assignment' added with due date 2025-01-10." ✅
![2](https://github.com/user-attachments/assets/10ec9bfb-cfd9-4ff9-a41f-d720fc51c39c)


Scenario 2: Viewing all tasks
![4](https://github.com/user-attachments/assets/9b61f1aa-c970-44f3-afff-31f0aaa9ec36)



The user decides to see all tasks they’ve entered.
The app will print a list of all tasks and their deadlines. 📝



Scenario 3: Deleting a completed task

![5](https://github.com/user-attachments/assets/74ce2316-e4ef-4daf-b671-e7bdf8763fd1)

The user selects the option to delete a task.
They provide the task description, and the app removes the task from the list if it matches.
A confirmation message will be displayed, like "Task 'Finish Python assignment' deleted." 🗑️

PART 3: Generalizing Into Pseudocode

Task
Let’s outline the steps of the program in pseudocode to focus on the overall logic before diving into the actual Python code.


Function add_task():
  Get task description from the user
  Get due date from the user
  Add task to the list
  Print confirmation message: "Task added successfully!"

Function view_tasks():
  If there are no tasks:
    Print "No tasks available."
  Else:
    Loop through the task list:
      Print task description and due date

Function delete_task():
  Ask user for the task to delete
  If task exists in the list:
    Remove the task
    Print "Task deleted."
  Else:
    Print "Task not found."

Main program:
  Display the menu with options:
    - Add task
    - View tasks
    - Delete task
  If user selects 'add task':
    Call add_task()
  If user selects 'view tasks':
    Call view_tasks()
  If user selects 'delete task':
    Call delete_task()
    
PART 4: Testing Your Program

Test Case 1: Adding a task
Input: "Finish Python assignment" with a due date of "2025-01-10"
Expected result: The task should be added, and a confirmation message should appear.
Actual result: The program correctly adds the task and confirms it. ✅

Test Case 2: Viewing all tasks
Input: No tasks yet.
Expected result: The program should say, "No tasks available."
Actual result: The app works fine and gives the expected message. 💬

Test Case 3: Deleting a non-existent task
Input: Trying to delete "Read a book" (a task that doesn’t exist).
Expected result: The app should say, "Task not found."
Actual result: The program catches this case and displays the correct message. ❌

Tools Used:

-Python: The primary programming language used for creating the to-do list app.

-IDLE/IDE: An integrated development environment (IDE) like PyCharm or VSCode for coding, testing, and debugging the program.

-Terminal/Console: For running the program and interacting with the user input/output.

-GitHub: For sharing the code and collaborating on version control.

Skills Learned:

-Python Lists: Learned how to manage and manipulate lists to store and update tasks dynamically.

-User Input Handling: Gained hands-on experience in receiving, validating, and processing user input.

-Functions: Enhanced understanding of breaking down a problem into smaller, reusable functions (add, view, and delete tasks).

-Flow Control: Applied if-else conditions and loops for managing the app's logic.

-Debugging: Developed troubleshooting skills by testing and refining the program to ensure it works under different scenarios.

-Commenting and Documentation: Improved my ability to write clean, well-commented code to enhance readability and maintainability.

-Program Design: Enhanced problem-solving skills by structuring the program’s flow and logic in a clear, manageable way.


