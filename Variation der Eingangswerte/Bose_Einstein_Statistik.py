import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Konstanten in eV
k_B_eV = 8.617e-5  # Boltzmann-Konstante in eV/K
mu_eV = 0.55       # Chemisches Potential (Fermi-Energie) in eV
E_eV = np.linspace(0.45, 0.8, 1000)  # Energie in eV
T_values = np.exp(np.linspace(np.log(3), np.log(450), 50))  # Temperaturbereich (K)

# Funktion für Bose-Einstein-Verteilung
def bose_einstein(E, T, mu, k_B):
    return 1 / (np.exp((E - mu) / (k_B * T)) - 1)

# Setup der Figur und Achsen
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlabel(r"Energy $\epsilon$ [eV]", fontsize=14)
ax.set_ylabel(r"$F(\epsilon)$", fontsize=14)
ax.set_xlim(0.525, 0.7)
ax.set_ylim(0, 1.5)
ax.grid(alpha=0.3)

# Passe das Layout an, um Platz für Achsenbeschriftungen zu schaffen
plt.subplots_adjust(bottom=0.2)

# Linie und Text für die Animation
line, = ax.plot([], [], color="dodgerblue", lw=2)
fill = None  # Placeholder für die Fläche
temp_text = ax.text(0.65, 1.25, "", ha="center", fontsize=14)

# Initialisierungsfunktion
def init():
    global fill
    line.set_data([], [])
    if fill:
        fill.remove()  # Entferne alte Fläche, falls vorhanden
    temp_text.set_text("")
    return line, temp_text

# Update-Funktion für die Animation
def update(frame):
    global fill
    T = frame  # Aktuelle Temperatur
    y = bose_einstein(E_eV, T, mu_eV, k_B_eV)
    line.set_data(E_eV, y)
    if fill:
        fill.remove()  # Entferne alte Fläche
    fill = ax.fill_between(E_eV, 0, y, color="dodgerblue", alpha=0.3)  # Aktualisiere Fläche
    temp_text.set_text(r"$T = {:.1f} \, \mathrm{{K}}$".format(T))
    return line, temp_text, fill

# Animation erstellen
ani = FuncAnimation(fig, update, frames=np.concatenate([T_values, T_values[::-1]]),
                    init_func=init, blit=False, interval=100)

# Speichern als GIF
gif_path = "bose_einstein_temperature_variation_adjusted.gif"
ani.save(gif_path, writer="pillow", fps=10)

print(f"Animation wurde erfolgreich gespeichert unter: {gif_path}")
