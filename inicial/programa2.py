def saludo_suma():
    print("Menu")
    print("1-Saludo")
    print("2-Suma")
    print("Escoja una opcion")
    opcion=input()
    if(opcion in "1" or opcion in "2"):
        if(opcion=="1"):
            nombre = input("Escriba su nombre \n")
            print("Bienvenido",nombre)
        if(opcion=="2"):
            print("Escriba el numero 1")
            numero1=input()
            numero2=input("Escriba el numero 2 \n")
            resultado=int(numero1)+int(numero2)
            print("La suma de",numero1,"+",numero2,"=",resultado)
    else:
        print("La opcion no es valida Adios!!!")
            

#Actividad
#Hacer un menu que el usuario pueda elegir multiplicar, dividir
#y restar
#el usuario en el menu solo puede elegir la opcion 1 o 2       
#ademas el ingreso por teclado solo pueden ser numeros 1 -9
