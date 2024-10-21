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

# Berechne Mittelwert und Standardabweichung
mu = np.mean(N_i)
sigma = np.std(N_i, ddof=1)

# Sortiere die Messwerte
sorted_N_i = np.sort(N_i)

# Berechne die empirische kumulative HÑufigkeitsverteilung (Summenverteilung)
cumulative_frequency = np.arange(1, n + 1) / n  # Summenverteilung (CDF)

# Berechne die theoretische Gau·sche Verteilungsfunktion W(N)
x_gauss = np.linspace(mu-250,mu+250, 1000)  # Wertebereich
cdf_gauss = norm.cdf(x_gauss, mu, sigma)  # Gau·sche CDF

# HinzufÅgen der Linien
plt.axhline(y=0.5, color='blue',alpha=0.7, linestyle='-', label=r'Erwartungswert $\mu$')
plt.axhline(y=0.84132, color='blue',alpha=0.7, linestyle='--', label=r'$\mu\pm\sigma$')
plt.axhline(y=0.5-0.34132, color='blue',alpha=0.7, linestyle='--')
plt.axvline(x=mu, color='blue',alpha=0.7, linestyle='-')
plt.axvline(x=mu + sigma, color='blue',alpha=0.7, linestyle='--')
plt.axvline(x=mu - sigma, color='blue',alpha=0.7, linestyle='--')

# Beschriftungen hinzufÅgen und leicht verschieben
plt.text(mu, -0.1, r'$\mu$', color='blue', fontsize=15, ha='center', va='bottom')
plt.text(mu + sigma, -0.1, r'$\mu + \sigma$', color='blue', fontsize=15, ha='center', va='bottom')
plt.text(mu - sigma, -0.1, r'$\mu - \sigma$', color='blue', fontsize=15, ha='center', va='bottom')
plt.text(3950, 0.5, '50%', color='blue', fontsize=15, ha='right', va='center')
plt.text(3950, 0.84132, '84%', color='blue', fontsize=15, ha='right', va='center')
plt.text(3950, 0.15868, '16%', color='blue', fontsize=15, ha='right', va='center')

# Plot der gemessenen Summenverteilung
plt.step(sorted_N_i, cumulative_frequency, where='post', label='Gemessene Summenverteilung', color='red')

# Plot der theoretischen Gau·schen Verteilungsfunktion
plt.plot(x_gauss, cdf_gauss, label=rf'$W(N, \mu={mu:.2f}, \sigma={sigma:.2f})$'.replace('.', ','), color='blue')

# Raster und Titel
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Titel und Achsenbeschriftungen mit angepasster Schriftgrî·e
plt.title('Vergleich der gemessenen Summenverteilung mit der Gau·schen Verteilungsfunktion', fontsize=35)
plt.xlabel(r'$N_\text{i} \, \text{ in Impulsen pro 12s}$', fontsize=25)
plt.ylabel('Kummulierte HÑufigkeit', fontsize=25)

# Anpassung der Schriftgrî·e der Ticks
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Legende mit angepasster Schriftgrî·e
plt.legend(fontsize=25)

plt.xlim([3950,4250])

# Zeige den Plot an
plt.show()
