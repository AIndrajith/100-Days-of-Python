# Data Cleaning Techniques - >
# different data cleaning techniques include handling 
# missing values id there's missing values somewhere, 
# removing duplicates sometimes renaming columns.

# Transforming and Exporting Clean Data ->

import pandas as pd

# Load CSV File
df = pd.read_csv("data.csv")

# Find any missing values
print(df.isnull().sum())
# if there's any of missing values exists then 
# it comes the value  1 

# name        0
#  age        0
#  sex        1
# location    0

# like this is there are not any of missing values then 
# all values are 0


# Fill Missing Values 
df['sex'] = df['sex'].fillna(M)  # fillna() = fill not available

# Drop Rows with missing values 
df = df.dropna()  # dropna() = drop not available

# Check for Duplicates 
print(df.duplicated().sum())

# Drop Duplicates
df = df.drop_duplicates()

# Rename Columns
df = df.rename(columns={"age": "how old"})

# Apply a Transformation
df["name"] = df["name"].str.upper()

# Normalize Numeric data
df["age"] = (df["age"] - df["age"].mean())/ df["age"].std()