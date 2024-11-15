import sympy as sp

# Definiere die Symbole fr die Variablen und ihre Unsicherheiten
L_stange, m_stange, L_koerper, m_koerper = sp.symbols('L_stange m_stange L_koerper m_koerper')
delta_L_stange, delta_m_stange, delta_L_koerper, delta_m_koerper = sp.symbols('delta_L_stange delta_m_stange delta_L_koerper delta_m_koerper')

#Formel fr r_eff
r_eff = ((m_koerper*L_koerper)+(m_stange*L_stange))/(m_koerper+m_stange)

# Berechne die partiellen Ableitungen
partial_L_stange = sp.diff(r_eff, L_stange)
partial_m_stange = sp.diff(r_eff, m_stange)
partial_L_koerper = sp.diff(r_eff, L_koerper)
partial_m_koerper = sp.diff(r_eff, m_koerper)

# Ausdruck fr das totale Differential
delta_r_eff = (sp.Abs(partial_L_stange) * delta_L_stange +
               sp.Abs(partial_m_stange) * delta_m_stange +
               sp.Abs(partial_L_koerper) * delta_L_koerper +
               sp.Abs(partial_m_koerper) * delta_m_koerper)

# Anzeige der Formel fr das totale Differential
print("Formel fr die Unsicherheit in r_eff:")
print(delta_r_eff)

# Funktion zur Berechnung der Unsicherheit in r_eff basierend auf gegebenen Werten
def berechne_unsicherheit(L_stange_wert, m_stange_wert, L_koerper_wert, m_koerper_wert,
                          delta_L_stange_wert, delta_m_stange_wert, delta_L_koerper_wert, delta_m_koerper_wert):
    # Setze die Werte fr die Variablen und Unsicherheiten in das totale Differential ein
    return delta_r_eff.subs({
        L_stange: L_stange_wert,
        m_stange: m_stange_wert,
        L_koerper: L_koerper_wert,
        m_koerper: m_koerper_wert,
        delta_L_stange: delta_L_stange_wert,
        delta_m_stange: delta_m_stange_wert,
        delta_L_koerper: delta_L_koerper_wert,
        delta_m_koerper: delta_m_koerper_wert
    })

#Werte fr die Messungen und ihre Unsicherheiten
L_stange_wert = 96.15/1000         # L„nge bis zum Mittelpunkt der Stange in mm
m_stange_wert = 18.9/1000          # Masse der Stange in g
L_koerper_wert = 60.74/1000        # L„nge bis zum Mittelpunkt des K”rpers in mm
m_koerper_wert = 499.7/1000        # Masse des K”rpers in g

delta_L_stange_wert = 0.005/1000    # Unsicherheit der L„nge der Stange in mm
delta_m_stange_wert = 0.1/1000     # Unsicherheit der Masse der Stange in g
delta_L_koerper_wert = 0.015/1000   # Unsicherheit der L„nge des K”rpers in mm
delta_m_koerper_wert = 0.1/1000    # Unsicherheit der Masse des K”rpers in g

# Berechne die Unsicherheit in r_eff
unsicherheit_r_eff = berechne_unsicherheit(
    L_stange_wert, m_stange_wert, L_koerper_wert, m_koerper_wert,
    delta_L_stange_wert, delta_m_stange_wert, delta_L_koerper_wert, delta_m_koerper_wert
)

print(f"Die berechnete Unsicherheit in r_eff betr„gt: {unsicherheit_r_eff*1000} mm")

