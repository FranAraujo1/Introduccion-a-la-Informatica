import re
texto = input("ingrese un texto:")
patron = "\W"
lista = re.findall(patron,texto)
primero = lista[0]
print(lista)
segundo = lista[4]
texto1 = re.sub(primero,"_",texto)
print(re.sub(segundo,"_", texto1))
