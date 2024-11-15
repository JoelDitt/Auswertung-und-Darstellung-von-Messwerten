import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Messwerte
N_i = np.array([
    3996, 4012, 4039, 4018, 4069, 4038, 3993, 3974, 3991, 4056,
    3999, 3996, 4040, 4130, 4073, 4170, 3990, 4059, 4032, 4072,
    4075, 3956, 4051, 4124, 3989, 4005, 4075, 4097, 4031, 4125,
    4077, 4042, 4140, 4071, 4146, 4058, 4048, 3996, 4086, 3997,
    4082, 4051, 4046, 4115, 4055, 4084, 4119, 4025, 4090, 4037,
    4111, 4042, 4067, 4008, 4030, 4120, 4085, 4035, 3985, 3995,
    4163, 4053, 3995, 4072, 4224, 3989, 4066, 3974, 4025, 3993,
    4097, 4048, 4045, 4050, 4020, 4012, 4128, 4127, 3979, 3972,
    4080, 4056, 4027, 4016, 4086, 4027, 4057, 4038, 4025, 4076,
    4090, 4126, 3999, 4081, 3980, 4026, 4036, 4017, 4082, 4089
])

# Anzahl der Messwerte und Klassen
n = len(N_i)
k = int(np.sqrt(n))  # Anzahl der Klassen

# Mittelwert und Standardabweichung
mu = np.mean(N_i)
sigma = np.std(N_i, ddof=1)

# Setzen der Klassenbreite
delta_N_K = 38    # int(6 / k * sigma)   Berechnung der Klassenbreite

# Berechnung der Bin-Grenzen basierend auf der Klassenbreite
bin_edges = np.array([3899.64, 3937.64, 3975.64, 4013.64, 4051.64, 4089.64, 4127.64, 4165.64, 4203.64, 4241.64])

# Histogramm der absoluten HÑufigkeit
hist_values, _ = np.histogram(N_i, bins=bin_edges)

# Berechnung der relativen HÑufigkeit
relative_frequency = (hist_values / n)

# Histogramm der relativen HÑufigkeiten
plt.bar(bin_edges[:-1], relative_frequency, width=delta_N_K, color=(1, 0, 0, 0), edgecolor='red', label='exp. Relative HÑufigkeitsverteilung')

# Gau·-Verteilung
range_width = 200  # Die Breite des Bereichs links und rechts vom Mittelwert
plt.xlim([mu - range_width, mu + range_width])  # Symmetrischer Bereich um den Mittelwert
x = np.linspace(mu - 2 * range_width, mu + 2 * range_width, 1000)  # Vergrî·erter x-Bereich fÅr die Gau·-Kurve
p = norm.pdf(x, mu, sigma) * delta_N_K  # Normierung auf Klassenbreite
plt.plot(x, p, 'k', linewidth=2, label=rf'$G(N_{{\mathrm{{i}}}}, \mu={mu:.2f}, \sigma={sigma:.2f}) \cdot \Delta N_{{\mathrm{{K}}}}$'.replace('.', ','))



# Blaue Linie bei Mittelwert
plt.axvline(mu, color='blue', linestyle='-', label=r'Erwartungswert $\mu$')

# Gestrichelte Linien bei Mittelwert +- Sigma
plt.axvline(mu + sigma, color='blue', linestyle='--', label=r'Standartabweichung $\sigma$')
plt.axvline(mu - sigma, color='blue', linestyle='--',)

# Raster hinzufÅgen
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Achsenbeschriftungen und Legende
plt.title('Histogramm der Messwerte $N_{{\mathrm{i}}}$ und Gau·-Verteilung', fontsize=35)
plt.xlabel(r'$N_\text{i} \, \text{ in Impulsen pro 12s}$', fontsize=25)  # Hier die Einheit fÅr N_i anpassen
plt.ylabel(r'$(dw/dN) \cdot \Delta N_\text{K}$', fontsize=25)
plt.xticks(fontsize=15)  # Schriftgrî·e der x-Achsenwerte
plt.yticks(fontsize=15)  # Schriftgrî·e der y-Achsenwerte
plt.legend(fontsize=25)
plt.show()