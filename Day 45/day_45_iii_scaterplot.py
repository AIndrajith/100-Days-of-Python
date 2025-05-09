# Creating Basic Plots

# Scaterplot

import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [2.5, 3.7, 4.6, 8.0, 10.5]

# Plot
plt.scatter(x, y, color="red")
plt.title("Scatter plot")
plt.xlabel("X-axis")
plt.ylabel("Y-label")
plt.show()