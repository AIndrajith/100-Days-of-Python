# Loading and Exploring data

import pandas as pd
import matplotlib.pyplot as plt

# Load Sales Data
print("===== Load Sales Data =====")
data = pd.read_csv("sales_data.csv")
print(data.head())

# summary of Dataset
print("===== summary of Dataset =====")
print(data.info())

# Statistcal summary
print("===== Statistcal summary =====")
print(data.describe())

# Check for Missing Values
print("===== Check for Missing Values =====")
print(data.isnull().sum())

# Fill missing values
data["Product_Category"] = data["Product_Category"].fillna("Unknown")

# Drop Rows with missing values 
data = data.dropna()

# convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

data['Sales_Amount'] = pd.to_numeric(data["Sales_Amount"], errors='coerce')

# Add a Year-month Column
data['Year_Month'] = data["Date"].dt.to_period('M')

# add a Revenue column (if Quantity and Price are available)
data['Revenue'] = data['Quantity'] * data['Price']

########################################
# Generating Insights and Visualizations

# Total Sales by Month
print("\n==Total Sales by Month==")
monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
print(monthly_sales)

# Top Products
print("\n===Top Products===")
top_products = data.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head(5)
print(top_products)

# Plot Monthly Sales
monthly_sales.plot(kind="bar", figsize=(10, 6), color="skyblue")
plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()