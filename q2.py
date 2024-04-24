import math
import matplotlib.pyplot as plt
# Define the function for the initial value problem
def f(t, y):
    return y/t - (y/t)**2
# Analytical solution
def analytical_solution(t):
    return t / (1 + math.log(t))
# Euler's method
def euler_method(f, t0, y0, tf, h):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    while t < tf:
        y += h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

# Given initial values
t0 = 1
y0 = 1
tf = 2
h = 0.1

# Approximate solution using Euler's method
t_values, y_values = euler_method(f, t0, y0, tf, h)

# Analytical solution values
analytical_values = [analytical_solution(t) for t in t_values]

# Compute absolute error
absolute_error = [abs(analytical_values[i] - y_values[i]) for i in range(len(t_values))]

# Compute relative error
relative_error = [absolute_error[i] / analytical_values[i] for i in range(len(t_values))]

# Print absolute and relative errors
print("Absolute Errors:")
for i in range(len(t_values)):
    print(f"At t = {t_values[i]}: {absolute_error[i]}")

print("\nRelative Errors:")
for i in range(len(t_values)):
    print(f"At t = {t_values[i]}: {relative_error[i]}")

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label='Approximate Solution (Euler\'s Method)', marker='o')
plt.plot(t_values, analytical_values, label='Analytical Solution', linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Approximate and Analytical Solutions')
plt.legend()
plt.grid(True)
plt.show()
