def palabraMasLarga(nombre_archivo):
    with open(nombre_archivo,'r') as lineas:
        palabras = lineas.read().split()
    mas_larga = len(max(palabras, key=len))
    return [palabra for palabra in palabras if len(palabra) == mas_larga]

print(palabraMasLarga("manipulacion_archivos.txt"))
la_palabra_mas_larga = palabraMasLarga("manipulacion_archivos.txt")
print("La cantidad de caracteres que contiene esta palabra es de: ",len(str(la_palabra_mas_larga)))

