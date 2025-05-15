# Loading and Processing Temperature data

import pandas as pd

# Load Temperature Data
data = pd.read_csv('temperature_data.csv', parse_dates=['Date'])
print(data.head())