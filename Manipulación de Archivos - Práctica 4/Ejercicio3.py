
def ultimasNlineas(nombreArchivo,N):
    with open(nombreArchivo) as archivo:
        for linea in (archivo.readlines() [-N:]):
            print(linea, end ='')
  

if __name__ == '__main__':
    nombreArchivo = "manipulacion_archivos.txt"
    N = 4
    print(ultimasNlineas(nombreArchivo,N))
else:
    print('Archivo no encontrado')