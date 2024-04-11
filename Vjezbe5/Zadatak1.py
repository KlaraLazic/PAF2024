import numpy as np
import matplotlib.pyplot as plt
from calculus import derivacija_raspon

# Funkcije
def cubic_function(x):
    return x**3

def trig_function(x):
    return np.sin(x)

# Parametri
lower = -2*np.pi
upper = 2*np.pi
h = 0.1

# Derivacije
cubic_points, cubic_derivatives = derivacija_raspon(cubic_function, lower, upper, h=h)
trig_points, trig_derivatives = derivacija_raspon(trig_function, lower, upper, h=h)

# Graf
plt.figure(figsize=(10, 6))

# Kubna funkcija
plt.subplot(2, 1, 1)
plt.plot(cubic_points, cubic_function(cubic_points), label='Originalna funkcija (x^3)')
plt.plot(cubic_points, cubic_derivatives, label='Numerička derivacija', linestyle='--')
plt.title('Kubna funkcija i njena derivacija')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Trigonometrijska funkcija
plt.subplot(2, 1, 2)
plt.plot(trig_points, trig_function(trig_points), label='Originalna funkcija (sin(x))')
plt.plot(trig_points, trig_derivatives, label='Numerička derivacija', linestyle='--')
plt.title('Trigonometrijska funkcija i njena derivacija')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
