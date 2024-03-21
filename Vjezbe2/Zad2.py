import numpy as np
import matplotlib.pyplot as plt

# Definiramo početne uvjete
v0 = float(input('Unesite iznos početne brzine u m/s: '))
alfa = float(input('Unesite kut otklona alfa u stupnjevima: '))
g = 9.81  # ubrzanje slobodnog pada u m/s^2

# Konvertiramo kut alfa iz stupnjeva u radijane
alfa = np.deg2rad(alfa)

# Definiramo vektore za brzinu i položaj
v_t = np.array([[0.0] * 1000, [0.0] * 1000])
x_t = np.array([[0.0] * 1000, [0.0] * 1000])

# Postavljamo početne vrijednosti brzine i položaja
v_t[0, 0] = v0 * np.cos(alfa)
v_t[1, 0] = v0 * np.sin(alfa)
x_t[0, 0] = 0
x_t[1, 0] = 0

# Definiramo dt
dt = 0.01 

# Računamo položaj i brzinu u svakom trenutku
for i in range(1, 1000):
    # Računamo ubrzanje u svakom trenutku
    a_t = np.array([0, -g])
    
    # Računamo brzinu u svakom trenutku
    v_t[0, i] = v_t[0, i-1] + a_t[0] * dt
    v_t[1, i] = v_t[1, i-1] + a_t[1] * dt
    
    # Računamo položaj u svakom trenutku
    x_t[0, i] = x_t[0, i-1] + v_t[0, i-1] * dt
    x_t[1, i] = x_t[1, i-1] + v_t[1, i-1] * dt

# Iscrtavamo grafove
plt.figure(figsize=(12, 6))

# x-y graf
plt.subplot(311)
plt.plot(x_t[0], x_t[1])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('x-y graf')

# x-t graf
plt.subplot(312)
plt.plot(np.arange(0, 10, dt), x_t[0])
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title('x-t graf')

# y-t graf
plt.subplot(313)
plt.plot(np.arange(0, 10, dt), x_t[1])
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.title('y-t graf')

plt.tight_layout()
plt.show()
