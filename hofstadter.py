import matplotlib.pyplot as plt
import numpy as np

def generate_sequences(n_max):
    # Initialize sequences with 0 (index 0 is unused)
    Q = [0] * (n_max + 1)
    C = [0] * (n_max + 1)
    
    # Initial conditions for Q-sequence: Q(1)=1, Q(2)=1
    Q[1] = 1
    Q[2] = 1
    for n in range(3, n_max + 1):
        Q[n] = Q[n - Q[n-1]] + Q[n - Q[n-2]]
        
    # Initial conditions for Conway sequence: C(1)=1, C(2)=1
    C[1] = 1
    C[2] = 1
    for n in range(3, n_max + 1):
        C[n] = C[C[n-1]] + C[n - C[n-1]]
        
    # Calculate H(n) = C(n) - Q(n)
    H = [C[i] - Q[i] for i in range(n_max + 1)]
    
    return Q, C, H

# Parameters
n_limit = 100000
Q, C, H = generate_sequences(n_limit)
n_values = np.arange(1, n_limit + 1)

# --- Figure 2: The Hofstadter Chaotic Heart sequence H(n) ---
plt.figure(figsize=(10, 6))
plt.scatter(n_values, H[1:], s=0.1, color='black', alpha=0.5)
plt.title("Hofstadter Chaotic Heart Sequence $H(n) = C(n) - Q(n)$")
plt.xlabel("n")
plt.ylabel("H(n)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# plt.savefig('Hofstadter_heart_sequence.png')
# -----------------------------------------------------------------------------------------------
