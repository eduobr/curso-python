#Devuelve el numero mayor
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

def DevuelveMax(numero1,numero2):
	if numero1>numero2:
		return numero1
		#print("El numero1: ",numero1," es mayor que el numero2: ",numero2)
	else:
		return numero2
		#print("El numero2: ",numero2," es mayor que el numero1: ",numero1)

print(DevuelveMax(numero1,numero2))

print("El programa ha finalizado")