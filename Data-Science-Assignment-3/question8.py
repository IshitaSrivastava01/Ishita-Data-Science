import matplotlib.pyplot as plt
import numpy as np

men = (22, 30, 35, 35, 26)
women = (25, 32, 30, 35, 29)
groups = ('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5')

x = np.arange(len(groups))

plt.bar(x - 0.2, men, 0.4, label='Men', color='steelblue')
plt.bar(x + 0.2, women, 0.4, label='Women', color='salmon')
plt.xticks(x, groups)
plt.title('Scores by Group and Gender')
plt.xlabel('Group')
plt.ylabel('Score')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()