'''Clase que contiene los checks (comprobaciones) necesarios para la interfaz.'''

# Imports
from base64 import b64decode,b64encode


class Checks:

    @classmethod
    def check_numero_teclado(cls, maximum=1):
        '''Permite al usuario seleccionar opciones y las comprueba'''
        # Si hay más de una opción
        if maximum > 0:
            input_number = input('[0 - ' + str(maximum) + ']: ')  # Mensaje input
        # Si solo hay una opción
        else:
            input_number = input('[0]: ')  # Mensaje input

        # Check de valores correctos
        while not input_number.isnumeric() or int(input_number) not in range(0, maximum+1):
            print('\nPor favor, escriba un número válido')
            input_number = input('[0 - ' + str(maximum) + ']: ')

        input_number = int(input_number)  # Conversión a entero
        return input_number

    @classmethod
    def bytes_json(cls, salt):
        token = b64encode(salt).decode('utf-8')
        return token

    @classmethod
    def json_bytes(cls, token):
        salt = b64decode(token)
        return salt

    @classmethod
    def json_bytes_recetas(cls, receta):
        return str(receta).encode()

