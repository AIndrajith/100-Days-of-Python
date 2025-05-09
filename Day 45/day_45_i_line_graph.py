# Creating Basic Plots

# Line Graph

import matplotlib.pyplot as plt

# Data 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot 
plt.plot(x, y, label="Line")
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()