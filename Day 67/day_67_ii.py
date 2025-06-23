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

root.mainloop()