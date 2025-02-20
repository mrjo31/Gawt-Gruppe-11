##Programm um Box-Whisker- unde Scatterplot für gew Datei macht
import pandas as pd
import matplotlib.pyplot as plt

def plots(filename,xlable,ylable,title,box=False,scatter=False):
    #einlesen
    df = pd.read_csv(filename,sep = ',')

    if box == True:
    # Boxplot für den DataFrame erstellen
        df.boxplot(column=[ylable])

    #Titel und Achsenbeschriftungen
        plt.title('Boxplot aus'+title+'.csv')
        plt.ylabel(ylable)

    # Diagramm anzeigen
        plt.show()


    # Scatterplot erstellen
    if scatter == True:
        plt.scatter(df[xlable],df[ylable],color='blue',alpha=0.7,s=5)

    # Titel und Achsenbeschriftungen für den Scatterplot hinzufügen
        plt.title('Scatterplot aus'+title+'.csv')
        plt.xlabel(xlable)
        plt.ylabel(ylable)

    # Diagramm anzeigen
        plt.show()
    return 0

plots('data-1.csv','DATE','Percent change from a year ago','Test',False,True)
