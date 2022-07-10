'''Utilizando operadores logicos determina si una cadena de texto introducida por el usuario
   tiene una longuitud mayor o igual a 3 y menor o igual a 12 (Basta con mostrar TRUE o FALSE)'''

cadena = input("Escribe un texto: ")
print('¿La longuitud de su texto es mayor o igual que 3 pero menor o igual que 12?',len(cadena)>=3 and len(cadena)<=12)