import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def init(self, speed, angle, x, y):
        self.x_poc = x
        self.y_poc = y
        self.speed = speed
        self.angle = np.radians(angle)
        self.reset()

    def reset(self):
        self.t = [0]
        self.v_y = [self.speed * np.sin(self.angle)]
        self.x = [self.x_poc]
        self.y = [self.y_poc]

    def __move(self, dt):
        self.v_y.append(self.v_y[-1] - 9.81 * dt)
        self.x.append(self.x[-1] + np.cos(self.angle) * dt * self.speed)
        self.y.append(self.y[-1] +  self.v_y[-1] * dt)
        self.t.append(self.t[-1] + dt)

    def range(self):
        while self.y[-1] >= 0:
            self.__move(0.01)
        return self.x[-1]

    def plot_trajectory(self):
        self.reset()

        self.range()

        plt.plot(self.x, self.y, label='Kosi hitac')
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plt.title('Kosi hitac')
        plt.legend()
        plt.grid(True)
        plt.show()