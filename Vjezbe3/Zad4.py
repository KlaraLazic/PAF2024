from matplotlib import pyplot as plt
import numpy as np


M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
PHI = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

PHI2 = list(PHI)
for i in range(len(PHI2)):
    PHI2[i] = PHI[i] ** 2

def duplaj(n):
    return n ** 2

a = np.sum(np.array(M) * np.array(PHI)) / sum(PHI2)

D = 0.005 # dijametar šipke
Dt = a / D

# Grafički prikaz
plt.plot(PHI, M, 'o', label='Podaci')
plt.plot(PHI, [a * phi for phi in PHI], 'r-', label='Linearna regresija')
plt.xlabel('φ (rad)')
plt.ylabel('M (Nm)')
plt.title('Linearna regresija za određivanje modula torzije')
plt.legend()
plt.grid(True)
plt.show()

print("Modul torzije (Dt):", Dt, "N/m")