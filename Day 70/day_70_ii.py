#  Creating interactive GUI with Tkinter

import pandas as pd
import tkinter as tk
from tkinter import filedialog

def load_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
    
data = load_file("sample_data.csv")
print(data.head())

root = tk.Tk()
root.title("Data Visualizer")
root.geometry("800x600")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    print(f"File selected: {file_path}")
    return file_path

upload_button = tk.Button(root, text="Upload File", command=open_file)
upload_button.pack(pady=10)

root.mainloop()