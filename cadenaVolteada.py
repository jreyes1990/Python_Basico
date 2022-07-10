''' Al realizar una consulta en un registro hemos recibido unos valores corruptos. Al parecer entrega
    el nombre y apellido del alumno al reves. ¿Que puede hacer para obtener el siguiente mensaje por pantalla '''

cadena = 'azebac ellehciM, 01'
cadena_volteada = cadena[::-1]
print(cadena_volteada[4::]," ha sacado un ",cadena_volteada[:2])
