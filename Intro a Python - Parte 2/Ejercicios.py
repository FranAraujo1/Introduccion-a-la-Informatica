#Ejercicio1
cadena = input("Ingrese una palabra:")
if cadena[0] == (cadena[0].upper()):
    print("La primer letra es mayúscula:",cadena[0])
else:
    print("La primer letra es minúscula:", cadnea[0])

#Ejercicio2
numero = int(input("Ingrese un número:"))
par = (numero % 2 == 0)
if numero > 0:
    if par:
        print(numero, "Es positivo y par")
    else:
        print(numero, "Es positivo e impar")
elif numero < 0:
    if par:
        print(numero, "Es negativo y par")
    else:
        print(numero, "Es negativo e impar")
else:
    print("Es 0 y por lo tanto par")
    
#Ejercicio3
numero = int(input("Ingrese un número del 1 al 6:"))
if numero >= 1 and numero <= 6:
    print(7 - numero)
else:
    print("El número ingresado es incorrecto")

#Ejercicio4
gramos = int(input("Ingrese el peso en gramos:"))
zona = input("Ingrese la zona:")
if gramos < 5000:
    if zona == "America del Sur":
        print(10 * gramos)
    elif zona == "America Central":
        print(15 * gramos)
    elif zona == "America del Norte":
        print(18 * gramos)
    elif zona == "Europa":
        print(24 * gramos)
    elif zona == "Asia":
        print(30 * gramos)

#Ejercicio5
dia = int(input("Ingrese un numero de la semana entre 1 y 7:"))
if dia >= 1 and dia <= 7:
    if dia == 1:
        print("Es lunes")
    elif dia == 2:
        print("Es martes")
    elif dia == 3:
        print("Es miércoles")
    elif dia == 4:
        print("Es jueves")
    elif dia == 5:
        print("Es viernes")
    elif dia == 6:
        print("Es sábado")
    elif dia == 7:
        print("Es domingo")
else:
    print("El número es incorrecto")

#Ejercicio6
p1 = input("Ingrese una palabra:")
p2 = input("Ingrese una palabra:")
p3 = input("Ingrese una palabra:")
p4 = input("Ingrese una palabra:")
p5 = input("Ingrese una palabra:")
lista = [p1, p2, p3, p4, p5]

lista.reverse()
print(lista)

#Ejercicio7 
una_lista = []
un_numero = int(input("Introduce un número en la lista:"))
while un_numero>=0:
	lista.append(numero)
	un_numero = int(input("Introduce un número en la lista:"))

for un_numero in una_lista:
	print(un_numero," ",end="")

#Ejercicio8
lista1 = []
lista2 = []
lista3 = []
for i in range(1,6):
	lista1.append(int(input("Introduce el elemento %d de la lista1:" % i)))
for i in range(1,6):
	lista2.append(int(input("Introduce el elemento %d de la lista2:" % i)))

for i in range(0,5):
	lista3.append(lista1[i] + lista2[i])

print("La suma de los elementos entre la lista 1 y 2 es:")
for numero in lista3:
	print(numero," ",end="")

#Ejercicio9
nombres = []
edades = []
    # Inicializo las listas hasta que introduzca un "*" 
while True:	
	nombre = input("Dime el nombre de un alumno:")
	if nombre != "*":
		nombres.append(nombre)
		edades.append(int(input("Dime su edad:")))
	if nombre == "*": break;	

    # Calcular la edad máxima
edad_max = max(edades)
    # Alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombres,edades):
	if edad >= 18:
		print(nombre)
	
    # Alumnos mayores 

print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres,edades):
	if edad == edad_max:
		print(nombre)

#Ejercicio10
contadores = {}
cadena = input("Escribí una cadena: ")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter] += 1
    else:
        contadores[caracter] = 1

for campo,valor in contadores.items():
    print (campo,valor)

#Ejercicio11
contadores = {}
arlfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper():
    contadores[letra] = 0

cadena = input("Escribí una cadena: ")

for caracter in cadena:
    if caracter.lower() in alfabeto:
        contadores [caracter] += 1

for campo, valor in contadores.items():
    print (campo, valor)

#Ejercicio12
alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

#Ejercicio13 - Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
numero = int(input("Introduce un número:"))
numero2 = int(input("Introduce otro número:"))

if (numero % numero2==0):
   print("El primer número es multiplo del segundo") 
elif (numero2 % numero==0):
    print("El segundo número es multiplo del primero") 
else:
    print("No son múltiplos")

#Ejercicio 14 - Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.
temp_max = float(input("Ingresar la temperatura máxima del día en grados cº: "))
temp_min = float(input("Ingresar la temperatura mínima del día en grados cº: "))
temp_media = (temp_max + temp_min) / 2

print("La temperatura media del día es de ",temp_media,"grados cº")





