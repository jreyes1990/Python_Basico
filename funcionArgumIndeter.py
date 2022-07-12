def argumentar(*args):
    for elemento in args:
        print(elemento)

argumentar(5,"Johel Yun",[0,1,2,3,4])


def nombrar(**kwargs):
    for kwarg in kwargs:
        #print(kwarg)
        print(kwarg," ",kwargs[kwarg])

nombrar(id=5,nombre="Feliz Feliciano",notas=[10,10,20,3,4])


def superNominacion(*args, **kwargs):
    suma = 0
    for e in args:
        suma += e
    print("El promedio indeterminado es {}".format(suma/len(args)))
    for clave in kwargs:
        print(clave,"\t",kwargs[clave])

superNominacion(10,10,20,3,4, id=5, nombre="Victor Liliput", edad=27, notas=[10,10,20,3,4])
