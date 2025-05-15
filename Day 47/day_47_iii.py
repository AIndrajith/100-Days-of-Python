# Plotting Temperature Trends ii

import pandas as pd
import matplotlib.pyplot as plt

# Load Temperature Data
data = pd.read_csv('temperature_data.csv', parse_dates=['Date'])

# Add Rolling Average Column
data["7-Day Average"] = data['Temperature'].rolling(window=7).mean()

plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--")
plt.title("Temperature Trends with Rolling Average")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()