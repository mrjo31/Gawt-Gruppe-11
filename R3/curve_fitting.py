import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Daten laden
df = pd.read_csv('merged_data.csv')

# Daten bereinigen
x_data = pd.to_numeric(df['Year'], errors='coerce')
y_data = pd.to_numeric(df['Deceased'], errors='coerce')
df = df.dropna(subset=['Year', 'Deceased'])

# Daten normalisieren
x_data_normalized = x_data - x_data.min()

# Daten plotten
plt.scatter(x_data, y_data, label="Daten")
plt.xlabel("Year")
plt.ylabel("Deceased")
plt.legend()
plt.show()

# Modellfunktion
def model_function(x, a, b, c, d):
    return (a*x**3+b*x**2+c*x+d)

# Curve Fitting
params, covariance = curve_fit(model_function, x_data_normalized, y_data)
print("Angepasste Parameter:", params)
print("Angepaste Funktion: ",params[0],'*x^3 + ',params[1],'*x^2 + ',params[2],'*x + ',params[3])

# Angepasste Kurve berechnen
fitted_y = model_function(x_data_normalized, *params)

# Plotten der Daten und der angepassten Kurve
plt.scatter(x_data, y_data, label="Daten")
plt.plot(x_data, fitted_y, color="red", label="Angepasste Kurve")
plt.xlabel("Year")
plt.ylabel("Deceased")
plt.legend()
plt.show()