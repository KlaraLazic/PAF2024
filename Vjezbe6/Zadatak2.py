
# Inicijalizacija oscilatora
from matplotlib import pyplot as plt
import numpy as np
from harmonic_oscillator import HarmonicOscillator


k = 1.0  # konstanta opruge
m = 1.0  # masa
x0 = 1.0  # početni položaj
v0 = 0.0  # početna brzina
oscillator = HarmonicOscillator(k, m, x0, v0)

# Parametri za graf
dt_values = [0.1, 0.01, 0.001]  # različiti koraci vremena
t_max = 10.0

def analiticki_period(k, m):
    return (2 * np.pi ) / np.sqrt(k / m)

analiticki_period_rezultat = analiticki_period(k, m)

def analiticki_pozicija(t, k, m, x0, v0):
    omega = np.sqrt(k / m)
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)

# Vremenski raspon
t_values = np.linspace(0, 10, 1000)

# Izračunamo položaje
x_values = analiticki_pozicija(t_values, k, m, x0, v0)

# Prikaz grafa
plt.figure(figsize=(10, 6))

for dt in dt_values:
    t = np.arange(0, t_max, dt)
    plt.scatter(t, oscillator.x(t, dt), label=f"dt={dt}", s=5)

plt.plot(t_values, x_values, label='Analiticki')
plt.xlabel('Vrijeme')
plt.ylabel('Položaj')
plt.title('Položaj harmonijskog oscilatora kao funkcija vremena')
plt.grid(True)
plt.legend()
plt.show()

# Ispitivanje perioda titranja
# for dt in dt_values:
#     period = oscillator.period(dt=dt, t_max=t_max)
#     print(f"Period titranja za dt={dt}: {period}")
#     print(f"Analiticki period: {analiticki_period_rezultat}")
#     print(f"Preciznost: {period / analiticki_period_rezultat * 100}\n")