'''Funcion Recursiva: Se utiliza a si misma en el mismo cuerpo de su definicion'''

def cuentaAtras(num):
    num -= 1
    if num > 0:
        print(num)
        cuentaAtras(num)
    else:
        print(num, "boom")
    print("Fin de funcion", num)

cuentaAtras(5)


def factorial(numFact):
    print("Valor inicial --->",numFact)
    if numFact > 1:
        numFact = numFact * factorial(numFact-1)
        print("Valor final --->",numFact)
    return numFact

factorial(7)