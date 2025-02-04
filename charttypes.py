import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [30, 20, 45, 15]  # Example values for each category

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Different Chart Types for the Same Data', fontsize=16)

# Line Chart
axs[0, 0].plot(categories, values, marker='o')
axs[0, 0].set_title('Line Chart')
axs[0, 0].set_xlabel('Categories')
axs[0, 0].set_ylabel('Values')

# Bar Chart
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Bar Chart')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')

# Stacked Bar Chart
# Here we'll simulate another set of data for stacking
values2 = [10, 25, 15, 30]  # Another set for stacking
axs[1, 0].bar(categories, values, label='Set 1')
axs[1, 0].bar(categories, values2, bottom=values, label='Set 2')
axs[1, 0].set_title('Stacked Bar Chart')
axs[1, 0].set_xlabel('Categories')
axs[1, 0].set_ylabel('Values')
axs[1, 0].legend()

# Pie Chart
axs[1, 1].pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title('Pie Chart')
axs[1, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show(block=True)