'''Tuplas: Una tupla es la secuencia de valores (muy parecida a la lista).
   Los valores almacenados es una tupla pueden ser de cualquier tipo, y tambien estan indexados
   
   Se diferencia de las listas en que
   - No podemos modificar sus valores luego de crearla (Es inmutable)
   - Definimos sus valores entre parentesis, en vez de corchetes'''

tupla = ('Lunes','Martes','Miercoles')
tupla_muti = ([1,2,3],'a',71.4,tupla)

print(tupla_muti)
print(tupla_muti[-1])
print(tupla_muti.index('a'))
print(tupla_muti.count(tupla))