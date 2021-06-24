import re

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = '[a-zA-Z0-9.]'


def verificar(patron,texto):
    if re.search(patron,texto):
        print("Verificado")
    else:
        print("No Verificado")
    
verificar(patron,texto)
