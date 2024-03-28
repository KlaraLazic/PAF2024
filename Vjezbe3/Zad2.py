N1 = 200
N2 = 2000
N3 = 20000

broj = 5

for i in range(0, N1):
    broj+= 1/3
for i in range(0, N1):
    broj -= 1/3    
print("nakon 200 iteracija", broj)

broj = 5
for i in range(0, N2):
    broj += 1/3
for i in range(0, N2):
    broj -= 1/3
print("nakon 2000 iteracija", broj)

broj = 5
for i in range(0, N3):
    broj += 1/3
for i in range(0, N3):
    broj -= 1/3
print("nakon 20000 iteracija", broj)

#  Zbog korištenja floating-point aritmetike u Pythonu, dolazi do gubitka preciznosti i zaokruživanja.