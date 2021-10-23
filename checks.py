'''Clase que contiene los checks (comprobaciones) necesarios para la interfaz.'''

# Imports
from base64 import b64decode,b64encode


class Checks:

    @classmethod
    def check_numero_teclado(cls, maximum=1):
        input_number = input('[0 - ' + str(maximum) + ']: ')  # Mensaje input

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

