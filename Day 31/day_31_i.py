import tkinter as tk

# Main Window 
root = tk.Tk()
root.title("Input Field Example")
root.geometry("300x200")

# Input Field
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button to Display Input
def display_input():
    user_input = entry.get()
    print("User Input: ", user_input)

button = tk.Button(root, text="Submit",command=display_input) 
button.pack(pady=10) 

root.mainloop()