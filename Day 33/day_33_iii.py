import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Validation Example")
root.geometry("300x200")

# Input Field
entry = tk.Entry(root)
entry.pack(pady=10)

# Validation Input
def validate_input():
    user_input = entry.get()
    if user_input.strip()== "":
        messagebox.showerror("Error","Input cannot be empty! ")
    else:
        messagebox.showinfo("Success",f"you entered : {user_input}")

# Button 
button = tk.Button(root, text="Submit", command=validate_input)        
button.pack(pady=10)

root.mainloop()