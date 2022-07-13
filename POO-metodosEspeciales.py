class Video():
    #Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se creo el video ",self.titulo)

    #Destructor de clase
    def __del__(self):
        print("Se elimino el video ",self.titulo)

    #Redefinimos len() para que devuelva la duracion del video
    def __len__(self):
        return self.duracion

    #Redefinimos str para que muestre la información del video
    def __str__(self):
        return f"{self.titulo} publicado en {self.lanzamiento} con una duración de {self.duracion} minutos"


c = Video('The Avengers',143,2012)
print(str(c))
print(len(c))
del(c)