from particle import Particle
import numpy as np

brzina = 10
kut = 45
x = 0
y = 0
my_particle = Particle()
my_particle.init(brzina, kut, x, y)

numericko = my_particle.range()
print("Numericko rjesenje:", numericko)

analiticko = (brzina**2 * np.sin(2 * np.radians(kut)))/9.81
print("Analiticko rjesenje:", analiticko)

print("Odstupanje:", abs (1 - (analiticko / numericko)) * 100, "%")