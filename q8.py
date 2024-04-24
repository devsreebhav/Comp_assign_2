import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# Define the differential equations
def fun1(t, y):
    return t * np.exp(3*t) - 2*y
def fun2(t, y):
    return 1 - (t - y)**2
def fun3(t, y):
    return 1 + y/t
def fun4(t, y):
    return np.cos(2*t) + np.sin(3*t)
# Define the analytical solutions for each problem
def analytical_sol1(t):
    return  (np.exp(-2*t)/25)*(1+np.exp(5*t)*(-1+5*t))
def analytical_sol2(t):
    return (t**2-3*t+1)/(t-3)
def analytical_sol3(t):
    return t*(np.log(t)+2)
def analytical_sol4(t):
    return (1/6) * (3*np.sin(2*t) -2* np.cos(3*t) + 8)
# Define the time span for each problem
t_span1 = (0, 1)
t_span2 = (2, 3)
t_span3 = (1, 2)
t_span4 = (0, 1)
# Define the initial conditions for each problem
y0_1 = 0
y0_2 = 1
y0_3 = 2
y0_4 = 1
# Solve each initial value problem numerically
sol1 = solve_ivp(fun1, t_span1, [y0_1], t_eval=np.linspace(0, 1, 100))
sol2 = solve_ivp(fun2, t_span2, [y0_2], t_eval=np.linspace(2, 3, 100))
sol3 = solve_ivp(fun3, t_span3, [y0_3], t_eval=np.linspace(1, 2, 100))
sol4 = solve_ivp(fun4, t_span4, [y0_4], t_eval=np.linspace(0, 1, 100))

# Calculate analytical solutions
t_values1 = np.linspace(0, 1, 100)
analytical_solution1 = analytical_sol1(t_values1)

t_values2 = np.linspace(2, 3, 100)
analytical_solution2 = analytical_sol2(t_values2)

t_values3 = np.linspace(1, 2, 100)
analytical_solution3 = analytical_sol3(t_values3)

t_values4 = np.linspace(0, 1, 100)
analytical_solution4 = analytical_sol4(t_values4)

# Plot the solutions
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.plot(sol1.t, sol1.y[0], label='Numerical Solution')
plt.plot(t_values1, analytical_solution1, label='Analytical Solution', linestyle='--')
plt.title("y' = te^3t - 2y, with y(0) = 0")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.subplot(222)
plt.plot(sol2.t, sol2.y[0], label='Numerical Solution')
plt.plot(t_values2, analytical_solution2, label='Analytical Solution', linestyle='--')
plt.title("y' = 1 - (t - y)^2, with y(2) = 1")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.subplot(223)
plt.plot(sol3.t, sol3.y[0], label='Numerical Solution')
plt.plot(t_values3, analytical_solution3, label='Analytical Solution', linestyle='--')
plt.title("y' = 1 + y/t, with y(1) = 2")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.subplot(224)
plt.plot(sol4.t, sol4.y[0], label='Numerical Solution')
plt.plot(t_values4, analytical_solution4, label='Analytical Solution', linestyle='--')
plt.title("y' = cos(2t) + sin(3t), with y(0) = 1")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
