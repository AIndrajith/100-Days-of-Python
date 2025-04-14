import tkinter as tk

# main window 
root = tk.Tk()
root.title("Button Events")
root.geometry("300x200")

# Event handlers
def on_enter(event):
    button.config(text="Mouse over")

def on_leave(event):
    button.config(text="Mouse Out")

# create Button
button = tk.Button(root, text="Hover Me")
button.pack(pady=20)

# Bind Events
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()