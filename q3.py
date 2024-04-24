import matplotlib.pyplot as plt
import numpy as np

# Define the differential equation
def f(x, y, z):
    return z, 2 * z - y + x * (np.exp(x) - 1)

# 4th-order Runge-Kutta method
def runge_kutta_4th_order(f, x0, y0, z0, xf, h):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    x = x0
    y = y0
    z = z0
    while x < xf:
        k1y, k1z = f(x, y, z)
        k2y, k2z = f(x + h / 2, y + 1/ 2 * k1y, z + 1 / 2 * k1z)
        k3y, k3z = f(x + h / 2, y + 1/ 2 * k2y, z + 1 / 2 * k2z)
        k4y, k4z = f(x + h, y + k3y, z + k3z)
        y += h/ 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        z += h/ 6 * (k1z + 2 * k2z + 2 * k3z + k4z)
        x += h
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
    return x_values, y_values

# Given initial values
x0 = 0
y0 = 0
z0 = 0
xf = 1
h = 0.01

# Solve the differential equation using 4th-order Runge-Kutta method
x_values, y_values = runge_kutta_4th_order(f, x0, y0, z0, xf, h)
# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Approximate Solution (RK4)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution by RK 4 method')
plt.legend()
plt.grid(True)
plt.show()
