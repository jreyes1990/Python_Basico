with open(r'C:\Cursos\PYTHON\Basico\output.txt','w') as f: #Crea el archivo output.txt
    f.write('Escritura en ficheros')
    f.write('\nOtra linea ')
    f.write('Y misma linea')

with open(r'C:\Cursos\PYTHON\Basico\output.txt','r') as f: #Lee la información del archivo output.txt
    print(f.read())

with open(r'C:\Cursos\PYTHON\Basico\output.txt','r') as f: #Muestra la información en pantalla del archivo output.txt
    data = f.readlines()
    print(data)

with open(r'C:\Cursos\PYTHON\Basico\output.txt','r') as f: #Lee la información del archivo output.txt con bucle FOR
    for linea in f:
        print(linea)

with open(r'C:\Cursos\PYTHON\Basico\output.txt','r') as f: #Separa las palabras del archivo output.txt
    for linea in f:
        palabras = linea.split()
        print(palabras,type(palabras))

palabra = list()
with open(r'C:\Cursos\PYTHON\Basico\output.txt','r') as f: #Todas las palabras del archivo output.txt esten en una misma lista
    for linea in f:
        term = linea.split()
        for t in term:
            palabra.append(t)
    print(palabra,type(palabra))