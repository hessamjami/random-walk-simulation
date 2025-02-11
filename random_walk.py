import numpy as np
import matplotlib.pyplot as plt

# Parameters
steps = 1000  # Number of steps
x, y = [0], [0]  # Start at origin

# Random Walk Process
for _ in range(steps):
    angle = np.random.uniform(0, 2 * np.pi)  # Random direction
    x.append(x[-1] + np.cos(angle))
    y.append(y[-1] + np.sin(angle))

# Plot the Random Walk
plt.figure(figsize=(8, 8))
plt.plot(x, y, linestyle="-", marker="", alpha=0.7, color="blue")
plt.scatter(x[0], y[0], color="red", label="Start")
plt.scatter(x[-1], y[-1], color="green", label="End")
plt.legend()
plt.title("2D Random Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()
