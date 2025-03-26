from typing import List

# Initialize an empty list to store tasks
tasks = []

# Function to add a new task
def add_task(task_name: str):
    global tasks
    # Create a task dictionary with name and completion status
    task = {"name": task_name, "completed": False}
    # Append the task to the tasks list
    tasks.append(task)
    print("Task added successfully.")

# Function to mark a task as completed
def complete_task(task_name: str):
    global tasks
    # Iterate through the tasks to find the matching task
    for task in tasks:
        if task['name'] == task_name:
            # Mark the task as completed
            task['completed'] = True
            print("Task marked as completed.")
            break
    else:
        # If no matching task is found
        print("Task not found.")

# Function to display all tasks
def show_tasks():
    print("\nTask List:")
    # Sort tasks by their completion status (Pending first)
    sorted_tasks = sorted(tasks, key=lambda t: t['completed'])
    for task in sorted_tasks:
        # Display task name and status
        status = "Done" if task['completed'] else "Pending"
        print(f"- {task['name']} [{status}]")

# Function to remove a task by name
def remove_task(task_name: str):
    global tasks
    # Filter out the task with the given name
    tasks = [task for task in tasks if task['name'] != task_name]
    print("Task removed successfully.")

# Task manager menu
def main():
    while True:
        try:
            # Display menu options
            print("\nTask Manager")
            print("1. Add Task")
            print("2. Complete Task")
            print("3. Show Tasks")
            print("4. Remove Task")
            print("5. Exit")
            # Get user input for menu choice
            choice = input("Enter your choice: ")

            # Validate the choice
            assert choice in {"1", "2", "3", "4", "5"}, "Invalid choice!"

            # Perform actions based on the user's choice
            if choice == "1":
                # Add a new task
                task_name = input("Enter task name: ")
                add_task(task_name)
            elif choice == "2":
                # Mark a task as completed
                task_name = input("Enter task name to mark as completed: ")
                complete_task(task_name)
            elif choice == "3":
                # Show all tasks
                show_tasks()
            elif choice == "4":
                # Remove a task
                task_name = input("Enter task name to remove: ")
                remove_task(task_name)
            elif choice == "5":
                # Exit the program
                print("Exiting...")
                break
            elif choice not in {"1", "2", "3", "4", "5"}:
                # Handle invalid choices
                print("Invalid choice. Try again.")
                continue
                print("Exiting...")
                break
            else:
                # Handle unexpected cases
                print("Invalid choice. Try again.")
        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
