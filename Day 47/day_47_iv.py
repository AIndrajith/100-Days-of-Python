# Highlighting Anomalies and Averages

import pandas as pd
import matplotlib.pyplot as plt

# Load Temperature Data
data = pd.read_csv('temperature_data.csv', parse_dates=['Date'])

# Identify Anaomalies
mean_temp = data["Temperature"].mean()
std_temp = data["Temperature"].std()
data["Anomally"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)

# Plot with Anomalies
plt.plot(data["Date"], data["Temperature"], label="Daily Temperature")
plt.scatter(data[data["Anomally"]]["Date"], data[data["Anomally"]]["Temperature"], color="red" , label="Anomaly")
plt.title("Temperature Trends with Anomalies")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()