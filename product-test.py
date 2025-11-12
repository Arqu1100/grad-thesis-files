import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Energy range
energy = np.linspace(-15, 15, 200)
sigma_Constant = 0.4
delta_E = np.diff(energy)[0]

# Define functions
def signal(E, sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-(E**2 / (2*sigma**2)))

def kernel(E, sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((E)**2 / (2*sigma**2)))

product_signal = signal(energy, sigma_Constant) * kernel(energy, sigma_Constant)

area = np.trapz(signal(energy, sigma_Constant), energy)
print(area)
plt.plot(energy, product_signal)
plt.grid()
plt.show()