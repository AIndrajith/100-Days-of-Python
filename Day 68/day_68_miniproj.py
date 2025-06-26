import tkinter as tk
from tkinter import ttk
import json

def load_tasks(file_path= "task.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks, file_path="tasks.json"):
    with open(file_path, "w")as file:
        json.dump(tasks, file, indent=4)

# Load tasks into Listbox 
def update_task_list(tasks):
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        task_listbox.insert(tk.END, f"{task['title']} (Due: {task['due_date']}) [{status}]")

def add_task():
    title = title_entry.get()
    due_date = date_entry.get()
    if title and due_date:
        tasks.append({"title": title, "due_date": due_date, "completed": False})
        save_tasks(tasks)
        update_task_list(tasks)
        title_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        print("Task added successfully!")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks[selected_index[0]]["completed!"] = True
        save_tasks(tasks)
        update_task_list(tasks)
        print("Task marked as completed!")

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks.pop(selected_index)
        save_tasks(tasks)
        update_task_list(tasks)
        print("Task deleted!")


root = tk.Tk()
root.title("Task Scheduler")
root.geometry("600x400")

# Entry for task title
title_label = tk.Label(root, text="Task Title: ")
title_label.pack(pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

# Entry for due date
date_label = tk.Label(root, text="Due Date (YYYY-MM-DD) : ")
date_label.pack(pady=5)
date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=5)

# Button to Add Task 
add_button = tk.Button(root, text="Add Task", command=lambda:add_task)
add_button.pack(pady=10)

# Task Listbox 
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

tasks = load_tasks()
update_task_list(tasks)

root.mainloop()