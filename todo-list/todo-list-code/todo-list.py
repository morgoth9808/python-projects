import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, f"⬜ {task}")  # Adding an empty checkbox
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task_index)
        if task_text.startswith("⬜"):
            task_text = "✅" + task_text[1:]  # Replace checkbox with a checkmark
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, task_text)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Function to save tasks to a text file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task[2:] + "\n")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack()

task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
task_listbox.pack()

# Load tasks from a text file (if it exists)
try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            task_listbox.insert(tk.END, f"⬜ {task.strip()}")
except FileNotFoundError:
    pass

# Start the GUI main loop
root.mainloop()
