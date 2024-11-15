import sympy as sp

# Definiere die Symbole fr die Variablen und ihre Unsicherheiten
m_gesamt, r_eff, d_feder, omega = sp.symbols('m_gesamt r_eff d_feder omega')
delta_m_gesamt, delta_r_eff, delta_d_feder, delta_omega = sp.symbols('delta_m_gesamt delta_r_eff delta_d_feder delta_omega')

# Berechne den tats„chlichen Radius inkl. Durchbiegung der Feder
r = r_eff + d_feder

# Formel fr die Zentripetalkraft (F_z = m_gesamt * omega^2 * r)
F_zentripetal = m_gesamt * omega**2 * r

# Berechne die partiellen Ableitungen
partial_m_gesamt = sp.diff(F_zentripetal, m_gesamt)
partial_r_eff = sp.diff(F_zentripetal, r_eff)
partial_omega = sp.diff(F_zentripetal, omega)

# Ausdruck fr das totale Differential
delta_F_zentripetal = (sp.Abs(partial_m_gesamt) * delta_m_gesamt +
                       sp.Abs(partial_r_eff) * delta_r_eff +
                       sp.Abs(partial_omega) * delta_omega)

# Anzeige der Formel fr das totale Differential
print("Formel fr die Unsicherheit in der Zentripetalkraft:")
print(delta_F_zentripetal)

# Funktion zur Berechnung der Unsicherheit in der Zentripetalkraft basierend auf gegebenen Werten
def berechne_unsicherheit(m_gesamt_wert, r_eff_wert, d_feder_wert, omega_wert,
                          delta_m_gesamt_wert, delta_r_eff_wert, delta_omega_wert):
    # Setze die Werte fr die Variablen und Unsicherheiten in das totale Differential ein
    return delta_F_zentripetal.subs({
        m_gesamt: m_gesamt_wert,
        r_eff: r_eff_wert,
        d_feder: d_feder_wert,
        omega: omega_wert,
        delta_m_gesamt: delta_m_gesamt_wert,
        delta_r_eff: delta_r_eff_wert,
        delta_omega: delta_omega_wert
    })

#Werte fr die Messungen und ihre Unsicherheiten
m_gesamt_wert = 518.6/1000            # Masse des K”rpers in kg
r_eff_wert = 121.722769/1000           # Effektiver Radius in m
d_feder_wert = 2.4835/1000             # Durchbiegung der Feder in m
omega_wert =   7.621525118             # Winkelgeschwindigkeit in rad/s

delta_m_gesamt_wert = 0.2/1000       # Unsicherheit der Masse des K”rpers in kg
delta_r_eff_wert = 0.019753182/1000    # Unsicherheit des effektiven Radius in m
delta_omega_wert = 0.316421989         # Unsicherheit der Winkelgeschwindigkeit in rad/s

# Berechne die Unsicherheit in der Zentripetalkraft
unsicherheit_F_zentripetal = berechne_unsicherheit(
    m_gesamt_wert, r_eff_wert, d_feder_wert, omega_wert,
    delta_m_gesamt_wert, delta_r_eff_wert, delta_omega_wert
)

print(f"Die berechnete Unsicherheit in der Zentripetalkraft betr„gt: {unsicherheit_F_zentripetal:.10f} N")
