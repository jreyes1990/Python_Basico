import math

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f"{self} pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"{self} pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"{self} pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(f"{self} pertenece al cuarto cuadrante")

        #Si Y==0, el punto se ubica sobre el eje X
        elif self.x != 0 and self.y == 0:
            print(f"{self} Se ubica sobre el eje X")

        #Si X==0, el punto se ubica sobre el eje X
        elif self.x == 0 and self.y != 0:
            print(f"{self} Se ubica sobre el eje Y")

        #Si ambos son 0, el punto se ubica en el origen
        else:
            print(f"{self} se ubica en el origen")

    def vector(self, p):
        print(f"El vector que une los puntos {self} y {p} es igual a ({p.x-self.x}, {p.y-self.y})")

    def distancia(self, p):
        mod = math.sqrt((p.x -self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {mod}")

a = Punto(5,8)
b = Punto(10,2)
c = Punto(4,6)
d = Punto(-8,4)

a.cuadrante()
b.cuadrante()
c.cuadrante()
d.cuadrante()

a.vector(d)
a.distancia(d)