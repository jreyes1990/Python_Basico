'''Diccionarios: Son colecciones de datos semejantes a las listas
   Los diccionarios se caracterizan por:
   - Se define cada elemento dentro de un diccionario como una relación entre clave :valor,
   - Las claves ejercen como indice de cada elemento (no son unicamente numeros) '''

colores = {'azul': 'blue', 'negro': 'black', 'rosado': 'pink'}
propiedades = {1: 'Nombre', 2: 'Apellido', 3: 'Profesión', 4: 'Región'}

print(f"""{propiedades}""")
print(f"""{colores}""")
print("\n")

### **************************************************************************************************** ###
'''Podemos escoger entre sus elementos utilizando las claves'''

print(f"""Se ingreso la clave 3, y corresponde a, RESPUESTA: {propiedades[3]}""")
print(f"""Se ingreso la clave 'azul', y corresponde a, RESPUESTA: {colores['azul']}""")
print("\n")

### **************************************************************************************************** ###
'''Tambien podemos modificar los valores de sus elementos y realizar operaciones con ellos'''

colores['negro'] = 'noir'

print(f"""{colores}""")

colores['anaranjado'] = 'orange'
colores['blanco'] = 'white'

print(f"""{colores}""")

print("\n")
edades = {'Albert': 24, 'Johel': 24, 'Roque': 26, 'Victor': 27}

print(f"""{edades}""")
print(f"""Roque tiene {edades['Roque']} años""")

edades['Johel'] +=1
print(f"""{edades}""")


print(f"""{edades['Albert'] + edades['Victor']}""")

### **************************************************************************************************** ###
'''METODOS
   A través de un bucle For podemos recorrer los elementos de un diccionario '''

print("Elementos segun bucle For")
for c in edades:
   print(f"""{c}""")
   print(f"""{edades[c]}""")

### **************************************************************************************************** ###
'''Metodo items(): Nos devuelve clave y valor automaticamente'''

print("Elementos valor y clave")
for c,v in edades.items():
   print(c,v)

### **************************************************************************************************** ###
'''Metodo del(): Nos permite eliminar los valores de un diccionario'''

del(colores['azul'])

print(f"""{colores}""")
print("\n")

### **************************************************************************************************** ###
'''Debemos combinar provechosamente las listas y los diccionarios.
   Por ejemplo para crear un equipo de personajes'''

equipo = []

personajes = {'Nombre': 'Raskolnikov', 'Clase': 'Picaro', 'Nación': 'Rusia'}
equipo.append(personajes)

print(f"""{equipo}""")

personajes = {'Nombre': 'Emma', 'Clase': 'Curandera', 'Nación': 'Francia'}
equipo.append(personajes)

personajes = {'Nombre': 'Rebeca', 'Clase': 'Banquera', 'Nación': 'Inglaterra'}
equipo.append(personajes)

print(f"""{equipo}""")

for e in equipo:
   print(e["Nombre"],",",e["Clase"]," oriundo de ",e["Nación"])


   