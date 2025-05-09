# Bar chart

import matplotlib.pyplot as plt

# Data 
categories = ["A","B","C","D"]
values = [10, 20, 15, 30]

# Plot
plt.bar(categories, values, color="skyblue")
plt.title("Bar Chart")
plt.xlabel("categories")
plt.ylabel("Values")
plt.show()