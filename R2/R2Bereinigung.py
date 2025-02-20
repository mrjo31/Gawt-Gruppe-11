import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv('data-2.csv', sep=',', header=0)

# Spaltennamen zusammenführen und umbenennen
df.columns = ['Jahr', 'Lebendgeborene (Anzahl) Insgesamt']

# Nach der Korrektur: Spaltennamen überprüfen
print("Aktuelle Spaltennamen:", df.columns)

# Spalten in numerische Werte umwandeln, ungültige Einträge werden NaN
df['Jahr'] = pd.to_numeric(df['Jahr'], errors='coerce')
df['Lebendgeborene (Anzahl) Insgesamt'] = pd.to_numeric(df['Lebendgeborene (Anzahl) Insgesamt'], errors='coerce')

# NaN-Werte entfernen
df = df.dropna()

# Werte filtern: Sinnvolle Jahreszahlen und positive Geburtenzahlen
#df = df[(df['Jahr'] >= 1900) & (df['Jahr'] <= 2025)]
#df = df[df['Lebendgeborene (Anzahl) Insgesamt'] > 0]

# Bereinigte Daten speichern
df.to_csv('bereinigte_datei.csv', index=False)

print("Bereinigung abgeschlossen. Ergebnisse gespeichert in 'bereinigte_datei.csv'")
