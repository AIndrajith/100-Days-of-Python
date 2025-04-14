import tkinter as tk

root = tk.Tk()
root.title("Dynamic Button Counter")
root.geometry("300x200")

# Counter variable
counter = 0

def increment_counter():
    global counter
    counter += 1
    label.config(text=f"Count: {counter}")


# Label and Button 
label = tk.Label(root, text="Count: 0", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=increment_counter)
button.pack(pady=10)

root.mainloop()