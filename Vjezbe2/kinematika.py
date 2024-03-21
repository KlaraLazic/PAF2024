import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(sila, masa, vrijeme):
    # Ulazni podaci
    F = sila
    m = masa

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

def kosi_hitac(brzina, kut, vrijeme):
    v0 = brzina
    alfa = kut
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