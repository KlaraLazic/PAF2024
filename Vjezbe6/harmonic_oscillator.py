import numpy as np

import numpy as np

class HarmonicOscillator:
    def __init__(self, k, m, x0, v0):
        self.k = k  # konstanta opruge
        self.m = m  # masa
        self.x0 = x0  # početni položaj
        self.v0 = v0  # početna brzina

    def x(self, t, dt):
        x_values = [self.x0]
        v_values = [self.v0]
        for i in range(1, len(t)):
            x_new = x_values[-1] + v_values[-1] * dt
            v_new = v_values[-1] - (self.k / self.m) * x_values[-1] * dt
            x_values.append(x_new)
            v_values.append(v_new)
        return np.array(x_values)

    def v(self, t, dt):
        x_values = [self.x0]
        v_values = [self.v0]
        for i in range(1, len(t)):
            x_new = x_values[-1] + v_values[-1] * dt
            v_new = v_values[-1] - (self.k / self.m) * x_values[-1] * dt
            x_values.append(x_new)
            v_values.append(v_new)
        return np.array(v_values)

    def a(self, t, dt):
        x_values = [self.x0]
        v_values = [self.v0]
        a_values = [-(self.k / self.m) * self.x0]
        for i in range(1, len(t)):
            x_new = x_values[-1] + v_values[-1] * dt
            v_new = v_values[-1] - (self.k / self.m) * x_values[-1] * dt
            a_new = -(self.k / self.m) * x_new
            x_values.append(x_new)
            v_values.append(v_new)
            a_values.append(a_new)
        return np.array(a_values)

    def period(self, dt, t_max):
        t = np.arange(0, t_max, dt)
        x_values = self.x(t, dt)
        zero_crossings = np.where(np.diff(np.sign(x_values)))[0]
        crossing_times = t[zero_crossings]

        periods = np.diff(crossing_times)
        return np.mean(periods)