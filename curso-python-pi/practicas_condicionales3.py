print("Asignaturas Optativas Año 2019:")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion  = input("Escriba la asignatura escogida: ")
asignatura = opcion.lower()
if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
	print("Asignatura elegida: "+asignatura)
else:
	print("La Asignatura elegida no está contemplada")