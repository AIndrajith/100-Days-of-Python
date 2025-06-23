from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

currunt_canvas = None

def plot_stock_data(stock):
    global currunt_canvas
    if currunt_canvas:
        currunt_canvas.get_tk_widget().destroy()

    filtered_data = data[data["stock"] == stock]
    fig = Figure(figsize=(6,4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(filtered_data["date"], filtered_data["price"], marker="o")
    ax.set_title(f"{stock} Stock Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    currunt_canvas = FigureCanvasTkAgg(fig, master=root)
    currunt_canvas.draw()
    currunt_canvas.get_tk_widget().pack()

import pandas as pd
import tkinter as tk 
from tkinter import ttk

def load_data(file_path):
    return pd.read_csv(file_path)

# create the main window 
root = tk.Tk()
root.title("Stock market Dashboard")
root.geometry("600x400")

# Dropdown for selecting stock
stock_label = tk.Label(root, text="Select Stock: ")
stock_label.pack(pady=5)
stock_dropdown = ttk.Combobox(root, values=["AAPL", "MSFT"])
stock_dropdown.pack(pady=5)

# Button to plot data
plot_button = tk.Button(root, text="Plot Stock Data", command=lambda:print("Plotting data..."))
plot_button.pack(pady=10)

# Update the button to call plot_stock_data
plot_button.config(command=lambda: plot_stock_data(stock_dropdown.get()))

data = load_data("stock_data.csv")

root.mainloop()