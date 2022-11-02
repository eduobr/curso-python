contador=0
miEmail = input("Introduce tu direccion de email: ")

for i in miEmail:
	if i=="@" or i==".":
		contador=contador+1

#Es lo mismo que email==True
if contador==2:
	print("El email es correcto")
else:
	print("El email no es correcto")