# Question 3 - Simple version

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('monthsales.csv')

# Create the line chart
plt.figure(figsize=(10, 6))

# Plot each year
plt.plot(df['Month'], df['2018'], marker='o', label='2018')
plt.plot(df['Month'], df['2019'], marker='s', label='2019')
plt.plot(df['Month'], df['2020'], marker='^', label='2020')
plt.plot(df['Month'], df['2021'], marker='d', label='2021')

# Add title and labels
plt.title('Year-Wise Sales')
plt.xlabel('Months')
plt.ylabel('Sales')

# Add legend and grid
plt.legend()
plt.grid(True)

# Display the chart
plt.show()