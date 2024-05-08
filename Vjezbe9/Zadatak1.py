import numpy as np
import matplotlib.pyplot as plt

# Konstante
G = 6.67408e-11  # Gravitacijska konstanta (Nm^2/kg^2)
m_S = 1.989e30  # Masa Sunca (kg)
n_Z = 5.9742e24  # Masa Zemlje (kg)
AU = 1.486e11  # Astronomska jedinica (m)
v0_Z = 29783  # Početna okomita brzina Zemlje (m/s)
godina = 365.242 * 24 * 3600  # Duljina godine u sekundama

# Početni uvjeti
x0 = AU  # Početni položaj Zemlje
y0 = 0  # Zemlja je na y = 0
vx0 = 0  # Horizontalna početna brzina Sunca (m/s)
vy0 = v0_Z  # Početna okomita brzina Zemlje (m/s)

# Funkcija za izračunavanje gravitacijske sile
def gravitacijska_sila(x, y):
    r = np.sqrt(x**2 + y**2)

    # r**3 jer je radius zemlje zanemariv naspram radijusu sunca
    Fx = -G * m_S * n_Z * x / r**3
    Fy = -G * m_S * n_Z * y / r**3

    return np.array([Fx, Fy])

# Eulerova metoda za numeričko rješavanje diferencijalnih jednadžbi
def euler_integration(r, v, dt):
    a = gravitacijska_sila(r[0], r[1]) / n_Z
    r += v * dt
    v += a * dt
    return r, v

# Inicijalizacija vektora za poziciju i brzinu
r = np.array([x0, y0], dtype=float)  # Postavljamo tip podataka na float64
v = np.array([vx0, vy0], dtype=float)  # Postavljamo tip podataka na float64

# Simulacija gibanja
dt = 3600  # Korak vremena u sekundama (jedan sat)
num_steps = int(godina / dt)  # Broj koraka za jednu godinu
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)

for i in range(num_steps):
    x_values[i] = r[0]
    y_values[i] = r[1]
    r, v = euler_integration(r, v, dt)

# Crtanje rezultata
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b', label='Earth')  # Plava linija Zemlje
plt.plot(0, 0, 'yo', markersize=10, label='Sun')  # Žuta točka Sunce
plt.plot([0], [AU], 'bo', markersize=5)  # Plava točka Zemlju
plt.title('Sun-Earth System')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
