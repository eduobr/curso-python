#Clave:Valor
midiccionario={"Alemania":"Berlin","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
#Agregar otro elemento al diccionario
midiccionario["Italia"]="Lisboa"
#Mostrar valor de Francia
print(midiccionario["Francia"])
print(midiccionario)
#Modificar elemento
midiccionario["Italia"]="Roma"
print(midiccionario)
#Borrar elemento
del midiccionario["Reino Unido"]
print(midiccionario)

#Asinar Tupla a diccionario
mitupla=("España","Francia","Reino Unido","Alemania")
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"París"}
print(midiccionario2)

#Asignar lista a valor
midiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario["Anillos"])

#Guardar diccionario dentro de diccionaro
midiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario["Anillos"])
print(midiccionario["Anillos"]["temporadas"])

#Devolver las clves del diccionario
print(midiccionario.keys())
#Devolver los valores del diccionario
print(midiccionario.values())