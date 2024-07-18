import tkinter as tk
from tkinter import messagebox

# Task class definition
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return self.description

    def mark_completed(self):
        self.completed = True

# Load tasks from file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return [Task(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            if not task.completed:
                file.write(f"{task}\n")

# Add task
def add_task():
    task_description = task_entry.get()
    if task_description:
        task = Task(task_description)
        tasks.append(task)
        task_listbox.insert(tk.END, task.description)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Mark task as completed
def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        task.mark_completed()
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Delete task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create the main window
app = tk.Tk()
app.title("To-Do List")

# Load tasks
filename = 'tasks.txt'
tasks = load_tasks(filename)

# Task entry
task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)

# Add task button
add_task_button = tk.Button(app, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Task list box
task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.pack(pady=10)

# Populate the list box with tasks
for task in tasks:
    task_listbox.insert(tk.END, task.description)

# Complete task button
complete_task_button = tk.Button(app, text="Complete Task", command=complete_task)
complete_task_button.pack(pady=5)

# Delete task button
delete_task_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Save tasks on exit
def on_closing():
    save_tasks(filename, tasks)
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main loop
app.mainloop()