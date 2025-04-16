import tkinter as tk

root = tk.Tk()
root.title("Input Validation")
root.geometry("300x200")

# Input Field
entry = tk.Entry(root)
entry.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result will be displayed here.")
result_label.pack(pady=10)

# Update Label
def update_label():
    text = entry.get()
    result_label.config(text=f"You entered: {text}")

button = tk.Button(root, text="Update",command=update_label) 
button.pack(pady=10) 

root.mainloop()