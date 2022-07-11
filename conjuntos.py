'''Conjuntos: Son colecciones de datos que nos facilitan ciertas operaciones ya que solo contienen
   valores unicos
   Se diferencian de las tuplas y listas en que
   - Cada elemento dentro del conjunto es unico
   - Sus elementos no estan ordenados '''

conjuntoVacio = set()
conjunto = {1,2,3}

print(f"""{type(conjuntoVacio)}\n{conjunto}""")

### **************************************************************************************************** ###
'''Metodo add(): Nos permite agregar elementos al conjunto'''

conjunto.add(4)
conjunto.add(5)
conjunto.add("C")
conjunto.add("A")
conjunto.add("P")
print(f"""Agregando elementos al conjunto\n{conjunto}""")

conjunto.add("C")
print(f"""Agregando elementos al conjunto\n{conjunto}""")

### **************************************************************************************************** ###
'''Utilizando los conjuntos para verificar pertenecia'''

grupo = {"Luis","Giulia","Victor","Aaron","Johel"}

print(f"""Verificando si Victor esta en el grupo, RESPUESTA: {"Victor" in grupo}""")
print(f"""Verificando si Johel no esta en el grupo, RESPUESTA: {"Johel" not in grupo}""")
print(f"""Verificando si 4 no esta en el grupo, RESPUESTA: {4 not in grupo}""")
print(f"""Verificando si 10 esta en el conjunto, RESPUESTA: {10 in conjunto}""")

### **************************************************************************************************** ###
'''Un conjunto elimina automaticamente los elementos duplicados'''

grupoCarros = {"Toyota","Toyota","Ford"}

print(f"""\n{grupoCarros}""")

### **************************************************************************************************** ###
'''Gracias a esta propiedad podemos convertir una lista a conjunto para eliminar duplicados facilmente'''

extra = [1,1,2,2,3,3,4,5,5,4,5,6]

print(f"""\n{extra}""")

c = set(extra)

print(f"""{c}""")

### **************************************************************************************************** ###
'''Podemos hacer la conversion en una sola linea'''

noDuplicados = list(set(c))

print(f"""{noDuplicados}""")

### **************************************************************************************************** ###
'''Cuando aplicamos la conversion a una cadena, el conjunto resultante incluye solo las letras unicas de esta'''

cadena = 'Jefe de jefe, patrón de patrón. Recógelo, recógelo'

print(f"""Resultante conversión de cadenas, donde incluye las letras unicas\n{set(cadena)}""")
