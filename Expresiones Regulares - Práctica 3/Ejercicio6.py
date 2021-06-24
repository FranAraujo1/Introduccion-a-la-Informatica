import re
frase = "Perros y gatoz se llevan mal"
lista = ["Perros", "Gatos", "Peces"]
for i in lista:
    if re.search(i, frase) is not None:
        print(i, "se encuestra en la frase")
    else:
        print(i,"no se encuentra en la frase")