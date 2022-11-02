#Mostramos texto con variables
for i in range(5):
	print(f"valor de la variable {i}")

print("--------------------------------------")

#Va desde el 5 al 47 de 3 en 3
for i in range(5,48,3):
	print(f"valor de la variable {i}")

print("--------------------------------------")

valido = False
email=input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("Email Correcto")
else:
	print("Email Incorrecto")