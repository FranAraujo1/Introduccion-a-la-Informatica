#a)
import re
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))


#d)
import re
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("he"))
print(encontrar_patron("hheeeeeeey"))
