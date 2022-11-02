mitupla=("Eduardo",20,4,1995)
print(mitupla[2])

#para convertir una tuple en lista
milista=list(mitupla)

print(milista)

#para convertir una lista en tuple
mitupla = tuple(milista)
print(mitupla)

#saber cuantas veces se repite un elmento
print(mitupla.count(20))

#saber cuantos elementos tiene una tupla
print(len(mitupla))

#desempaquetado de tupla
nombre,dia,mes,agno=mitupla
print(nombre)
print(dia)
print(mes)
print(agno)