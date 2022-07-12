def suma(a, b):
    resultado = a + b
    return resultado

print(suma(5,6))


'''Definir un valor predeterminado para nuestros parametros'''

def resta(a=None, b=None):
    if a==None or b==None:
        print("Error, enviar 2 numeros en la funcion")
    else:
        return a-b

resta(2)


'''Argumentos por referencia'''

n = 10

def duplicarSecuencia(numero):
    for i,n in enumerate(numero):
        numero[i] *= 2
    return numero

nota_A = list(range(5))
nota_B = duplicarSecuencia(nota_A)
print(f"Nota A {nota_A} Nota B {nota_B}")

nota_C = list(range(6))
nota_D = duplicarSecuencia(nota_C[:])
print(f"Nota C {nota_C} Nota D {nota_D}")