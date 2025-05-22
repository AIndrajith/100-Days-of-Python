# Visualizing Expenses with Graphs

import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def load_expenses():
    return pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])

def summarize_expenses(df):
    summary = df.groupby("Category")["Amount"].sum()
    print("\n Expense Summary: ")
    print(summary)

df = load_expenses()
summarize_expenses(df)

def plot_expenses_by_category(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8), title="Expenses by Category")
    plt.ylabel("")
    plt.show()

plot_expenses_by_category(df)

def plot_monthly_trends(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    monthly_summary.plot(kind="bar", figsize=(10, 6), title="Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.show()

plot_monthly_trends(df)