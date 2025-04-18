from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.withdraw() # Hides the main window

# Show different message boxes
messagebox.showinfo("Info","This is an info message")
messagebox.showwarning("Warning", "This is a warning message")
messagebox.showerror("error","This is an error message")

response = messagebox.askyesno("Question ", "Do you want to continue?")
print("Response: ",response)