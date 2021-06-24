#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le
# aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento)
# y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar
#  esta clase y en algunos casos aplicar este descuento.


class Notebook:
    def __init__(self, precio,marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._precio = precio

    def precioConDescuento(self, descuento):
        return self._precio - descuento
    
 
descuento = int(input("Ingresar el monto de descuento: "))

notebook1 = Notebook(1000,'Apple','2010')
print(notebook1.precioConDescuento(descuento))