'''Clase que contiene las excepciones resultantes del uso de la interfaz'''


class InterfazException(Exception):

    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
