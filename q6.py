import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 10
t_max = 10
t1 = t_max
dt = 0.1
num_steps = int(t_max / dt) + 1

# Function to solve the ODE using the shooting method
def shooting_method(guess):
    x = np.zeros(num_steps)
    x[0] = 0  # Boundary condition at t = 0
    for i in range(num_steps - 1):
        x[i + 1] = x[i] + guess * dt  # Euler's method
        guess -= g * dt ** 2  # Update the guess using the ODE
    return x

# Exact solution
def exact_solution(t):
    return -5*t ** 2+5*t
# Function to find the optimal guess value using numpy.argmin
def find_optimal_guess():
    guess_values = np.linspace(-5, 5, 100)  # Initial guess values
    errors = []
    for guess in guess_values:
        x_num = shooting_method(guess)
        error = abs(x_num[-1] - 0)  # Absolute difference from the desired boundary condition
        errors.append(error)
    optimal_guess_index = np.argmin(errors)
    return guess_values[optimal_guess_index]

# Plotting
def plot_results():
    plt.figure(figsize=(10, 6))
    # Plot exact solution
    t_exact = np.linspace(0, t_max, 100)
    x_exact = exact_solution(t_exact)
    plt.plot(t_exact, x_exact, label="Exact Solution", color="black")
    # Numerical solution using shooting method
    optimal_guess = find_optimal_guess()
    x_num = shooting_method(optimal_guess)
    plt.plot(np.linspace(0, t_max, num_steps), x_num, label="Numerical Solution", linestyle="-", linewidth=2)
    # Candidate solutions
    for i in range(5):
        guess = np.random.uniform(-5, 5)  # Random guess within range
        x_candidate = shooting_method(guess)
        plt.plot(np.linspace(0, t_max, num_steps), x_candidate, label=f"Candidate Solution {i+1}", linestyle="-", linewidth=1)
    plt.title("Boundary Value Problem: Shooting Method")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot results
plot_results()





