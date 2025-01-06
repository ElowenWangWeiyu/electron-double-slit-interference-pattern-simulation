# Double-Slit Interference of Electrons Simulation
This repository contains a Python simulation of the double-slit interference pattern of electrons using the principles of quantum mechanics. The simulation models electron behavior as quantum states and visualises the resulting interference pattern on a detection screen. The electron's wavefunction is computed as a superposition of wavefunctions passing through two slits, creating the characteristic interference effect.

## Features

- Electron as a Quantum State: The electron is represented by a quantum state as a superposition of two slits, using a Gaussian-like wavefunction for each slit.
- Wavefunction Interference: The simulation calculates the interference pattern on a detection screen by combining the contributions of both slits.
- Normalisation: The simulation ensures the probability distribution is normalised so that the sum of probabilities across the screen is 1.
- Visualisation: It generates a plot showing the probability distribution of detecting the electron at different positions on the screen.

## How to Use

- Clone the repository to your local machine.
- Install the required dependencies: pip install numpy matplotlib qutip
- Run the script: double slit interference pattern simulation.py

## Customisation

You can modify the simulation parameters in double slit interference pattern simulation.py:
- num_screen_points: The number of points on the detection screen (higher values will result in smoother plots).
- screen_range: The range of positions on the detection screen (arbitrary units).
- slit_separation: The separation between the two slits (arbitrary units).
- slit_width: The width of each slit (controls the diffraction width).
- electron_momentum: The momentum of the electron (affects the de Broglie wavelength and the interference pattern).

## Expected Output

Here is the expected output with the parameters in the script. The output will be different with customised simulation parameters of your choice.
![Expected Output](electron%20double%20slit%20interference%20pattern%20expected%20output.png)

## Dependencies

- Python 3.x
- `matplotlib`
- `numpy`
- `qutip`

## License

This project is licensed under MIT License.
