import tkinter as tk
from tkinter import ttk
import json

def load_exchange_rates(file_path="exchange_rates.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Exchange rate file not found!")
        return {}

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def handle_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_dropdown.get()
        to_currency = to_currency_dropdown.get()
        rates = load_exchange_rates()
        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is not None:
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text="Conversion Error!")
    except ValueError:
        result_label.config(text="Invalid Amount!")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# From Currency Dropdown
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_dropdown = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY"])
from_currency_dropdown.pack(pady=5)

# To Currency Dropdown
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_dropdown = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY"])
to_currency_dropdown.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=lambda:handle_conversion)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()