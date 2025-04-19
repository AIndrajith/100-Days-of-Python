import tkinter as tk

root = tk.Tk()
root.title("Listbox manage, ment")
root.geometry("300x300")

# listbox 
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# add item 
def add_item():
    item = entry.get()
    if item: 
        listbox.insert(tk.END, item)
        entry.delete(0,tk.END)

# delete item 
def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Entry field
entry = tk.Entry(root) 
entry.pack(pady=5) 

# buttons 
add_button = tk.Button(root, text="Add item", command=add_item)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete ITem", command=delete_item)
delete_button.pack(pady=5)

root.mainloop()