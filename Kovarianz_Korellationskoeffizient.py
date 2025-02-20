###Berechnet hier Kovarianz zwischen Prozentwerten und Daten

import pandas as pd

data = pd.read_csv('bereinigte_datei.csv',sep=',')
df = pd.DataFrame(data)

# Datumswerte in datetime-Format konvertieren
#df['DATE'] = pd.to_datetime(df['DATE'], format='%d.%m.%Y')

# Datumswerte in numerische Werte (z. B. Tage seit 2000) umwandeln
#df['DATE_numeric'] = (df['DATE'] - pd.Timestamp("2000-07-01")).dt.days


# Kovarianzmatrix berechnen
cov_matrix = df.cov()
print("Kovarianz zwischen X und Y:", cov_matrix.loc['Jahr','Lebendgeborene (Anzahl) Insgesamt'])

correlation = df['Jahr'].corr(df['Lebendgeborene (Anzahl) Insgesamt'])

print("Korellationskoeffizient: ",correlation)

"""Das Programm dient zu Berechnung der Kovarianz und des Korellationskoeffizienten der gegebenen Datensätze. Für den ersten
Datensatz musste das Datum vom Format TT.MM.JJJJ in einen numerischen Wert (Anzahl der Tage die seit dem ersten Datum vergangen
sind) umgerechnet werden, damit überhaupt ein Wert berechnet werden konnte. Für die restlichen Datensätze wurder die Befehle,
die auf den ersten Datensatz bezogen waren einfach auskommentiert."""
