import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

cluster1 = np.random.normal(loc=10, scale=2, size=500)
cluster2 = np.random.normal(loc=50, scale=10, size=500)
cluster3 = np.random.normal(loc=200, scale=50, size=500)

data = np.concatenate([cluster1, cluster2, cluster3])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.hist(data, bins=50, edgecolor='black')
ax1.set_title('Linear Scale')
ax1.set_xlabel('Time')
ax1.set_ylabel('Value')

ax2.hist(data, bins=50, edgecolor='black', log=True)
ax2.set_title('Logarithmic Scale')
ax2.set_xlabel('Time')
ax2.set_ylabel('Log(Value)')

plt.tight_layout()
plt.show(block=True)