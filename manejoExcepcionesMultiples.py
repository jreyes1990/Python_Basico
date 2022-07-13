'''Excepxiones multiples: En el mismo bloque de codigo pueden surgir distintos tipos de errores
   y suelen ser conveniente actuar de manera particular para cada error.
   
   Se recomienda asignar la excepcion a una variable, asi podemos analizar el tipo de error que sucede por
   su identificador'''

try:
    num = int(input("Ingresa un numero: "))
    print('9/{} = {}'.format(num,9/num))
except Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)


print(type(1).__name__)
print(type(3.14).__name__)
print(type([]).__name__)
print(type(()).__name__)
print(type({}).__name__)


try:
    num = int(input("Ingresa un numero: "))
    print('9/{} = {}'.format(num,9/num))
except ValueError:
    print("No se puede dividir entre un texto")
except ZeroDivisionError:
    print("No se puede dividir entre cero, intenta de nuevo")
except Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)