import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'State': ['Maharashtra', 'UP', 'Gujarat', 'Tamil Nadu', 'Kerala', 'Punjab', 'Bihar', 'West Bengal', 'Rajasthan', 'Delhi'],
    'Population': [112374333, 199812341, 60439692, 72147030, 33406061, 27743338, 104099452, 91276115, 68548437, 16787941],
    'Literacy_Rate': [82.34, 67.68, 78.03, 80.09, 93.91, 75.84, 61.80, 76.26, 66.11, 86.21],
    'Region': ['West', 'North', 'West', 'South', 'South', 'North', 'East', 'East', 'North', 'North']
})
df.to_csv('population_literacy.csv', index=False)
print("CSV file created!")

# Scatter plot
regions = df['Region'].unique()
colors = {'North': 'blue', 'South': 'green', 'East': 'orange', 'West': 'red'}
for region in regions:
    d = df[df['Region'] == region]
    plt.scatter(d['Population'], d['Literacy_Rate'], 
                marker='D', s=np.sqrt(d['Literacy_Rate'])*50, 
                color=colors[region], label=region)
plt.xlabel('Population'), plt.ylabel('Literacy Rate'), plt.legend()
plt.title('Population vs Literacy Rate by Region')
plt.show()

# Bar chart
df.groupby('Region')['Literacy_Rate'].mean().plot(kind='bar', color=['blue', 'green', 'orange', 'red'])
plt.title('Average Literacy Rate by Region')
plt.xlabel('Region'), plt.ylabel('Average Literacy Rate (%)')
plt.show()