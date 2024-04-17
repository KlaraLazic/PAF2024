import matplotlib.pyplot as plt
import numpy as np

from harmonic_oscillator import HarmonicOscillator

# Inicijalizacija oscilatora
k = 1.0  # konstanta opruge
m = 1.0  # masa
x0 = 1.0  # početni položaj
v0 = 0.0  # početna brzina
oscillator = HarmonicOscillator(k, m, x0, v0)

# Parametri za graf
dt_values = [0.1, 0.01, 0.001]  # različiti koraci vremena
t_max = 20.0

# Crtanje grafova
plt.figure(figsize=(15, 5))

# x-t graf
plt.subplot(1, 3, 1)
for dt in dt_values:
    t = np.arange(0, t_max, dt)
    plt.plot(t, oscillator.x(t, dt), label=f"dt={dt}")
plt.title("x - t graf")
plt.xlabel("t")
plt.ylabel("x")
plt.legend()

# v-t graf
plt.subplot(1, 3, 2)
for dt in dt_values:
    t = np.arange(0, t_max, dt)
    plt.plot(t, oscillator.v(t, dt), label=f"dt={dt}")
plt.title("v - t graf")
plt.xlabel("t")
plt.ylabel("v")
plt.legend()

# a-t graf
plt.subplot(1, 3, 3)
for dt in dt_values:
    t = np.arange(0, t_max, dt)
    plt.plot(t, oscillator.a(t, dt), label=f"dt={dt}")
plt.title("a - t graf")
plt.xlabel("t")
plt.ylabel("a")
plt.legend()

plt.tight_layout()
plt.show()