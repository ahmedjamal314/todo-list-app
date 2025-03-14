# Simple To-Do List App

# Initialize an empty task list
tasks = []

def show_tasks():
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks yet! Add a new task.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added!')

def remove_task():
    """Remove a task from the list."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(task_num)
        print(f'Task "{removed_task}" removed!')
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    """Main loop to run the To-Do List app."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-4.")

# Run the app
if __name__ == "__main__":
    main()
