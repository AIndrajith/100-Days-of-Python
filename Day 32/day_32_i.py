import tkinter as tk

# Main Window 
root = tk.Tk()
root.title("Canvas Examples")
root.geometry("400x400")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw Shapes 
canvas.create_line(10, 10, 200, 200, fill="blue", width=3)
canvas.create_rectangle(50, 50, 150, 150, outline="red", width=2)
canvas.create_oval(200, 50, 350, 200, outline="green", width=2)

root.mainloop()