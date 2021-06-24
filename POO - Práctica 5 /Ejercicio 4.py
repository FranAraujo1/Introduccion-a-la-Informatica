# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible 
# indicar directamente un número nuevo que reemplace al valor actual.


class Contador():
    def __init__(self, numero):
        self._numero = numero
        
    def inc(self):
        self._numero += 1

    def dis(self):
        self._numero -= 1

    def reset(self):
        self._numero == 0

    def valorActual(self):
        return self._numero 
        
    def valorNuevo(self, nuevoValor):
        self._numero = nuevoValor
        

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()



