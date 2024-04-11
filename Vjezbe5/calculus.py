import numpy as np

def derivacija_tocka(f, x, h=1e-5, method="three-step"):
    if method == "three-step":
        return (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)
    else:
        return (f(x + h) - f(x - h)) / (2*h)

def derivacija_raspon(f, lower, upper, h=1e-5, method="three-step"):
    points = np.linspace(lower, upper, num=100)
    derivatives = [derivacija_tocka(f, x, h, method) for x in points]
    return points, derivatives

def integracija_numericka(f, lower, upper, num_divisions):
    step = (upper - lower) / num_divisions
    x_values = np.linspace(lower, upper, num_divisions)
    y_values = f(x_values)
    integral = step * np.sum(y_values)
    return integral, integral - step * np.max(y_values), integral - step * np.min(y_values)

def integracija_trapezna(f, lower, upper, num_divisions):
    step = (upper - lower) / num_divisions
    x_values = np.linspace(lower, upper, num_divisions + 1)
    y_values = f(x_values)
    integral = step * (np.sum(y_values) - 0.5 * (y_values[0] + y_values[-1]))
    return integral