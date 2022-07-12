from cmath import inf


contador = 0

print("Estructura de control WHILE")
while contador <= 5:
    contador += 1
    print("Contador vale ",contador)
else:
    print("Se realizaron {} iteraciones".format(contador))

### **************************************************************************************************** ###
'''BREAK: Este comando detenemos el bucle en cualquier momento'''

contador_1 = 0

print("Estructura de control WHILE, aplicando (BREAK)")
while contador_1 <= 5:
    contador_1 += 1
    if contador_1 == 4:
        print("Rompemos el bucle cuando contador vale", contador_1)
        break
    print("Contador vale", contador_1)
else:
    print("Se realizaron {} iteraciones".format(contador_1))

### **************************************************************************************************** ###
'''CONTIUE: Este comando saltamos a la siguiente iteracion sin romper el bucle'''

contador_2 = 0

print("Estructura de control WHILE, aplicando (CONTINUE)")
while contador_2 <= 5:
    contador_2 += 1
    if contador_2 == 4:
        print("Ya que C vale {}, Saltamos esta iteracion y continuamos con la siguiente".format(contador_2))
        continue
    print("Contador vale", contador_2)
else:
    print("Se realizaron {} iteraciones".format(contador_2))

### **************************************************************************************************** ###
'''MENU DE USUARIO'''

print("Bienvenido")

while (True):
    opcion = input("""\nQue quieres hacer?\n(1) Saludar\n(2) Sumar 2 numeros\n(3) Salir\nIngresa una opcion: """)
    if opcion == '1':
        print("\nBarradas le manda muchos saludos!\n")
    elif opcion == '2':
        n1 = float(input("Ingresa el primer numero: "))
        n2 = float(input("Ingresa el segundo numero: "))
        resultado = n1 + n2
        print("\nEl resultado de la suma es {}".format(resultado))
    elif opcion == '3':
        print("\nDios me lo bendiga licenciado")
        break
    else:
        print("\nNo hay manera, socio. Intenta de nuevo")