#Ejercicio 1
valor = input("Pone un nombre ")
print(len(valor))

#Ejercicio 2
palabra = input("Ingresar una palabra ")
print(palabra[-2].upper())
print(palabra[-1].upper())


#Ejercicio 3
nombre = input("¿Cual es tu nombre?: ")
apellido = input("¿Cual es tu apellido?: ")
print("Hola",nombre,apellido)

#Ejercicio 4
nombre = input("¿Cual es tu nombre?: ")
apellido = input("¿Cual es tu apellido?: ")
apellido2 = input("¿Cual es tu segundo apellido?: ")
print("Iniciales: ",nombre[0].upper(),apellido[0].upper(),apellido2[0].upper())

#Ejercicio 5
numero1 = int(input("Ingresar un numero: "))
numero2 = int(input("Ingresar un numero: "))
numero3 = int(input("Ingresar un numero: "))

promedio = ((numero1 + numero2 + numero3) / 3)
print("El promedio de los numeros ingresados es de: ",promedio)

#Ejercicio 6
minutos = int(input("Ingresar la cantidad de minutos: "))
segundos_ingresados = (minutos * 60)
hs = (int(segundos_ingresados/3600))
mins = (minutos - (hs*3600)/60) 
print("Son",hs,"horas con",mins,"minutos")

#Ejercicio 7
sueldo_base = int(input("Ingresar sueldo base: "))
cantidad_de_ventas = int(input("Ingresar cantidad de ventas: "))
porcentaje_ganado_por_ventas = (cantidad_de_ventas * 10)
sueldo_total_del_mes = ((100 + porcentaje_ganado_por_ventas) * sueldo_base)/100
ganacia_x_ventas = sueldo_total_del_mes - sueldo_base
print("Dinero que recibira por las ventas generadas:$",ganacia_x_ventas)
print("Sueldo total a fin de mes: $",sueldo_total_del_mes)

#Ejercicio 8
numero_de_respuestas_correctas = int(input("Ingresar el número de respuestas correctas: "))
numero_de_respuestas_incorrectas = int(input("Ingresar el número de respuestas incorrectas: "))
nota = 0
nota_final = nota + (numero_de_respuestas_correctas*4) - (numero_de_respuestas_incorrectas*1)
print("Nota Final:",nota_final)
