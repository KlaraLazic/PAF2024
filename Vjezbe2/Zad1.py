import numpy as np
import matplotlib.pyplot as plt

# Ulazni podaci
F = float(input("Unesite iznos sile u N: "))
m = float(input("Unesite masu čestice u kg: "))

# Konstante
t_max = 10  # Maksimalno vrijeme za prikaz na grafu
dt = 0.01  # Korak integracije

# Inicijalni uvjeti
x0 = 0  # Početna pozicija
v0 = 0  # Početna brzina

# Funkcije kretanja
def x(t):
    return x0 + v0*t + 0.5*(F/m)*(t**2)

def v(t):
    return v0 + (F/m)*t

def a(t):
    return F/m

# Vremenska osa
t = np.arange(0, t_max, dt)

x_t = np.zeros_like(t)
v_t = np.zeros_like(t)
a_t = np.zeros_like(t)

x_t[0] = x0
v_t[0] = v0
a_t[0] = a(t[0])

# Izračun pozicije, brzine i ubrzanja u svakom trenutku
for i in range(1,len(t)):
    x_t[i] = x(t[i])
    v_t[i] = v(t[i])
    a_t[i] = a(t[i])

# Crtanje grafova
plt.figure(figsize=(12, 6))

plt.subplot(311)
plt.plot(t, x_t)
plt.xlabel('vrijeme (s)')
plt.ylabel('pozicija (m)')
plt.title('x - t graf')

plt.subplot(312)
plt.plot(t, v_t)
plt.xlabel('vrijeme (s)')
plt.ylabel('brzina (m/s)')
plt.title('v - t graf')

plt.subplot(313)
plt.plot(t, a_t)
plt.xlabel('vrijeme (s)')
plt.ylabel('ubrzanje (m/s^2)')
plt.title('a - t graf')

plt.tight_layout()
plt.show()