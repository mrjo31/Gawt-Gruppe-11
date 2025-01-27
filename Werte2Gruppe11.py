import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei im aktuellen Ordner einlesen
data = pd.read_csv('Datensatz_4_Beschleunigung_2.csv', delimiter=';', skipinitialspace=True)

# Median der relevanten Spalte berechnen und ausgeben
median_value = data['Absolute Beschleunigung (m/s^2)'].median()
print(f"Median: {median_value}")


modus = data['Absolute Beschleunigung (m/s^2)'].mode()
print(f"Modus:\n{modus}")

mean = data['Absolute Beschleunigung (m/s^2)'].mean()
print(f"Aritmethischer Mittelwert: {mean}")

varianz_stich = data['Absolute Beschleunigung (m/s^2)'].var()
print(f"Stichprobenvarianz: {varianz_stich}")

# Spannweite
Spannweite = data['Absolute Beschleunigung (m/s^2)'].max() - data['Absolute Beschleunigung (m/s^2)'].min()
print(f"Spannweite: {Spannweite}")

# Variationskoeffizient
variationskoeffizient = data['Absolute Beschleunigung (m/s^2)'].std() / data['Absolute Beschleunigung (m/s^2)'].mean()
print(f"variationskoeffizient: {variationskoeffizient}")

# Mittlere Abweichung vom Median
mit_vom_median = (data['Absolute Beschleunigung (m/s^2)'] - data['Absolute Beschleunigung (m/s^2)'].median()).abs().mean()
print(f" Mittlere Abweichung vom Median: {mit_vom_median}")


# Quartile berechnen
quartile = {
    'Q1': data['Absolute Beschleunigung (m/s^2)'].quantile(0.25),
    'Q2 (Median)': data['Absolute Beschleunigung (m/s^2)'].quantile(0.5),
    'Q3': data['Absolute Beschleunigung (m/s^2)'].quantile(0.75)
}
print(f" Quartile: {quartile}")


# Dezile berechnen
dezile = {f'D{i}': data['Absolute Beschleunigung (m/s^2)'].quantile(i * 0.1) for i in range(1, 10)}
print(f" Dezile: {dezile}")



# Quartilsabstand (R_Q0.5) berechnen
quartil_abstand = quartile['Q3'] - quartile['Q1']
print(f" Quartilsabstand: {quartil_abstand}")









plt.figure(figsize=(8, 6))
data['Absolute Beschleunigung (m/s^2)'].plot(kind='box', vert=False, grid=True)
plt.title('Box-Whisker-Plot der Beschleunigungswerte')
plt.xlabel('Absolute Beschleunigung (m/s^2)')
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(data['Time (s)'], data['Absolute Beschleunigung (m/s^2)'], alpha=0.7)
plt.title('Scatterplot der Beschleunigungswerte über die Zeit')
plt.xlabel('Zeit (s)')
plt.ylabel('Absolute Beschleunigung (m/s^2)')
plt.grid(True)
plt.show()

