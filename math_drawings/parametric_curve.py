import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 5000)
# x= sqrt(2) sin^(3)(t)
# y= -cos^(3)(t)-cos^(2)(t)+2cos(t)
x = np.sqrt(2) * np.power(np.sin(t), 3)
y = -np.power(np.cos(t), 3) - np.power(np.cos(t), 2) + 2 * np.cos(t)

plt.figure(figsize=(10, 10), dpi=100)
plt.plot(x, y, color='#EF1A2D', linewidth=2)
plt.title(r'Parametric Curve: $x = \sqrt{2} \sin^3(t), y = -\cos^3(t) - \cos^2(t) + 2\cos(t)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.5)
plt.axis('equal')


plt.plot(x, y)
# plt.savefig('parametric_curve.png')
plt.show()

