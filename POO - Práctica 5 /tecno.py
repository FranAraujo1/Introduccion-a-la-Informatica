class tecnologia:
    def_unit_(self, bateria)
    self.bateria = 100

    def cargar_a_tope(self):
        self.bateria = 100

    def descargado(self):
            return self.bateria <= 20

class celular(tecnologia):
    def utilizar(self, minutos):
        self.bateria -= (1/2)*minutos


 class notebook(tecnologia):
     def utilizar(self, minutos):
        self.bateria -= minutos

un_celu = celular(tecnologia)
una_notebook = notebook(tecnologia)
print(un_celu.descargado())
un_celu.utilizar(180)
print(un_celu_descargado)            