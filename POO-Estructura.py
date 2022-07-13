# Se crea una estructura para los productos
class Producto:

    def __init__(self, cod, nombre, categoria, pvp):
        self.cod = cod
        self.nombre = nombre
        self.categoria = categoria
        self.pvp = pvp

    def __str__(self):
        return '{} {}'.format(self.nombre, self.pvp)


# Y otra estructura para el negocio
class Negocio:

    def __init__(self, productos=[]):
        self.productos = productos

    def mostrarProducto(self, cod=None):
        for p in self.productos:
            if p.cod == cod:
                print(p)
                return
        print("Producto no encontrado")

    def borrarProducto(self, cod=None):
        for i,p in enumerate(self.productos):
            if p.cod == cod:
                del(self.productos[i])
                print(str(p),"> ELIMINADO")
                return 
        print("Producto no encontrado")


limones = Producto(cod="10010", nombre="Limones", categoria="Fruta", pvp=0.80)
platos = Producto("10020", "Platos Alpina", "Vajilla", 2.4)

print(f"{limones}")
print(f"{platos}")

negocio = Negocio(productos=[limones,platos])
negocio.productos

negocio.mostrarProducto('10010')
negocio.borrarProducto('10010')
negocio.mostrarProducto('10010')