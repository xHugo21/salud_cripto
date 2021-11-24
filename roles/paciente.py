'''Clase que contiene el rol "Paciente". Capaz de ver sus pacientes y crear nuevos pacientes'''

# Imports
from jsonmethods import JsonMethods
from interfaces.stringinterfaz import StringInterfaz


class Paciente:
    def __init__(self, id, key, iv, salt, expediente):
        '''Inicializa los atributos del paciente'''
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente

    def mi_informe(self):
        '''Accede a los datos del paciente seleccionado'''
        data = JsonMethods.leer_txt('BBDD/' + self.__salt.hex() + '.txt', self.__key, self.__iv)
        StringInterfaz.ficha_paciente(data)
        return 0

    def mis_recetas(self):
        '''Método que permite ver las recetas asociadas al paciente. Utiliza cifrado asimétrico'''
        pass