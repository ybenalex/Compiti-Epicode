import pandas as pd

file = pd.read_csv("owid-covid-data.csv.csv")
#print(file)

# 1 - dimensioni e diciture intetazione del file
#print(file.shape)
#print(file.head())
#print(file.columns)
riepilogo = file.describe()
#print(riepilogo)

# 2 - si chiede per ogni continente di trovare, il numero totali dei casi,
print(riepilogo)
print(file.columns)
list_continente =["Africa", "Europa", "Asia", "America-nord", "America-sud"]
for continente in list_continente :
    print("continente:", continente, "total_cases:", file.total_cases.groupby("continente")

# 3 - funzione che prende due continente in input dataset e fa il confronto
def confronto(dataset, "continente1", "continente2"):
    file = pd.read_csv("dataset")
    filtro1 = file.total_deaths & file.continente == "continente1"
    filtro2 = file.total_deaths & file.continente == "continente2"
    if file.filtro1.min() < file.filtro2.min():
        print("ci sono stati piu morti nel continente1 che nel continente2")

# 4 - funzione per numero totali di vaccinazioni
def confronto2(dataset, "continente1", "continente2"):
    file = pd.read_csv("dataset")
    filtro1 = file.new_vaccinations & file.continente == "continente1"
    filtro2 = file.new_vaccinations & file.continente == "continente2"
    if file.filtro1.min() < file.filtro2.min():
        print("ci sono stati piu vaccinazioni nel continente1 che nel continente2")

# 5 -