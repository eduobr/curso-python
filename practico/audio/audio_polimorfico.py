class ArchivoAudio:
    def __init__(self, nombrearchivo):
        if not nombrearchivo.endswith(self.ext):
            raise Exception("formato archivo invalido")
        self.nombrearchivo =  nombrearchivo

class ArchivoMP3(ArchivoAudio):
    ext = "mp3"
    def play(self):
        print("ejecutándose {} como mp3".format(self.nombrearchivo))

class ArchivoMP3(ArchivoAudio):
    ext = "wav"
    def play(self):
        print("ejecutándose {} como wav".format(self.nombrearchivo))

class ArchivoOgg(ArchivoAudio):
    ext = "ogg"
    def play(self):
        print("ejecutándose {} como ogg".format(self.nombrearchivo))

"""
Si colocamos:
mp3 = ArchivoMP3("miarchivo.wav")
nos dara error ya que la extensión no se corresponde con la de la clase
"""