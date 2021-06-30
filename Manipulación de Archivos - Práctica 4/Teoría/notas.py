#MANIPULACION de ARCHIVOS - Practica 4
import os
# apertura de archivos
# - "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. 
# - "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión. (r,r+,w,a)

archivo = open(path_al_archivo, modo)

# Importante cerrar el archivo

archivo.close()

# Algo que siempre nos asegura el cerrado del archivo es:

with open(path_al_archivo, modo) as miarch:
    #Aquí van las líneas de procesamiento del archivo


# Escritura de archivos

    with open(path_al_archivo, modo) as miarch:
        miarch.write("Este es el contenido del archivo")

# Leer archivo completo
bio = open("bio.txt", "r")
bio.read()

#Leer por lineas
bio = open("bio.txt", "r")
bio.readlines()
bio.readline()











