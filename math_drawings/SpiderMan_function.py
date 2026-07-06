import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-15, 15, 5000)

mask1 = (x >= -1.26) & (x <= 1.26)
z1 = np.where(mask1, -0.5 * np.cos(5 * x) + 5, np.nan)

mask2 = (x >= -2) & (x <= -0.3)
z2 = np.where(mask2, 2 * (x**2) - 10, np.nan)

mask3 = (x >= -2) & (x <= -1)
z3 = np.where(mask3, (-1/29) * (x**6), np.nan)

mask4 = (x >= 1) & (x <= 2)
z4 = np.where(mask4, (-1/29) * (x**6), np.nan)

mask5 = (x - 0.01021 >= -0.3) & (x - 0.01021 <= 0.3)
z5 = np.where(mask5, (x - 0.54021)**4 + 3 * (x - 0.54021)**3 - 2 * (x - 0.54021) - 10.2163, np.nan)

mask6 = (x >= 0.3) & (x <= 2)
z6 = np.where(mask6, 2 * (x**2) - 10, np.nan)

mask7 = (x >= 1) & (x <= 2.3)
z7 = np.where(mask7, 2 * np.power(np.abs(x - 1), x), np.nan)

mask8 = (x >= -2.3) & (x <= -1)
z8 = np.where(mask8, 2 * np.power(np.abs(-x - 1), -x), np.nan)

mask9 = (x - 0.27 >= 1) & (x - 0.27 <= 6)
z9 = np.where(mask9, np.sqrt(np.abs(x - 1.27)) + 4.53, np.nan)

mask10 = (x >= 4) & (x <= 7.13)
z10 = np.where(mask10, -((1/3) * (x**2) - 22.88), np.nan)

mask11 = (x + 0.27 >= -6) & (x + 0.27 <= -4)
z11 = np.where(mask11, 0.5 * (-(x + 0.27)**2) + 24.77, np.nan)

mask12 = (x - 0.28 >= 4) & (x - 0.28 <= 6)
z12 = np.where(mask12, 0.5 * (-(x - 0.28)**2) + 24.77, np.nan)

mask13 = (x >= 1) & (x <= 7.13)
z13 = np.where(mask13, np.sqrt(np.abs(x - 2.31)) + 3.63, np.nan)

mask14 = (x >= -7.1) & (x <= -1)
z14 = np.where(mask14, np.sqrt(np.abs(-(x + 2.3))) + 3.63, np.nan)

mask15 = (x >= -7.14) & (x <= -4)
z15 = np.where(mask15, -((1/3) * (x**2) - 22.88), np.nan)

mask16 = (x >= -6.2) & (x <= -1)
z16 = np.where(mask16, np.sqrt(np.abs(-x - 1.27)) + 4.53, np.nan)

mask17 = (x + 0.07 >= -8) & (x + 0.07 <= -2.1)
z17 = np.where(mask17, np.power(10.0, x + 2.06) + 2, np.nan)

mask18 = (x - 0.07 >= 2.1) & (x - 0.07 <= 8)
z18 = np.where(mask18, (1 / np.power(10.0, x - 2.06)) + 2, np.nan)

mask19 = (x >= -6) & (x <= -1.9)
z19 = np.where(mask19, np.power(10.0, x + 1.56) + 1.21, np.nan)

mask20 = (x >= 1.9) & (x <= 6)
z20 = np.where(mask20, (1 / np.power(10.0, x - 1.56)) + 1.21, np.nan)

mask21 = (x >= -4) & (x <= -1.8)
z21 = np.where(mask21, x + 3, np.nan)

mask22 = (x >= -3.27) & (x <= -1.4)
z22 = np.where(mask22, x + 2, np.nan)

mask23 = (x >= 1.8) & (x <= 4)
z23 = np.where(mask23, -x + 3, np.nan)

mask24 = (x >= 1.4) & (x <= 3.27)
z24 = np.where(mask24, -x + 2, np.nan)

mask25 = (x >= -4) & (x <= -2)
z25 = np.where(mask25, x**2 - 16.96, np.nan)

mask26 = (x >= 2) & (x <= 4)
z26 = np.where(mask26, x**2 - 16.96, np.nan)

mask27 = (x >= -6.04) & (x <= -4)
z27 = np.where(mask27, x**2 - 35.3, np.nan)

mask28 = (x >= 4) & (x <= 6.04)
z28 = np.where(mask28, x**2 - 35.3, np.nan)

mask29 = (x >= 2.2) & (x <= 10)
z29 = np.where(mask29, np.log10(np.abs(x)) + 2.44, np.nan)

mask30 = (x >= 2.5) & (x <= 8)
z30 = np.where(mask30, np.log10(np.abs(x)) + 3.63, np.nan)

mask31 = (x >= -10) & (x <= -2.2)
z31 = np.where(mask31, np.log10(np.abs(-x)) + 2.44, np.nan)

mask32 = (x >= -8) & (x <= -2.5)
z32 = np.where(mask32, np.log10(np.abs(-x)) + 3.63, np.nan)

mask33 = (x >= 8.07) & (x <= 8.27)
z33 = np.where(mask33, np.power(np.abs(x - 8.75), -4.0) - 0.08, np.nan)

mask34 = (x >= -8.27) & (x <= -8.07)
z34 = np.where(mask34, np.power(np.abs(x + 8.75), -4.0) - 0.08, np.nan)

mask35 = (x >= 8.26) & (x <= 10)
z35 = np.where(mask35, -0.5 * (x - 0.04)**2 + 53.11928, np.nan)

mask36 = (x - 0.04207 >= -10) & (x - 0.04207 <= -8.26)
z36 = np.where(mask36, -0.5 * (x - 0.04207)**2 + 53.5372, np.nan)

mask37 = (x >= 4) & (x <= 8.17)
z37 = np.where(mask37, np.power(0.5 * (x + 4.77) - 3.68, 3.0) - 19.76, np.nan)

mask38 = (x >= -8.17) & (x <= -4)
z38 = np.where(mask38, np.power(-0.5 * (x - 4.77) - 3.68, 3.0) - 19.76, np.nan)

mask39 = (x >= -3.27) & (x <= -2)
z39 = np.where(mask39, -(x + 7.27)**2 + 14.78, np.nan)

mask40 = (x >= 2) & (x <= 3.27)
z40 = np.where(mask40, -(x - 7.27)**2 + 14.78, np.nan)

# ===== BLACK BACKGROUND SETUP =====
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

all_curves = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20,
              z21, z22, z23, z24, z25, z26, z27, z28, z29, z30, z31, z32, z33, z34, z35, z36, z37, z38, z39, z40]

for curve in all_curves:
    ax.plot(x, curve, color='white', linewidth=2)

# ===== FILLS =====
ax.fill_between(x, z1, z5, where=mask1 & mask5, color='white')
ax.fill_between(x, z2, z3, where=mask2 & mask3, color='white')
ax.fill_between(x, z6, z4, where=mask6 & mask4, color='white')
ax.fill_between(x, z7, z13, where=mask7 & mask13, color='white')
ax.fill_between(x, z8, z14, where=mask8 & mask14, color='white')

plt.show()