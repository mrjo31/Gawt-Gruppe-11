"""Der vorliegende Code ist eine Funktion, welche als Parameter den Namen einer .csv Datei, sowie einen Spaltennamen annimmt. Für die gegebene Funktion
werden dann sämtliche Werte berechnet, die im Lastenheft gewünscht sind und in eine Liste eingetragen, welche mit dem return-Befehl ausgegeben wird.
Durch den Befehl result = descriptive_values(...) [...] print(i) werden besagte Werte in der Konsole ausgegeben und sind leicht ablesbar. Der Sinn dahinter ist,
dass man für beliebige Datensätze sehr schnell alle Werte berechnen kann, ohne irgendwelche Befehle unnötig oft eingeben zu müssen. Des weiteren Kann man mit "val" 
auch angeben ob die eingegebene Spalte sortiert werden soll sowie mit file, ob die sortierte Liste als neue Datei gespeichert werden soll oder nicht, was sich 
bei der Sortierung der Listen bezahlt gemacht hat. Outputname ist dementsprechend der Name der neuen, sortierten Liste.
Der Spearman-Rangkorrelationskoeffizient wurde nachträglich hinzugefügt und ist somit nicht in der Funktion, weshalb er einzeln aufgerufen werden muss."""


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

def descriptive_values(filename, column_name, val=False, file=False, outputname=None):
    """
    Funktion zur Berechnung verschiedener statistischer Kennzahlen, einschließlich Quartilen, Dezilen und Quartilsabstand.

    Parameter:
        filename (str): Pfad zur CSV-Datei.
        column_name (str): Name der Spalte, die analysiert werden soll.
        val (bool): Ob die Daten sortiert analysiert werden sollen.
        file (bool): Ob die Daten in eine neue Datei gespeichert werden sollen.
        outputname (str): Name der Ausgabedatei (falls file=True).

    Rückgabewerte:
        list: Eine Liste mit den berechneten Werten.
    """
    # Daten einlesen
    df = pd.read_csv(filename, sep=',')

    if val:  # Sortieren der Daten nach der angegebenen Spalte
        df = df.sort_values(by=column_name)

    # Mittelwert
    mean = df[column_name].mean()

    # Median
    median = df[column_name].median()

    # Modus
    mode = df[column_name].mode().tolist()  # Gibt eine Liste der häufigsten Werte zurück

    # Spannweite
    value_range = df[column_name].max() - df[column_name].min()

    # Stichprobenvarianz berechnen
    sample_variance = df[column_name].var(ddof=1)

    # Variationskoeffizient
    variation_coefficient = df[column_name].std(ddof=1) / df[column_name].mean()

    # Mittlere Abweichung vom Median
    mad_from_median = (df[column_name] - df[column_name].median()).abs().mean()

    # Quartile berechnen
    quartile = {
        'Q1': df[column_name].quantile(0.25),
        'Q2 (Median)': df[column_name].quantile(0.5),
        'Q3': df[column_name].quantile(0.75)
    }

    # Dezile berechnen
    dezile = {f'D{i}': df[column_name].quantile(i * 0.1) for i in range(1, 10)}

    # Quartilsabstand (R_Q0.5) berechnen
    quartile_range = quartile['Q3'] - quartile['Q1']

    # Optional: Ergebnisse in eine Datei schreiben
    if file:
        df.to_csv(outputname, index=False)

    # Ergebnisse anzeigen
    if val:
        print("Werte für sortierte Liste:\n")
    else:
        print("Werte für unsortierte Liste:\n")

    values = [
        "mean:", mean,
        "median:", median,
        "mode:", mode,
        "range:", value_range,
        "sample_variance:", sample_variance,
        "variation_coefficient:", variation_coefficient,
        "mad_from_median:", mad_from_median,
        "quartile:", quartile,
        "quartile_range (R_Q0.5):", quartile_range,
        "dezile:", dezile
    ]
    return values

def calculate_spearman_from_csv(file_path):
    """
    Berechnet den Spearman-Rangkorrelationskoeffizienten aus einer CSV-Datei.

    :param file_path: Pfad zur CSV-Datei.
    :return: Spearman-Koeffizient.
    """
    data = pd.read_csv(file_path, sep=',')
    coefficient, _ = spearmanr(data.iloc[:, 0], data.iloc[:, 1])
    return coefficient

############### Hauptprogramm ################

# Beispiel für die unsortierte Liste
result = descriptive_values('data-1.csv', 'Percent change from a year ago', val=False)
for i in result:
    print(i)

# Beispiel für die sortierte Liste
result_sorted = descriptive_values('data-1.csv', 'Percent change from a year ago', val=True)
for i in result_sorted:
    print(i)

# Berechnung des Spearman-Rangkorrelationskoeffizienten
spearman_coeff = calculate_spearman_from_csv('data-1.csv')
print(f"Spearman-Rangkorrelationskoeffizient: {spearman_coeff}")
