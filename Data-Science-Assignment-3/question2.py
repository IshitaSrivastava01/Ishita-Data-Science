# Step 1: Import the library we need
import matplotlib.pyplot as plt  # for drawing charts

# Step 2: Create the data (given in the question)
nos = [2, 9, 20, 25, 30, 39]     # Number of students
marks = [12, 24, 25, 27, 29, 30]  # Marks obtained

# Step 3: Create a horizontal bar chart
plt.figure(figsize=(10, 6))  # Make chart wider (width=10, height=6)

# barh() makes HORIZONTAL bars (h = horizontal)
# First parameter = y-axis values (marks)
# Second parameter = x-axis values (number of students)
plt.barh(marks, nos, color='skyblue', edgecolor='black')

# Step 4: Add labels and title
plt.ylabel('Marks Obtained')      # Label for y-axis (vertical axis)
plt.xlabel('Number of Students')   # Label for x-axis (horizontal axis)
plt.title('Number of Students vs Marks Obtained')

# Step 5: Add grid lines (makes it easier to read)
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Only vertical grid lines

# Step 6: Add value labels on the bars (shows the number on each bar)
for i, (students, mark) in enumerate(zip(nos, marks)):
    plt.text(students + 0.5, mark, str(students), va='center', fontsize=10)

# Step 7: Adjust layout so nothing gets cut off
plt.tight_layout()

# Step 8: Show the chart
plt.show()