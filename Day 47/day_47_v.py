# Customizing and Saving Plots

import pandas as pd 
import matplotlib.pyplot as plt

# Load Temperature data
data = pd.read_csv('temperature_data.csv', parse_dates=['Date'])

plt.style.use("seaborn-v0_8-whitegrid")       # Change Style
plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="blue")
plt.title("Customized Temperature Plot")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("temperature_plot.png")     # Save the plot
plt.show()