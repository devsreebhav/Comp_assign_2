import numpy as np
import matplotlib.pyplot as plt
# Define the differential equation
def f(t, y, y_prime):
    return t* np.log(t) +(2/t)*y_prime - 2*(y/t**2)
# Exact solution
def exact_solution(t):
    return (7*t/4) + (t**3/2)* np.log(t) - (3/4)*t**3
# Euler's method for second-order ODE
def euler_second_order(t0, y0, y_prime0, h, N):
    t_values = [t0]
    y_values = [y0]
    y_prime_values = [y_prime0]

    for _ in range(N):
        t_new = t_values[-1] + h
        y_prime_new = y_prime_values[-1] + h * f(t_values[-1], y_values[-1], y_prime_values[-1])
        y_new = y_values[-1] + h * y_prime_values[-1]
        
        t_values.append(t_new)
        y_prime_values.append(y_prime_new)
        y_values.append(y_new)

    return t_values, y_values

# Initial conditions and parameters
t0 = 1
y0 = 1
y_prime0 = 0
h = 0.001
N = int((2 - t0) / h)

# Solve using Euler's method
t_values, y_values = euler_second_order(t0, y0, y_prime0, h, N)

# Compute exact solution
t_exact = np.linspace(t0, 2, 100)
y_exact = exact_solution(t_exact)

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label="Euler's Method")
plt.plot(t_exact, y_exact, label="Exact Solution", linestyle='--')
plt.title("Approximate and Exact Solutions")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
