import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple login")
root.geometry("300x200")

# user credentials
USERNAME = "admin"
PASSWORD = "pwd123"

# Labels and Entry Fields
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show = "*")
password_entry.pack()

# Authentication Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Success", "Welcom, Admin")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Login Button 
login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack(pady=10)

root.mainloop()