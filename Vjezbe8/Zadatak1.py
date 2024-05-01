import numpy as np
import matplotlib.pyplot as plt

class Cestica:
    def __init__(self, q, m, xyz0, v0):
        self.q = q
        self.m = m
        self.xyz = [xyz0]
        self.v = [v0]

    def gibanje(self, E, B, dt, num_steps):
        for _ in range(num_steps):
            # a = (self.q / self.m) * (E + np.cross(self.v[-1], B))
            a = 0.00000000001 * (self.q / self.m) * (E + np.cross(self.v[-1], B))
            new_v = self.v[-1] + a * dt
            new_xyz = self.xyz[-1] + new_v * dt
            self.v.append(new_v)
            self.xyz.append(new_xyz)
        
        self.xyz = np.array(self.xyz)

# Konstante
q = -1.6e-19  # Naboja elektrona u Coulombima
m = 9.11e-31  # Masa elektrona u kilogramima

E = np.array([0, 0, 0])  # Vektor električnog polja u Voltima po metru
B = np.array([0, 0, 1.0])  # Vektor magnetskog polja u Teslama

# Početno stanje: položaj i brzina
xyz0 = np.array([0, 0, 0])    # Početni položaj u metrima
v0 = np.array([0.1, 0.1, 0.1])    # Početna brzina u metrima po sekundi

# Simulacija gibanja nabijene čestice
dt = 0.01  # Veličina vremenskog koraka u sekundama
num_steps = 1000  # Broj koraka simulacije

# Inicijalizacija čestica i simulacija gibanja
elektron = Cestica(q, m, xyz0, v0)
elektron.gibanje(E, B, dt, num_steps)
pozitron = Cestica(-q, m, xyz0, v0)
pozitron.gibanje(E, B, dt, num_steps)

# Crtanje putanje
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(elektron.xyz[:,0], elektron.xyz[:,1], elektron.xyz[:,2], label='Elektron', color='blue')
ax.plot(pozitron.xyz[:,0], pozitron.xyz[:,1], pozitron.xyz[:,2], label='Pozitron', color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
