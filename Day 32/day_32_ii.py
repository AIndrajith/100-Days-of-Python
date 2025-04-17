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
    canvas.create_oval(x, y, x+20, y+20, fill="red", outline="blue")

canvas.bind("<B1-Motion>", draw) 

root.mainloop()