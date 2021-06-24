#Ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas
#de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P".

ocurrencias = []
with open("/Users/frana/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","r") as lineas:
    for linea in lineas:
        if linea[0] != "P":
            ocurrencias.append(linea)

print(len(ocurrencias))

