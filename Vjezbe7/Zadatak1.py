import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, theta, koeficijent_trenja=0.47, masa=5):
        self.v0 = v0  # početna brzina u m/s
        self.theta0 = np.radians(theta)  # početni kut u radijanima

        self.koeficijent_trenja = koeficijent_trenja
        self.gustoca_medija = 1.225 #kg/m3
        self.povrsina_tijela =  0.25
        self.masa = masa

        self.x = 0
        self.y = 0
        self.v = self.v0
        self.theta = self.theta0

        self.x_history = [self.x]
        self.y_history = [self.y]

    def euler_step(self, dt):
        # Za X
        vx = self.v * np.cos(self.theta)

        ax = -1 * np.sign(vx) * ((self.gustoca_medija * self.koeficijent_trenja * self.povrsina_tijela)/(2 * self.masa)) * vx**2

        vx_new = vx + ax * dt

        x_new = self.x + vx_new * dt

        # Za Y
        vy = self.v * np.sin(self.theta)
        
        ay = -9.81 + -1 * np.sign(vy) * ((self.gustoca_medija * self.koeficijent_trenja * self.povrsina_tijela)/(2 * self.masa)) * vy**2

        vy_new = vy + ay * dt

        y_new = self.y + vy_new * dt

        # Updejt
        self.x = x_new
        self.y = y_new
        self.v = np.sqrt(vx_new ** 2 + vy_new ** 2)
        self.theta = np.arctan(vy_new / vx_new)

        # print('x=', self.x, ',y=', self.y, ',vx=', vx_new, ',vy=', vy_new, ',ax=', ax, ',ay', ay)

        self.x_history.append(x_new)
        self.y_history.append(y_new)
        
        return x_new, y_new

def simulate_projectile(dt, total_time):
    # Parametri projektila
    v0 = 40  # početna brzina u m/s
    theta = 45  # početni kut u stupnjevima

    # Inicijalizacija projektila
    projectile = Projectile(v0, theta)

    x_values = [0]  # Početna pozicija po x osi
    y_values = [0]  # Početna pozicija po y osi
    
    current_time = 0
    
    while current_time < total_time:
        x_new, y_new = projectile.euler_step(dt)
        x_values.append(x_new)
        y_values.append(y_new)
        current_time += dt
        
    return x_values, y_values

# Parametri simulacije
dt_values = [0.1, 0.01, 0.001]  # različiti koraci vremena
total_time = 5  # ukupno vrijeme simulacije

# Simulacija i prikaz rezultata
plt.figure(figsize=(10, 6))
for dt in dt_values:
    x_values, y_values = simulate_projectile(dt, total_time)
    plt.plot(x_values, y_values, label=f'dt={dt}')

plt.title('Simulacija kosog hitca s otporom zraka')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.show()
