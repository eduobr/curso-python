class ListaContactos(list):
    def buscar(self, nombre):
        '''Devuelve todos los contactos que contienen el valor de búsqueda en su nombre.'''
        contactos_coincidentes = []
        for contacto in self:
            if nombre in contacto.nombre:
                contactos_coincidentes.append(contacto)
        return contactos_coincidentes

class Contacto:
    todos_contacto = ListaContactos()
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.todos_contacto.append(self)
    
    @staticmethod
    def mostrar_contactos():
        for i in Contacto.todos_contacto:
            print(i.nombre)

class Vendedor(Contacto):
    def __init__(self, nombre, email, telefono):
        super().__init__(nombre, email)
        self.telefono = telefono

    def pedido(self, pedido):
        print("En una aplicación completa enviaría el pedido "
                "{} pedido a {}".format(pedido, self.nombre))

class NombreLargoDict(dict):
    def clave_maslarga(self):
        maslarga = None
        for key in self:
            if not maslarga or len(key) > len(maslarga):
                maslarga=key
        return maslarga

'''
from contacto import NombreLargoDict
clavelarga = NombreLargoDict
clavelarga['hola'] = 1
clavelarga['la mas larga'] = 5
clavelarga['adiós'] = 'final'
clavelarga.clave_maslarga()
'''
        
