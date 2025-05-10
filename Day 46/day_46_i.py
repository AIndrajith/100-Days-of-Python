# Loading and Exploring data

import pandas as pd

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