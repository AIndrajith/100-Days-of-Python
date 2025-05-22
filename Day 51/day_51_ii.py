# Categorizing and Summarizing data

import csv
from datetime import datetime
import pandas as pd

def load_expenses():
    return pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])

def summarize_expenses(df):
    summary = df.groupby("Category")["Amount"].sum()
    print("\n Expense Summary: ")
    print(summary)

df = load_expenses()
summarize_expenses(df)