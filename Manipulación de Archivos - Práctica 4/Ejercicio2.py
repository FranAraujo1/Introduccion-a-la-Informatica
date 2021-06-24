cant_lineas = int(input('Ingrese la cantidad de líneas a leer: '))

with open("/Users/frana/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", 'r') as archivo:
    for i in range(cant_lineas):
        linea = archivo.readline()
        print(linea, end='')
