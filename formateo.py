nombre = 'La cartuja de parma'
x = .7

print(F'El valor de {nombre} es ', x)

'''Aplicando metodos'''
print(f'El valor de {nombre.title()} es', x, ' dolares por el papel') #f: evalua el valor del nombre que esta dentro de las llaves

diccionario = {'uno': x, 'dos': x.__add__(10)} #__add__ : Suma o añade el valor que pasa como argumento (x)
print(diccionario)
print(f'{nombre.title()} cuesta {diccionario["uno"]} pesos y el otro libro {diccionario["dos"]} pesos.')