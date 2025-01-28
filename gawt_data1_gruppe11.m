T = readtable("data-1.csv","VariableNamingRule","preserve");
T(1:93,1:2)

colonne2 =T(:,2)
modus=mode(colonne2) % modus
mittelwert=mean(colonne2) % arithmetische rmittelwert
%medianwert = median(T{:,2}); % Median der zweiten Spalte direkt aus der Tabelle
%disp(medianwert); % Median anzeigen
spannweite = range(colonne2); % Spannweite berechnen
disp(spannweite); % Spannweite anzeigen
% Daten aus der Tabelle extrahieren
colonne2 = T{:,2};
% Daten aus der Tabelle extrahieren
colonne2 = T{:,2};

% Stichprobenvarianz berechnen
stichprobenvarianz = var(colonne2, 1); % Der zweite Parameter 1 sorgt für die Stichprobenvarianz (n-1 Korrektur)
disp(stichprobenvarianz); % Ergebnis anzeigen
% Daten aus der Tabelle extrahieren
colonne2 = T{:,2};

% Mittelwert berechnen
mittelwert = mean(colonne2);

% Standardabweichung berechnen
stdabweichung = std(colonne2);

% Variationskoeffizient berechnen
variationskoeffizient = stdabweichung / mittelwert;

disp(variationskoeffizient); % Ergebnis anzeigen
% Wenn T deine Tabelle ist, dann:
% Alle numerischen Variablen extrahieren
numericVars = varfun(@isnumeric, T, 'OutputFormat', 'uniform');
numericData = T(:, numericVars);

% Boxplot für jede numerische Variable erstellen
figure; % Neue Figur für das Boxplot
boxplot(table2array(numericData)); % Boxplot für die Daten
title('Box-Whisker-Plot für jede numerische Variable');
ylabel('percent change from a year ago ')% Wenn T deine Tabelle ist, dann:
% Alle numerischen Variablen extrahieren
numericVars = varfun(@isnumeric, T, 'OutputFormat', 'uniform');
numericData = T(:, numericVars);

% Berechnung der Quartile und Dezile für jede numerische Variable
for i = 1:width(numericData)
    data = numericData{:, i};
    
    % Quartile berechnen (25%, 50%, 75%)
    quartile = quantile(data, [0.25, 0.5, 0.75]); % Q1, Median (Q2), Q3
    % Dezile berechnen (10%, 20%, ..., 90%)
    dezile = prctile(data, 10:10:90); % 10%, 20%, ..., 90%
    
    % Ausgabe der Ergebnisse
    disp(['Variable: ', numericData.Properties.VariableNames{i}]);
    %disp(['Quartile: (Q1, Median, Q3): ', num2str(quartile')]);
    disp(['Quartile: (Q1, Median, Q3):']);
    format long ;
    disp( num2str(quartile'))
    %disp(['Dezile (10%, 20%, ..., 90%): ', num2str(dezile')]);
    disp(['Dezile (10%, 20%, ..., 90%): '])
    disp( num2str(dezile'))
    disp('-------------------------------');
end
% Beispiel: Quartilsabstand und Dezile für jede Variable in der Tabelle T berechnen

% Variablen initialisieren
quartilsabstand = [];  % Quartilsabstände
dezile = [];  % Dezile

% Schleife durch jede Spalte der Tabelle
for i = 1:width(T)
    daten = T{:,i};  % Spalte als numerisches Array extrahieren
    
    % Quartilsabstand berechnen
    quartilsabstand(i) = iqr(daten);  % IQR: Interquartilsabstand
    
    % Dezile berechnen
    dezile(:,i) = quantile(daten, (0.1:0.1:0.9));  % Dezile von 10% bis 90%
end

% Ergebnisse anzeigen
disp('Quartilsabstände für jede Variable:');
disp(quartilsabstand);

disp('Dezile für jede Variable (Spalten repräsentieren Variablen):');
disp(dezile);
