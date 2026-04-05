# Question 5: Bar chart for Compu-Tech Employee Data

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('emp.csv')

# Create red bar chart
plt.bar(df['Department'], df['No_of_Emp'], color='red', edgecolor='black')

# Add labels and title
plt.title('Compu-Tech Employee Data')
plt.xlabel('Departments')
plt.ylabel('Number of Employees')

# Show the chart
plt.show()