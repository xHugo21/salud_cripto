'''Clase que controla el inicio de sesión.'''

# Imports
from json_things.jsonmethods import JsonMethods
import json
from checks import Checks
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class IniciarSesion:

    @staticmethod
    def inicio_sesion():
        '''Gestiona el inicio de sesión. Devuelve la posición del usuario en caso de encontrarlo o None en caso contrario.'''

        ruta = 'BBDD/usuarios.json'  # Ruta al archivo json que almacena los usuarios

        # Abrimos el json y guardamos el contenido en data
        json_file = open(ruta)
        data = json.load(json_file)

        # Variables de control
        existe = False
        intentos = 0
        posicion = None

        # Comprobamos si existe (3 intentos)
        while existe is False and intentos < 3:
            id = input('\tEscriba su ID (' + str(3 - intentos) + ' intentos restantes): ')  # Pedir id

            # Comprobar tipo de id es entero
            try:
                id = int(id)
                if isinstance(id, int):
                    # Recorremos el json en busca del usuario
                    for i in range(len(data)):
                        # Si lo encuentra -> existe = True y posicion = i
                        if int(id) == int(data[i]["ID"]):
                            existe = True
                            posicion = i
            # Si no es entero devolver el siguiente mensaje
            except ValueError:
                print("Introduzca un número como ID")

            intentos += 1  # Si no lo ha encontrado aumentamos el número de intentos

        # Si no existe tras pasar el bucle devuelve error
        if existe is False:
            print('\nReinicie la aplicación e inténtelo de nuevo')
            return -1

        # Si llega aquí es que el usuario existe
        salt = Checks.json_bytes(data[posicion]['salt'])
        iv = Checks.json_bytes(data[posicion]['iv'])
        expediente = salt.hex()
        key = IniciarSesion.password(salt)
        if key == -1:
            return -1
        return [salt, iv, expediente, key, id]



    @staticmethod
    def password(salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        pw = input('\tEscriba su contraseña: ')
        key = kdf.derive(str.encode(pw))
        return key
