# Question 4 - Simplified with loop

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('monthsales.csv')

# Colors for each year
colors = {'2018': 'blue', '2019': 'green', '2020': 'orange', '2021': 'red'}

# Create the chart
plt.figure(figsize=(12, 7))

# Loop through each year and plot with customizations
for year in ['2018', '2019', '2020', '2021']:
    plt.plot(df['Month'], df[year], 
             marker='*',        # Star marker
             markersize=10,     # Size 10
             linestyle='--',    # Dashed line
             linewidth=3,       # Line width 3
             color=colors[year],
             label=year)

# Labels and title
plt.title('Year-Wise Sales', fontsize=16, fontweight='bold')
plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales', fontsize=12)

# Legend and grid
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()