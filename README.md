Certainly! Here’s an updated version of the README to reflect the changes made to the project by introducing the `Task` class and the Tkinter GUI.

---

# To-Do List Application

This Python project is a simple GUI-based To-Do List Application using Tkinter. It allows users to manage tasks by adding, viewing, completing, and deleting them. The tasks are stored in a file for persistence.

## Features

- **Add Tasks**: Easily add new tasks using the input field and the "Add Task" button.
- **View Tasks**: All tasks are displayed in a list box.
- **Complete Tasks**: Select a task and mark it as completed, which removes it from the list.
- **Delete Tasks**: Remove tasks from the list without marking them as completed.
- **Persistent Storage**: Tasks are saved to a file (`tasks.txt`) on exit and loaded at startup.

## Getting Started

### Prerequisites

- Python 3.x with Tkinter installed (usually included with Python).

### Installing

1. Clone or download the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.

   ```bash
   cd todo-list-python
   ```

### Running the Application

1. Open a terminal or command prompt.

2. Run the main Python file.

   ```bash
   python todo_list_gui.py
   ```

3. Use the GUI to add, complete, or delete tasks.

## Usage

- **Add a Task**: Enter the task description in the input field and click "Add Task."
- **Complete a Task**: Select a task from the list and click "Complete Task" to mark it as completed.
- **Delete a Task**: Select a task from the list and click "Delete Task" to remove it.
- **Exit**: Closing the window will save all uncompleted tasks automatically.

## Code Overview

### Task Class

- **Description**: Encapsulates task-related data and behaviors.
- **Attributes**: 
  - `description` (str): The text of the task.
  - `completed` (bool): Status indicating if the task is completed.

### Main Components

- **Entry Widget**: For task input.
- **Listbox Widget**: Displays tasks.
- **Buttons**: For adding, completing, and deleting tasks.
- **Messagebox**: For error and confirmation messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to add or modify any sections based on specific details or additional features you want to highlight in your project.