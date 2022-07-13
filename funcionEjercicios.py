'''Realiza una funcion llamada area_rectangulo() que devuelva el area a partir de una base y una altura.
   Calcula el area de un restangulo de 15 de base y 10 de altura'''

def area_rectangulo(base,altura):
    return base*altura

print(f"El area del rectangulo es: {area_rectangulo(15,10)}")


'''Realiza una funcion llamada area_circulo que devuelva el area a partir de un radio.
   Calcula el area de un circulo de 5 de ancho'''

import math

def area_circulo(radio):
    return (radio**2)*math.pi

print(f"El area del circulo es: {area_circulo(2.5)}")


'''Realiza una funcion llamada relacion() que a partir de 2 numeros cumpla lo siguiente:
   - Si el primer numero es mayor que el segundo, debe devolver 1.
   - Si el primer numero es menor que el segundo, debe devolcer -1.
   - Si ambos numeros son iguales, debe devolver 0.'''

def relacion(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))


'''Realiza una funcion llamada intermedio() que a partir de 2 puntos, devuelva su punto intermedio'''

def intermedio(a,b):
    return (a+b)/2

print(f"{intermedio(-12,24)}")


'''Realiza una funcion separar() que tome una lista de numeros enteros y devuelva dos listas ordenadas:
   La primera con los numeros pares y la segunda con los numeros impares'''

numeros = [1,2,3,4,5,6,7,8,9,10]

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares,impares

pares, impares = separar(numeros)

print(f"Pares {pares}")
print(f"Impares {impares}")