import numpy as np
import matplotlib.pyplot as plt
# Constants
g = 10
t_max = 10
dt = 0.1
num_steps = int(t_max / dt) + 1
# Function to solve using relaxation method
def relaxation_method():
    x = np.zeros(num_steps)  # Initial guess for solution
    x[-1] = 0  # Boundary condition at t = t_max
    for _ in range(1000):  # Maximum iterations for convergence
        for i in range(num_steps - 2, 0, -1):  # Iterate backward in time
            x[i] = 0.5 * (x[i+1] + x[i-1] + g * dt ** 2)  # Relaxation formula
        # Check convergence (change below a threshold)
        if np.abs(x[1] - x[0]) < 1e-6:
            break
    return x
# Exact solution
def exact_solution(t):
    return -5*t ** 2+5*t
# Plotting
def plot_results():
    plt.figure(figsize=(10, 6))
# Plot exact solution
    t_exact = np.linspace(0, t_max, 100)
    x_exact = exact_solution(t_exact)
    plt.plot(t_exact, x_exact, label="Exact Solution", color="black")
# Numerical solution using relaxation method
    t_num = np.linspace(0, t_max, num_steps)
    x_num = relaxation_method()
    plt.plot(t_num, x_num, label="Numerical Solution (Relaxation Method)", linestyle="-", linewidth=2)
 # Candidate solutions
    for i in range(5):
        # Generate candidate solution by adding random noise to the numerical solution
        x_candidate = x_num + np.random.normal(loc=0, scale=0.1, size=num_steps)
        plt.plot(t_num, x_candidate, label=f"Candidate Solution {i+1}", linestyle="-", linewidth=1)
    plt.title("Boundary Value Problem: Relaxation Method")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot results
plot_results()
