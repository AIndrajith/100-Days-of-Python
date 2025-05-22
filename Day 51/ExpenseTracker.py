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

def plot_expenses_by_category(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8), title="Expenses by Category")
    plt.ylabel("")
    plt.show()


def plot_monthly_trends(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    monthly_summary.plot(kind="bar", figsize=(10, 6), title="Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.show()

def main():
    print("Welcome to the Expenses Tracker!")
    while True:
        print("\nOptions: ")
        print("1. Log an Expenses")
        print("2. View Expenses Summary")
        print("3. Plot Expenses by Category")
        print("4. Plot Monthly Trends")
        print("5. Exit")

        choice = input("Enter your Choice: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter Amount: "))
            description = input("Enter Description: ")

            load_expenses(date, category, amount, description)
            print("Expense logged successfull!")

        elif choice == "2":
            df = load_expenses()
            summarize_expenses(df)
        
        elif choice == "3":
            df = load_expenses()
            plot_expenses_by_category(df)

        elif choice == "4":
            df = load_expenses()
            plot_monthly_trends(df) 

        elif choice == "5":
            print("Good bye!")
            break       
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()