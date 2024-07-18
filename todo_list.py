def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to load tasks from a file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to mark a task as completed
def mark_task_completed(tasks, task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' deleted.")
    else:
        print("Invalid task number.")


if __name__ == '__main__':
    main()
