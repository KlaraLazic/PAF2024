from math import erf
import numpy as np
import matplotlib.pyplot as plt
from calculus import integracija_numericka, integracija_trapezna

# Funkcije
def test_function(x):
    return np.exp(-x**2)

# Parametri
lower = -2
upper = 2
num_divisions = [5, 10, 20, 50]  # različiti brojevi podjela za testiranje

# Analitičko rješenje
analytical_solution = np.sqrt(np.pi) * (erf(upper) - erf(lower)) / 2

# Pravokutnu aproksimaciju
rectangular_upper_bounds = []
rectangular_lower_bounds = []
rectangular_middle_values = []
for n in num_divisions:
    integral, lower_bound, upper_bound = integracija_numericka(test_function, lower, upper, n)
    rectangular_upper_bounds.append(upper_bound)
    rectangular_lower_bounds.append(lower_bound)
    rectangular_middle_values.append(integral)

# Trapezna formula
trapezoidal_values = [integracija_trapezna(test_function, lower, upper, n) for n in num_divisions]

# Graf
plt.figure(figsize=(10, 6))
plt.plot(num_divisions, [analytical_solution]*len(num_divisions), label='Analitičko rješenje', linestyle='--')
plt.plot(num_divisions, rectangular_upper_bounds, label='Gornja međa (pravokutna)', marker='o')
plt.plot(num_divisions, rectangular_middle_values, label='Numerički integral (pravokutna)', marker='o')
plt.plot(num_divisions, rectangular_lower_bounds, label='Donja međa (pravokutna)', marker='o')
plt.plot(num_divisions, trapezoidal_values, label='Numerički integral (trapezna)', marker='o')
plt.title('Numerička integracija funkcije exp(-x^2)')
plt.xlabel('Broj podjela')
plt.ylabel('Vrijednost integrala')
plt.xscale('log')
plt.legend()
plt.show()
