# Question 7: Boxplot for Student Marks Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Marks.csv')

# Remove the Student column (only keep subject marks)
marks_data = df.drop('Student', axis=1)

# Create boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(marks_data.values, labels=marks_data.columns)

# Add labels and title
plt.title('Student Performance Analysis by Subject', fontsize=14, fontweight='bold')
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Show the chart
plt.tight_layout()
plt.show()

# Print summary statistics
print("\n" + "="*50)
print("SUBJECT SUMMARY STATISTICS")
print("="*50)
print(df.describe())