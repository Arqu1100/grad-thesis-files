import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Energy range
energy = np.linspace(-15, 15, 200)
sigma_Constant = 1.5
delta_E = np.diff(energy)[0]

# Define functions
def signal(E, sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-(E**2 / (2*sigma**2)))

def kernel(E, sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((E)**2 / (2*sigma**2)))

def shifted_kernel(E, sigma, shift):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((E-shift)**2 / (2*sigma**2)))

# Compute signal and kernel
signal_vals = signal(energy, sigma_Constant)
kernel_vals = kernel(energy, sigma_Constant)

# Convolution
conv = np.convolve(signal_vals, kernel_vals, mode='same') * delta_E
conv_energy = energy

# Define the shifts we’ll visualize
shift_values = [-4, -2, 0, 2]
area_scatter = []

# --- Create Grid Layout (2x2 above, 1x2 below) ---
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1, 1, 0.8])

# Create axes for the four product plots
axes_products = [fig.add_subplot(gs[i//2, i%2]) for i in range(4)]

# Create axis for convolution (spans bottom row)
ax_conv = fig.add_subplot(gs[2, :])

# --- Loop over shifts to create product plots ---
for i, shift_value in enumerate(shift_values):
    ax = axes_products[i]

    # Shifted kernel and product
    kernel_shift = shifted_kernel(energy, sigma_Constant, shift_value)
    product = signal_vals * kernel_shift
    area = np.trapz(product, energy)
    area_scatter.append(area)

    # Plot signal, shifted kernel, and product
    ax.plot(energy, signal_vals, label='Signal', linestyle="--")
    ax.plot(energy, kernel_shift, label=f'Kernel (shift={shift_value})', color = 'red', linestyle=":")
    ax.plot(energy, product, color='black', label='Product')
    ax.fill_between(energy, product, color='yellow', alpha=0.3,
                    label=f'Area = {area:.4f}')
    ax.set_xlim(-10,10)
    ax.set_title(f'Shift = {shift_value}')
    ax.set_xlabel('Epsilon')
    ax.set_ylabel('Amplitude')
    ax.legend(fontsize=8)
    ax.grid(True)

# --- Convolution plot ---
ax_conv.plot(conv_energy, conv, color='black', label='Convolved Signal')
ax_conv.plot(conv_energy, signal_vals, color='red', label='Signal', linestyle="--")
ax_conv.scatter(shift_values, area_scatter, color='blue', s=80, zorder=5,
                label='Points of intergral product')
ax_conv.set_title('Convolution of Signal and Kernel')
ax_conv.set_xlabel('Energy')
ax_conv.set_ylabel('Amplitude')
ax_conv.set_xlim(-10,10)
ax_conv.legend()
ax_conv.grid(True)

plt.tight_layout()
plt.show()
