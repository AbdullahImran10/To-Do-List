import tkinter as tk
from database import *
create_database()
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
listbox = tk.Listbox(root, width=50, height=12)
listbox.pack(pady=10)
def refresh():
    listbox.delete(0, tk.END)
    tasks = get_tasks()
    for task in tasks:
        status = "✔" if task[2] else "✘"
        listbox.insert(
            tk.END,
            f"{task[0]} | {task[1]} | {status}"
        )
def add():
    task = entry.get()
    if task != "":
        add_task(task)
        entry.delete(0, tk.END)
        refresh()
def delete():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected)
        task_id = int(item.split("|")[0])
        delete_task(task_id)
        refresh()
def complete():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected)
        task_id = int(item.split("|")[0])
        complete_task(task_id)
        refresh()
tk.Button(root, text="Add Task", command=add).pack(pady=5)
tk.Button(root, text="Complete Task", command=complete).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete).pack(pady=5)
refresh()
root.mainloop()