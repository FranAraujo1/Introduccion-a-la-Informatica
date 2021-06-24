#Ejercicio en Grupo 1 - Compra de una Casa
costo_total = int(input("Costo total de la casa: "))
porcentaje_deposito = costo_total * 0.25

sueldo_anual = int(input("¿Cual es su sueldo anual?: "))
sueldo_mensual = sueldo_anual / 12

porcentaje_ahorrado = float(input("¿Que porcentaje del sueldo quieres ahorrar por mes?: "))
g = 0.04
cantidad_ahorrada = sueldo_anual * (porcentaje_ahorrado * 12)
ganancia_por_mes = (cantidad_ahorrada * g) /12
ganancia_total = (cantidad_ahorrada * g)
cantidad_ahorrada_por_mes = (porcentaje_ahorrado * sueldo_mensual) + ganancia_por_mes
#ganancia_por_ano = ganancia_por_mes * 12
#ahorros_anuales = sueldo_anual * (porcentaje_ahorrado * 12) + ganancia_por_ano

cantidad_de_meses = porcentaje_deposito / (cantidad_ahorrada + ganancia_total)
print(porcentaje_deposito)
print("Usted debería ahorrar durante",cantidad_de_meses,"meses")