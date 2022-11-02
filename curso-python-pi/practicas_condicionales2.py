print("Programa de Becas 2019")
distancia = int(input("Ingrese la distancia: "))
hermanos=int(input("Ingrese la cantidad de hermanos: "))
salario=int(input("Ingrese su salario: "))

if distancia>40 and hermanos>5 or salario<10000:
	print("Puede obtener Beca")
else:
	print("No puede obtener Beca")