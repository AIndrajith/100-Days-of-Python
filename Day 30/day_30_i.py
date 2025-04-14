import tkinter as tk

# Main Window 
root = tk.Tk()
root.title("Basic Button Example")
root.geometry("300x200")

# Button click Handler
def on_click():
    print("Button Clicked!")

# Create Button 
button = tk.Button(root, text="Click Me", command=on_click) 
button.pack(pady=20) 

# Run the application
root.mainloop()