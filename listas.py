'''Listas: Son un tipo de dato compuesto de varios elementos, estos pueden ser caracteres o numeros
   u otros tipos incluso. Cada elemento de lal lista es accessible gracias a su indice'''

listaCompras = ["Huevos", "Leche", "Queso", "Jabón"]
listaPrecios = ["Huevos",1.5,"Leche",2,"Queso",3.5,"Jabón",5]

print(type(listaCompras))
print(f"""Los {listaPrecios[0]} cuestan {listaPrecios[1]} la {listaPrecios[2]} cuesta {listaPrecios[3]}""")

### **************************************************************************************************** ###
'''Mutabilidad: Las listan tienen la caracteristica de permitirnos modificar el valor de alguno de sus
   elementos. Esto se llama mutabilidad y es importante distinguir entre objetos mutables, como las
   listas y otros objeto inmutables'''

listaPrecios[1] = 0.9

print(f'''{listaPrecios} \nLos {listaPrecios[0]} cuestan {listaPrecios[1]}''')

### **************************************************************************************************** ###
'''Metodos de las listas: Podemos inicializar una lista de numeros a traves de una funcion llamada
   range(a, b, in).
   - a: Es el limite inferior de la secuencia de numeros
   - b: Es el limite superior (este se excluye)
   - in: Es la unidad de incremento (argumento opcional)'''

numeros = range(0,20,2);
listaNumeros = list(numeros);

print(f"""{numeros}\n{listaNumeros}""")

### **************************************************************************************************** ###
'''Para añadir elementos a la lista utilizamos el metodo append()'''

listaNumeros.append(15)
print(f"""Agregando elemento 15\n{listaNumeros}""")

### **************************************************************************************************** ###
'''Aplicar el operador de la adicion (+) para concatenar 2 listas'''

print(f"""Aplicando metodo adicion\n{listaNumeros + [23,66,12,35,'hola','overtime']}""")
print(f"""Aplicando metodo adicion desde\n{listaNumeros[:5] + [23,66,12,35,'hola','overtime']}""")

### **************************************************************************************************** ###
'''Funcion len(): nos permite conocer el numero total de elementos'''

print(f"""El total de elementos es: {len(listaNumeros)}""")

### **************************************************************************************************** ###
'''Actualizar varios elementos de una lista utilizando slicing'''

listaNumeros[:4] = ["Platos",14,"Libros","Teclados"]

print(f"""Aplicando varios elementos\n{listaNumeros}""")

### **************************************************************************************************** ###
'''Listas anidadas, asignando listas como valores en una lista'''

fila1 = [1,2,3]
fila2 = [4,5,6]
fila3 = [7,8,9]
matriz = [fila1,fila2,fila3]

print(f"""Listas anidadas en la matriz\n{matriz}""")