import math

class Punto:

    def __init__(self,x=0,y=0):
        """
        cada vez que instanciemos un objeto tendremos que declarar los puntos x e y
        a menos que le pasemos parametros por defecto
        """
        self.mover(x,y)

    def mover(self,x,y):
        "Mueve el punto a una nueva localización en un espacio bidimensional."
        self.x = x
        self.y = y
    
    def reiniciar(self):
        'Reinicia el objeto al origen Geométrico: 0,0'
        self.mover(0,0)
    

    def calcular_distancia(self, otro_punto):
        """
        Se le pasa otro objeto Punto
        Se usa el teorema de pitagoras para calcular la distancia entre dos puntos
        Haya la raiz cuadrada del cuadrado de los valores
        La distancia es devuelta como un float
        """
        return math.sqrt(
            (self.x - otro_punto.x) ** 2 +
            (self.y - otro_punto.y) ** 2
        )


#punto1 = Punto(2,4)
#punto2 = Punto(6)

#punto1.reiniciar()
#punto2.mover(5,3)

#print(punto2.calcular_distancia(punto1))
