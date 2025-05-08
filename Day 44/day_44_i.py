# Loading and Inspecting Data

import pandas as pd

# Load CSV File
df = pd.read_csv("data.csv")
print(df.head())

# Shape of the DataFrame
print(df.shape)

# Data Types
print(df.dtypes)

# Summary Statistics
print(df.describe())