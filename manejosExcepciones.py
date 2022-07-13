'''Errores y excepciones: Los errores detienen la ejecución de un programa.
   Se pueden presentar distintos tipos de errores'''

while(True):
    try:
        num = int(input("Ingresa un numero: "))
        print("El numero {} y al dividirlo da {}".format(num,num/num))
        break
    except:
        print("Por favor, intente de nuevo")


while(True):
    try:
        num = int(input("Ingresa un numero: "))
        print("El numero {} y al dividirlo da {}".format(num,num/num))
    except:
        print("Por favor, intente de nuevo")
    else:
        print("La ejecución fue exitosa.")
        break

while(True):
    try:
        num = int(input("Ingresa un numero: "))
        print("El numero {} y al dividirlo da {}".format(num,num/num))
    except:
        print("Por favor, intente de nuevo")
    else:
        print("La ejecución fue exitosa.")
        break
    finally:
        print("Fin del bucle")