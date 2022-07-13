productos = [
    {'cod': '10001', 'Nombre': 'Jabón Harmony', 'Categoria': 'Higiene Personal', 'PVP': 0.9},
    {'cod': '10002', 'Nombre': 'Cereal Nestle', 'Categoria': 'Cereal', 'PVP': 1.5},
    {'cod': '10003', 'Nombre': 'Limones', 'Categoria': 'Fruta', 'PVP': 0.70}
]

print(f"{productos[0]}")

def mostrarProducto(productos, cod):
    for p in productos:
        if (cod == p['cod']):
            return print('{} {}'.format(p['Nombre'], p['PVP']))
    print("Producto no encontrado")

mostrarProducto(productos,'10003')

def borrarProducto(productos, cod):
    for i,p in enumerate(productos):
        if (cod == p['cod']):
            del(productos[i])
            return print(str(p),"> ELIMINADO")
    print("Producto no encontrado")

borrarProducto(productos,'10003')


print("==CATALOGO DE PRODUCTOS==")
print(productos)

print("\n==MOSTRAR PRODUCTOS POR COD==")
mostrarProducto(productos,'10001')
mostrarProducto(productos,'10002')

print("\n==BORRAR PRODUCTOS POR COD==")
borrarProducto(productos,'10001')
borrarProducto(productos,'10002')

print("\n==CATALOGO DE PRODUCTOS==")
print(productos)