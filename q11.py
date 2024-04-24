def f(t, x):
    return 1 /( x ** 2 + t ** 2)

def runge_kutta_step(t, x, h):
    k1 = h * f(t, x)
    k2 = h * f(t + h/2, x + k1/2)
    k3 = h * f(t + h/2, x + k2/2)
    k4 = h * f(t + h, x + k3)
    return x + (k1 + 2*k2 + 2*k3 + k4) / 6

def fourth_order_runge_kutta(t0, x0, t_end, h):
    t_values = [t0]
    x_values = [x0]
    t = t0
    x = x0
    while t < t_end:
        x = runge_kutta_step(t, x, h)
        t += h
        t_values.append(t)
        x_values.append(x)
    return t_values, x_values

# Initial conditions
t0 = 0
x0 = 1
t_end = 3.5e6
h = 1  # Step size

# Solve the initial value problem using fourth-order Runge-Kutta method
t_values, x_values = fourth_order_runge_kutta(t0, x0, t_end, h)

# Find the value of the solution at t = 3.5e6
idx = t_values.index(3.5e6)
solution_at_3p5e6 = x_values[idx]

print("Value of the solution at t = 3.5e6:", solution_at_3p5e6)
