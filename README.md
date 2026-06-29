#  To-Do List Application

A simple desktop To-Do List application built using **Python**, **Tkinter**, and **SQLite**. This project allows users to add, view, complete, and delete tasks through a graphical user interface.

---

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Store tasks permanently using SQLite
* Simple and user-friendly GUI

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* SQLite (Database)

---

## Project Structure

```text
TodoApp/
│
├── main.py          # Entry point
├── gui.py           # GUI implementation
├── database.py      # Database operations
├── todo.db          # SQLite database (created automatically)
└── README.md
```

---

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python main.py
```

---

## Database

The application automatically creates an SQLite database named `todo.db` if it does not already exist.

Database table:

| Column    | Type                  |
| --------- | --------------------- |
| id        | INTEGER (Primary Key) |
| title     | TEXT                  |
| completed | INTEGER               |

---

## Future Improvements

* Edit existing tasks
* Add due dates
* Task priorities
* Search and filter tasks
* Dark mode
* Better UI using CustomTkinter
* User authentication

---

## Author

**Abdullah Imran**

Built as a Python learning project to practice GUI development, databases, and CRUD operations.
