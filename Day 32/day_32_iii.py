import tkinter as tk

# Main Window 
root = tk.Tk()
root.title("Canvas Examples")
root.geometry("400x400")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw on Mouse Drag
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+2, y+2, fill="blue", outline="blue")

# clear function
def clear_canvas():
    canvas.delete("all")

# Bind drawing
canvas.bind("<B1-Motion>", draw) 

# clear button
clear_btn = tk.Button(root, text="clear", command=clear_canvas)
clear_btn.pack(pady=10)

root.mainloop()