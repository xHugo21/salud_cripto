from checks import Checks
import os
from jsonmethods import JsonMethods
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class MaxSuper:
    @staticmethod
    def add_super():
        print('\nNuevo Super')
        nombre = input('\tInsertar nombre: ')
        apellidos = input('\tInsertar apellidos: ')
        id = input('\tInsertar ID: ')
        if JsonMethods.control_usuarios(id) == -1:
            return -1
        pw = input('\tInsertar contraseña: ')
        salt = os.urandom(16)
        iv = os.urandom(16)
        JsonMethods.crear_expediente(salt)
        JsonMethods.add_usuario(id, salt, iv)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        expediente = salt.hex()
        new_ruta = 'BBDD/' + str(expediente) + '.txt'
        key = kdf.derive(pw.encode())
        data = JsonMethods.crear_diccionario_doctor(nombre, apellidos, id, 2)
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        print('TODO OK JOSE LUIS')
        return 0
