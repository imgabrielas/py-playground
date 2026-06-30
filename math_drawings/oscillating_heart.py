import numpy as np
import matplotlib.pyplot as plt

# 1. Define x between -e and e
limit = np.e
x = np.linspace(-limit, limit, 5000)

# 2. Define the function
# y = sin(pi^3 * x) * sqrt(e^2/2 - x^2/2) + sqrt(abs(x))
y = np.sin(np.pi**3 * x) * np.sqrt(np.e**2 / 2 - x**2 / 2) + np.sqrt(np.abs(x))

# 3. Create Figure (10x10 inches * 100 dpi = 1000x1000 pixels)
plt.figure(figsize=(10, 10), dpi=100)

# 4. Plot
plt.plot(x, y, color='#EF1A2D', linewidth=1.5)
plt.title(r'$y = \sin(\pi^3 x) \sqrt{\frac{e^2}{2} - \frac{x^2}{2}} + \sqrt{|x|}$')
plt.grid(True, linestyle='--', alpha=0.5)
plt.axis('equal')

# 5. SAVE FIRST, SHOW SECOND
# plt.savefig('oscillating_heart.png')
plt.show()
