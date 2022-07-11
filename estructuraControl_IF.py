x = 6

if x == 2:
    print("x vales 2")
if x == 6:
    print("x vales 6")

a = 10
b = 5

if a == 10:
    print("A vale {}".format(a))
    if b == 5:
        print("B vale {}".format(b))

if a == 10 and b == 5:
    print("A vale {} and B vale {}".format(a, b))

z = 13

if z % 2 == 0:
    print(z," es un numero par")
else:
    print(z, " es un numero impar")

# Respuestas dinamicas
texto = input("¿Que desea hacer?: ")

if texto == 'SALUDAR':
    print("Muy buenas noches")
elif texto == 'RETIRARSE':
        print("Ok, nos vemos")
else: 
    print("Ingrese una valida")