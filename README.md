PART 1: Defining Your Problem
Task
 In this project, I'm creating a simple to-do list app. The app will allow users to add tasks, view them with deadlines, and delete completed ones. It will help people stay organized and keep track of their tasks.
Requirements
 The user will input the task description and the due date. The app will store these tasks and let the user view them later. Users can also remove tasks that are no longer needed. When a task is added, the app will show a confirmation message, and when it's deleted, the app will notify the user.
Inspiration
I wanted to build this app because I’ve often struggled with keeping track of things I need to do. A simple digital list seemed like the perfect solution, and it’s a great way to practice working with lists and user input in Python. The user will enter tasks through the console, and the app will show a list of all tasks and their deadlines. When a task is marked as complete, the user can remove it. Ultimately, the app will help the user feel more organized by providing an easy-to-use interface for task management.

 
PART 2: Working Through Specific Examples

Task:
 I want to break down the app into manageable pieces to make sure everything works smoothly. Here's how I imagine it would function step by step.
Scenario 1: Adding a task 
The user chooses to add a new task.![Screenshot 2025-01-05 220708](https://github.com/user-attachments/assets/41828696-c082-4437-a65c-bd892b271bdb)

The app will ask for a description of the task (e.g., "Finish Python assignment") and the due date (e.g., "2025-01-10"). ![5](https://github.com/user-attachments/assets/a0ccab9d-e983-42a2-bab7-ee1644fc5c6a)

The task will be saved in a list, and the app will show a confirmation message: "Task 'Finish Python assignment' added with due date 2025-01-10."
Scenario 2: Viewing all tasks![3](https://github.com/user-attachments/assets/087d54b3-7407-4321-a44f-76073bbcdb80)

The user decides to see all tasks they’ve entered.
The app will print a list of all tasks and their deadlines.![2](https://github.com/user-attachments/assets/b95e52de-9d0e-48f1-8c85-13bc604c6900)

Scenario 3: Deleting a completed task
The user selects the option to delete a task.
They provide the task description, and the app removes the task from the list if it matches.
A confirmation message will be displayed, like "Task 'Finish Python assignment' deleted."![5](https://github.com/user-attachments/assets/b0088557-b659-404e-928d-52a0d04bce96)


PART 3: Generalizing Into Pseudocode
Task
 Let’s get more specific and outline the steps of the program in pseudocode. This helps me focus on the overall logic before diving into the actual Python code.
Pseudocode:
Function add_task()
  Get task description from the user
  Get due date from the user
  Add task to the list
  Print confirmation message

Function view_tasks()
  If there are no tasks
    Print "No tasks available."
  Else
    Loop through the task list
      Print task description and due date

Function delete_task()
  Ask user for the task to delete
  If task exists in the list
    Remove the task
    Print "Task deleted."
  Else
    Print "Task not found."

Main program
  Display the menu with options
  If user selects 'add task'
    Call add_task()
  If user selects 'view tasks'
    Call view_tasks()
  If user selects 'delete task'
    Call delete_task()


PART 4: Testing Your Program
Task
 Once I’ve written some code, I’ll test it by simulating different scenarios to ensure it behaves as expected.
Test Case 1: Adding a task
Input: "Finish Python assignment" with a due date of "2025-01-10"
Expected result: The task should be added, and a confirmation message should appear.
Actual result: The program correctly adds the task and confirms it.
Test Case 2: Viewing all tasks
Input: No tasks yet.
Expected result: The program should say, "No tasks available."
Actual result: The app works fine and gives the expected message.
Test Case 3: Deleting a non-existent task
Input: Trying to delete "Read a book" (a task that doesn’t exist).
Expected result: The app should say, "Task not found."
Actual result: The program catches this case and displays the correct message.
