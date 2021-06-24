archivo = open("/Users/frana/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", 'r')
leer = archivo.read()
palabras = leer.split()

print("La cantidad de palabras en el texto es de: ", len(palabras))

archivo.close()