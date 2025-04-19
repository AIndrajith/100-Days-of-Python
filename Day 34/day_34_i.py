import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x300")

# Listbox Widget
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Add items to listbox
listbox.insert(tk.END, "Task 1")
listbox.insert(tk.END, "Task 2")

# Get selected item
def get_selected():
    selected = listbox.get(tk.ACTIVE)
    print("Selected:",selected)

button = tk.Button(root, text="Get Selected", command=get_selected)
button.pack(pady=10) 

root.mainloop()