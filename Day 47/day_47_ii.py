# Plotting Temperature Trends

import pandas as pd
import matplotlib.pyplot as plt

# Load Temperature Data
data = pd.read_csv('temperature_data.csv', parse_dates=['Date'])

# Plot Temperature Trend
plt.plot(data['Date'], data['Temperature'], label="Temperature")
plt.title("Temperature Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()