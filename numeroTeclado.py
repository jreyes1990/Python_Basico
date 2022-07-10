'''Realiza un programa que lea 2 numeros por teclado y determine los siguientes aspectos
   (Es suficiente con mostrar TRUE o FALSE)
   - Si los 2 numeros son iguales
   - Si los 2 numeros son diferentes
   - Si el primero es mayor que el segundo
   - Si el segundo es mayor o igual que el primero'''

n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))

print("\n")
print("¿Los numero son iguales? RESPUESTA: ", n1==n2)
print("¿Los numeros son diferentes? RESPUESTA:", n1!=n2)
print("¿El primero es mayor que el segundo? RESPUESTA: ", n1>n2)
print("¿El segundo es mayor o igual que el primero? RESPUESTA: ", n1<=n2)
