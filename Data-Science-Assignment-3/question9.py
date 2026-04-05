import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# Part (a) - Pie Chart
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
totals = [df[p].sum() for p in products]
plt.figure(figsize=(8, 8))
plt.pie(totals, labels=products, autopct='%1.1f%%')
plt.title('Total Units Sold per Product')
plt.show()

# Part (b) - Subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(df['month_number'], df['bathingsoap'], 'bo-', label='Bathing Soap')
ax1.set_title('Bathing Soap Sales')
ax1.legend()
ax2.plot(df['month_number'], df['facewash'], 'gs-', label='Facewash')
ax2.set_title('Facewash Sales')
ax2.set_xlabel('Month')
ax2.legend()
plt.tight_layout()
plt.show()