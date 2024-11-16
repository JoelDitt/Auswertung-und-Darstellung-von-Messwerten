import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Daten
auslenkwinkel_rad = np.array([0.0000, 0.7854, 1.5708, 2.3562, 3.1416, 3.9270, 4.7124, 5.4978, 6.2832])
drehmoment = np.array([0, 0.0239055, 0.047811, 0.06773225, 0.0876535, 0.111559, 0.13148025, 0.15937, 0.1832755])

# Lineare Regression
slope, intercept, r_value, p_value, std_err = linregress(auslenkwinkel_rad, drehmoment)
regressions_gerade = slope * auslenkwinkel_rad + intercept

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Messpunkte ohne Fehlerbalken
ax.plot(auslenkwinkel_rad, drehmoment, 'o', color='red', label='Messwerte')

# Regressionsgerade
ax.plot(auslenkwinkel_rad, regressions_gerade, color='blue', label=f'Regressionsgerade: $M = {slope:.4f} \cdot \phi + {intercept:.4f}$')

# Achsenbeschriftungen und Titel
ax.set_xlabel(r'Auslenkwinkel $\phi$ (rad)', fontsize=18)
ax.set_ylabel(r'Drehmoment $M$ (Nm)', fontsize=18)
ax.set_title('Drehmoment in Abh„ngigkeit vom Auslenkwinkel', fontsize=20)
ax.legend(fontsize=18)

# Gitter und Layout
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Plot anzeigen
plt.show()
