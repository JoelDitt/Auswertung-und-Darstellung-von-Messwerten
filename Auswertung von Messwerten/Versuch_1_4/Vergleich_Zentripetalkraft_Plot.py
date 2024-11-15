import numpy as np
import matplotlib.pyplot as plt

# Werte fr die eingestellte und berechnete Zentripetalkraft
eingestellte_kraft = np.array([
    2.03, 3, 3.985
])

berechnete_kraft = np.array([
    1.856, 2.737, 3.741
])

# Messunsicherheiten fr die eingestellte und berechnete Zentripetalkraft
unsicherheit_eingestellt = np.array([
    0.1556, 0.143955659, 0.1278             # Werte fr die Unsicherheiten der eingestellten Kraft
])

unsicherheit_berechnet = np.array([
    0.131985137, 0.196803115, 0.312694717   # Werte fr die Unsicherheiten der berechneten Kraft
])

# šberprfe, ob die Anzahl der Messwerte bereinstimmt
assert len(eingestellte_kraft) == len(berechnete_kraft) == len(unsicherheit_eingestellt) == len(unsicherheit_berechnet), \
    "Die Anzahl der Messwerte und Unsicherheiten muss bereinstimmen."

# Erstelle den Balken-Plot
x = np.arange(len(eingestellte_kraft))  # X-Achse (Messpunkte)

# Balkenbreite fr jeden Typ von Zentripetalkraft
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# Balken fr eingestellte und berechnete Zentripetalkraft mit Fehlerbalken
bar1 = ax.bar(x - width/2, eingestellte_kraft, width, label='Eingestellte Zentripetalkraft', color='red', yerr=unsicherheit_eingestellt, capsize=100)
bar2 = ax.bar(x + width/2, berechnete_kraft, width, label='Berechnete Zentripetalkraft', color='blue', yerr=unsicherheit_berechnet, capsize=100)

# Beschriftungen und Titel
ax.set_xlabel('Nummer der Messung', fontsize=15)
ax.set_ylabel(r'Zentripetalkraft $F_\text{ZP}$ in N', fontsize=15)
ax.set_title('Vergleich der Zentripetalkraft von Messreihe 1', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels([f'{i+1}' for i in x], fontsize=12)  # Messpunkte-Beschriftung
ax.legend(loc='upper left', fontsize=18)  # Legende oben links platzieren

ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))  # Raster alle 0.5 N

# Grid und Layout
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Plot anzeigen
plt.show()
