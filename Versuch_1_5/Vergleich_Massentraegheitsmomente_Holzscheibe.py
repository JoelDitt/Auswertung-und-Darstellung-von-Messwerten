import numpy as np
import matplotlib.pyplot as plt

# Werte der Tr�gheitsmomente und Unsicherheiten
werte = np.array([
    0.002458959,  # J mit D_dyn
    0.002436356,  # J mit D_stat
    0.00247493   # J mit Definitionsgleichung
])

unsicherheiten = np.array([
    0.00084294,  # Unsicherheit f�r J mit D_dyn
    0.00074517,  # Unsicherheit f�r J mit D_stat
    0.0          # Unsicherheit f�r J (angenommen keine)
])

# Beschriftung der Balken
# Beschriftung der Balken mit korrekten Indizes
labels = [
    r'$J \, \text{mit} \, D_\text{dyn}^*$', 
    r'$J \, \text{mit} \, D_\text{stat}^*$', 
    r'$J \, \text{mit Definitionsgleichung}$'
]

# Position der Balken auf der X-Achse
x = np.arange(len(werte))

# Erstelle das Balkendiagramm
fig, ax = plt.subplots(figsize=(10, 6))
bar = ax.bar(x, werte, yerr=unsicherheiten, capsize=5, color=['blue', 'green', 'orange'], alpha=0.8)

# Beschriftungen und Titel
ax.set_xlabel('Berechnungsmethode', fontsize=15)
ax.set_ylabel(r'Massentr�gheitsmoment $J$ in $\mathrm{kg \cdot m^2}$', fontsize=15)
ax.set_title('Vergleich der berechneten Massentr�gheitsmomente', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Werte auf den Balken anzeigen
for i, v in enumerate(werte):
    ax.text(i, v + 0.00005, f'{v:.6f}', ha='center', va='bottom', fontsize=10)

# Layout anpassen und Plot anzeigen
plt.tight_layout()
plt.show()
