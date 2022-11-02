print("Verificación de Acceso")

edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad Incorrecta")
else:
	print("puedes pasar")
print("El programa ha finalizado")
