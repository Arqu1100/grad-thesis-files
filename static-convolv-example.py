import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

plt.style.use('standard.mplstyle')

# Energy range
energy = np.linspace(-15, 15, 200)
sigma_Constant = 1.5
delta_E = np.diff(energy)[0]

# Functions
def signal(E, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(E**2) / (2 * sigma**2))

def kernel(E, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(E**2) / (2 * sigma**2))

def shifted_kernel(E, sigma, shift):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((E - shift)**2) / (2 * sigma**2))

# Compute signal and kernel
signal_vals = signal(energy, sigma_Constant)
kernel_vals = kernel(energy, sigma_Constant)

# Convolution
conv = np.convolve(signal_vals, kernel_vals, mode='same') * delta_E
conv_energy = energy

# Shifts and products
shift_values = [-4, -2, 0, 2]
area_scatter = []
products = []

for shift_value in shift_values:
    kernel_shift = shifted_kernel(energy, sigma_Constant, shift_value)
    product = signal_vals * kernel_shift
    area = np.trapz(product, energy)
    products.append(product)
    area_scatter.append(area)

# --- Create one big 4x2 figure ---
fig, axes = plt.subplots(4, 2, figsize=(7, 9), sharey='col', sharex=True)
#fig.suptitle("Signal × Kernel Products and Convolved Signal", fontsize=16)

for i, shift_value in enumerate(shift_values):
    # --- Left column: product plots ---
    ax_left = axes[i, 0]
    kernel_shift = shifted_kernel(energy, sigma_Constant, shift_value)
    ax_left.plot(energy, signal_vals, linestyle="--", color='red')
    ax_left.plot(energy, kernel_shift, color='red', linestyle=":")
    ax_left.plot(energy, products[i], color='orange')
    
    # Fill and label area inside plot
    ax_left.fill_between(energy, products[i], color='yellow', alpha=0.3)
    max_product = max(products[i])
    ax_left.text(2.3, 0.185, f'Area = \n {area_scatter[i]:.2f}', color='black', fontsize=16)
    
    ax_left.set_xlim(-10, 10)
    ax_left.set_title(f'Shift = {shift_value}')
    ax_left.grid(True)

    # --- Right column: convolution + signal ---
    ax_right = axes[i, 1]
    ax_right.plot(conv_energy, conv, color='black')
    ax_right.plot(conv_energy, signal_vals, color='red', linestyle="--")
    
    # Scatter point and coordinates
    ax_right.scatter(shift_value, area_scatter[i], color='blue', s=80, zorder=5)
    ax_right.text(shift_value + 0.4, area_scatter[i],
                  f'({shift_value:.1f}, {area_scatter[i]:.3f})',
                  fontsize=16, color='blue')
    
    ax_right.set_xlim(-10, 10)
    ax_right.set_title(f'Convolution')
    ax_right.grid(True)

# Shared axis labels
fig.text(0.04, 0.5, 'Amplitude', va='center', rotation='vertical', fontsize=22)
fig.text(0.5, 0.04, 'Energy', ha='center', fontsize=22)

# --- Manual legend (without the point) ---
legend_elements = [
    Line2D([0], [0], color='orange', linestyle='--', label='Signal'),
    Line2D([0], [0], color='red', linestyle=':', label='Shifted Kernel'),
    Line2D([0], [0], color='orange', label='Product'),
    Line2D([0], [0], color='black', label='Convolved Signal')
]

fig.legend(handles=legend_elements, loc='outside upper right', frameon=True, mode='expand', ncols=4)

fig.tight_layout(rect=[0.06, 0.06, 0.95, 0.95])
plt.show()
