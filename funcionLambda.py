def doblar(num):
    resultado = num * 2
    return resultado

print(f"{doblar(5)}")


'''Utilidad de las funciones anonimas se ve al asignarlas a una variable'''

doblarLambda = lambda num: num * 2

print(f"{doblarLambda(15)}")


imparLambda = lambda num: num % 2

print(f"{imparLambda(5)}")

revertirLambda = lambda cadena: cadena[::-1]

print(f"{revertirLambda('camarada')}")

sumarLambda = lambda x,y: x+y

print(f"{sumarLambda(15,20)}")
