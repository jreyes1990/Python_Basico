''' FOR: Es un bucle que se repite un numero predeterminado de veces.
    El bucle se reitera varias veces como elementos tenga el objeto (iterable) que recorre el For.
    Los objetos iterables pueden ser listas, cadenas de texto, etc. '''

numeros = [1,2,3,4,5,6,7,8,9,10]
indices = 0

while (indices < len(numeros)):
    print(numeros[indices])
    indices += 1

for i in numeros:
    print(i)

### **************************************************************************************************** ###
'''Ya que la lista son mutables podemos modificar su contenido en un bucle'''

numero = [0,1,2,3,4,5,6,7,8,9,10]
indice = 0

for numeros in numero:
    numero[indice] *= 10
    indice += 1
    numero

print(numero)

### **************************************************************************************************** ###
'''Funcion enumerate(): Permite realizar una lectura secuencial del objeto con clave y valor
   Esta funcion devuelve el elemento y su indice'''
numeros = [0,1,2,3,4,5,6,7,8,9,10]
numero = [1,2,3,4,5,6,7,8,9,10]
indice = 0

for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
    numeros

print(numeros)

### **************************************************************************************************** ###
'''Recorriendo cadena de texto'''

cad = "Hola, mi gente"

for caracter in cad:
    print(caracter)


cad2 = ""

for caracter in cad:
    cad2 += "*"
    
print(cad,"\n",cad2)


cad3 = ""

for caracter in cad:
    cad3 += caracter * 3
    
print(cad3)


for i in range(10):
    print(i)


for i in range(5,30,3):
    print(i)


lista = list(range(5))

for i in lista:
    print(lista)
    print(i)


### **************************************************************************************************** ###
'''EJERCICIO 1
   Realizar un programa que lea 2 numeros por teclado y permita elegir entre 3 opciones en un menu
   - Mostrar la suma de 2 numeros.
   - Mostrar la resta de 2 numeros (el primero menos el segundo).
   - Mostrar la multiplicación de 2 numeros'''

n1 = float(input("Introduce el primer numero: "))
n2 = float(input("Introduce el segundo numero: "))

print("¿Que quieres hacer?\n[1] Suma los 2 numeros\n[2] Restar los 2 numeros\n[3] Multiplicar los 2 numeros")
opcion = input("Ingresa una opcion: ")

if opcion == "1":
    print(f"La suma de {n1} + {n2} es {n1+n2}")
elif opcion == "2":
    print(f"La resta de {n1} + {n2} es {n1-n2}")
elif opcion == "3":
    print(f"La multiplicacion de {n1} + {n2} es {n1*n2}")
else:
    print("La opcion ingresada es invalida")


### **************************************************************************************************** ###
'''EJERCICIO 2
   Dada a una lista de strings (cadena de caracteres), haga un programa que devuelva
   - El numero de strings que tienen la longuitud de 2 o mas caracteres, y cuyo primer y ultimo caracter son iguales.
   - Una lista nueva con solo estos strings'''

listas = ['avila','cafe','este','narracion','buda','extra','salida']
listas2 = []
suma = 0

for item in listas:
    if(len(item) >= 2 and (item[0] == item[-1])):
        suma += 1
        listas2.append(item)
        suma, listas2

print(suma, listas2)


### **************************************************************************************************** ###
'''EJERCICIO 3
   Realiza un programa que pida un numero impar. Si el usuario no ingresa un numero impar, 
   debe repetirse el proceso hasta que ingrese un numero valido'''

while (True):
    n = int(input("Introduce un numero impar: "))
    if (n%2 != 0):
        break