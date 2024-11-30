import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Daten
g_values = np.array([25, 30, 35, 45, 50, 55])  # Gegenstandsweiten in cm
b_means = np.array([117.8833333, 64.78333333, 49.26666667, 37.21666667, 34.43333333, 32.31666667])  # Mittelwerte der Bildweiten in cm

# Berechnung der Inversen
g_inverse = 1 / g_values  # 1/g
b_inverse = 1 / b_means  # 1/b

# Lineare Regression
slope, intercept, r_value, p_value, std_err = linregress(g_inverse, b_inverse)

# Werte für den Plot generieren (erweiterter Bereich)
g_inverse_full = np.linspace(-0.02, max(g_inverse) + 0.02, 1000)  # Bereich stark erweitert
b_inverse_fit_full = slope * g_inverse_full + intercept

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Messpunkte
ax.plot(g_inverse, b_inverse, 'o', color='red', label=r'Messwerte $b^{-1}=f(g^{-1})$'
)

# Regressionsgerade
ax.plot(g_inverse_full, b_inverse_fit_full, color='blue', label=f'Regressionsgerade: $y = {slope:.4f}x + {intercept:.4f}$')

# Achsenbeschriftungen und Titel
ax.set_xlabel(r'g$^{-1}$ in cm$^{-1}$', fontsize=18)
ax.set_ylabel(r'b$^{-1}$ in cm$^{-1}$', fontsize=18)
ax.set_title('Lineare Darstellung zur Ermittlung der Brennweite $f$', fontsize=20)
ax.legend(fontsize=14)

# Achsen-Ticks anpassen
ax.tick_params(axis='both', labelsize=14)

# Achsenlimits erweitern
x_min, x_max = -0.02, max(g_inverse) + 0.02
y_min, y_max = min(b_inverse_fit_full), max(b_inverse_fit_full)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Gitter und Layout
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Plot anzeigen
plt.show()

# Brennweite berechnen
f_linear = 1 / intercept  # f = 1 / Achsenabschnitt
print(f"Brennweite (f): {f_linear:.2f} cm")

# Fehler des Achsenabschnitts
delta_b = std_err  # Unsicherheit des Achsenabschnitts (aus linregress)

# Fehler der Brennweite
delta_f = delta_b / intercept**2
print(f"Messfehler der grafischen Brennweite: {delta_f:.2f} cm")

