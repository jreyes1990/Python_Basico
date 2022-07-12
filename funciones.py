'''FUNCION
   Permiten reutilizar codigo.
   Una funcion podria considerarse como una variable que encierra un conjunto de instrucciones.
   Por lo tanto al llamar a una funcion lo que estamos haciendo es ordenar al programa para que
   ejecute un conjunto de instrucciones.
   Algunas caracteristicas de las funciones son:
   
   - Se pueden crear en cualquier momento del programa.
   - Su palabra reservada es def.
   - Seguido de def viene el nombre de la funcion y entre parentesis los argumentos de entrada.
   - No es obligatorio que la funcion devuelva un valor, aunque se puede usando la palabra reservada.
   - Las variables declaradas dentro de la funcion son locales a esa funcion.
   - Para declarar la variable dentro de una funcion, pero poder acceder desde fuera de la funcion, esta se puede declarar como golbal. '''

def saludar():
    print("Hola, esto se llama dentro la funcion saludar")

saludar()

def tabla_del_5():
    for i in range(10):
        print(f"5 x {i} = {5*i}")

tabla_del_5()

'''Scope: define el area de un programa en la cual puede acceder a un nombre'''

def prueba():
    n = 10
    return n

prueba()