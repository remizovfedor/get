import matplotlib.pyplot as plt

numbers = [256, 255, 127, 64, 32, 5, 0]
voltages = [0.0, 3.258, 1.678, 0.869, 0.459, 0.1143, 0.01]

plt.plot(numbers, voltages)
plt.show()