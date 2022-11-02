import datetime

#Almacena todas las ids disponibles para las nuevas notas

ultima_id = 0

class Nota:
    '''Representa una nota en el cuaderno. Se compara con un String en la búsquedas y 
    las etiquetas para cada nota.'''

    def __init__(self, memo, tags=''):
        '''Inicializa una nota con memo y tags opcionales separados por comas. Automáticamente
        configura la fecha de la creación de la nota y una única id'''
        self.memo = memo
        self.tags = tags
        self.creacion_date = datetime.date.today()
        #definimos una variable global para saber las ids que se han ido utilizando en las notas
        global ultima_id
        ultima_id += 1
        self.id = ultima_id 
        
    def match(self, filter):
        '''Determina si una nota concuerda con el filtro de texto. Devuelve True si concuerda, en 
        otro caso False. Busqueda es case sensitive y compara tanto text como con tags.'''
        return filter in self.memo or filter in self.tags

class Cuaderno:
    '''Representa una colección de notas que pueden ser etiquetadas, modificadas y se pueden buscar.'''
    def __init__(self):
        '''Inicializa un cuaderno con una lista vacia.'''
        self.notas = []
    
    def nueva_nota(self, memo, tags=''):
        '''Crea una nueva nota y la añade a la lista.'''
        self.notas.append(Nota(memo,tags))
    
    def modificar_memo(self, nota_id, memo):
        '''Encuentra la nota con la id dada y cambia su memo al valor dado.'''
        #self.modificar_memo(self, nota_id).memo = memo
        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.memo = memo
            return True
        return False
    
    def modificar_tags(self, nota_id, tags):
        '''Encuentra la nota con la id dada y cambia sus tags al valor dado.'''
        #self._encontrar_nota(nota_id).tags = tags
        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.tags = tags
            return True
        return False

    def search(self, filter):
        '''Encuentra todas las notas que concuerdan con el filtro string dado.'''
        return [nota for nota in self.notas if nota.match(filter)]

    def _encontrar_nota(self, nota_id):
        '''Localiza la nota con la id dada.'''
        for nota in self.notas:
            if str(nota.id) == str(nota_id):
                return nota
        #si no encuentra la nota devuelve None
        return None