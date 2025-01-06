import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

# Parameters
num_screen_points = 500
screen_range = (-5, 5)   # Screen positions (arbitrary units)
slit_separation = 2      # Separation between slits (arbitrary units)
slit_width = 0.5         # Width of the slits (arbitrary units)
electron_momentum = 1.0  # Momentum of the electron (arbitrary units)
h_bar = 1.0              # Reduced Planck's constant (set to 1 for simplicity)

# de Broglie wavelength of the electron (λ = h / p)
wavelength = h_bar / electron_momentum

# Define the screen positions (detection screen)
screen_coords = np.linspace(screen_range[0], screen_range[1], num_screen_points)

# Slit positions (arbitrary units, assuming slits are at -1 and +1)
slit_A_position = -slit_separation / 2
slit_B_position = slit_separation / 2

# Quantum state for the two slits (represented by position basis states)
state_A = qt.fock(2, 0)  # Slit A as a quantum state (position 0)
state_B = qt.fock(2, 1)  # Slit B as a quantum state (position 1)

# Superposition of states |A> and |B> (superposition principle)
alpha = 1 / np.sqrt(2)  # Normalisation coefficient for slit A
beta = 1 / np.sqrt(2)   # Normalisation coefficient for slit B

# Superposition state
superposition_state = alpha * state_A + beta * state_B

# Define Gaussian-like wavefunctions for each slit
slit_A_wave = np.exp(-((screen_coords - slit_A_position) ** 2) / slit_width)
slit_B_wave = np.exp(-((screen_coords - slit_B_position) ** 2) / slit_width)

# Quantum wavefunction resulting from the superposition
wavefunction = alpha * slit_A_wave + beta * slit_B_wave

# Compute the probability distribution (square of the wavefunction's magnitude)
probabilities = np.abs(wavefunction) ** 2

# Normalize the probabilities (this ensures they sum to 1)
probabilities /= np.sum(probabilities)

# Plot the interference pattern
plt.figure(figsize=(8, 6))
plt.plot(screen_coords, probabilities, label="Electron Interference Pattern", color='b')
plt.xlabel("Screen Position (arbitrary units)", fontsize=12)
plt.ylabel("Probability", fontsize=12)
plt.title("Electron Double-Slit Interference Pattern", fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
