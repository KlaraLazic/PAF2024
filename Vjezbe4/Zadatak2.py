import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()

p1.init(10, 60, 0, 0)
print("Domet je ${:.2f} m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()