import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate normally distributed data
np.random.seed(42)  # for reproducibility
mu, sigma = 1, 0.01  # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

# Create the histogram
count, bins, ignored = plt.hist(s, 30, density=True, alpha=0.6, color='b', edgecolor='black')

# Fit a normal distribution to the data
best_fit_line = norm.pdf(bins, mu, sigma)

# Plot the histogram and the best fit line
plt.plot(bins, best_fit_line, 'r-', linewidth=2)

# Labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram with Gaussian Fit')

# Adding a legend
plt.legend(['Normal Distribution Fit', 'Histogram'])

# Save the plot to a file instead of showing it
plt.savefig('chart.png', dpi=300, bbox_inches='tight')

# Optionally, close the plot to free up memory
plt.close()