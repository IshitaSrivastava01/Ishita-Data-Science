import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
profits = df['total_profit']

plt.hist(profits, bins=5, color='skyblue', edgecolor='black')
plt.title('Monthly Profit Distribution')
plt.xlabel('Profit (Rs)')
plt.ylabel('Number of Months')
plt.show()