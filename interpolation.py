import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

np.random.seed(42)  
x = np.linspace(0, 10, 50)
y = np.random.rand(50) * 2 - 1  # Random data between -1 and 1

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

ax1.plot(x, y, 'o', label='Data Points')
ax1.plot(x, y, '-', label='None Interpolation', drawstyle='steps-mid')
ax1.set_title('Interpolation Method: None')
ax1.legend()

ax2.plot(x, y, 'o', label='Data Points')
ax2.plot(x, y, '-', label='Linear Interpolation')
ax2.set_title('Interpolation Method: Linear')
ax2.legend()

x_new = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_new)

ax3.plot(x, y, 'o', label='Data Points')
ax3.plot(x_new, y_smooth, '-', label='Cubic Interpolation')
ax3.set_title('Interpolation Method: Cubic')
ax3.legend()

# Layout adjustments
plt.tight_layout()
plt.show(block=True)