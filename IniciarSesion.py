from json_things.json import Json
import json
from checks import Checks
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class IniciarSesion:
    def __init__(self):
        pass

    @staticmethod
    def iniciar_sesion1():
        datos = Json.datos_iniciar_sesion()
        existe = False
        intentos = 0
        while existe == False and intentos < 3:
            id = input('Insertar id valido ' + str(3 - intentos) + ' intentos restantes ->')
            for i in range(len(datos)):
                if int(id) == int(datos[i]["ID"]):
                    existe = True
            intentos += 1
        if existe == False:
            return -1
        existe = False
        intentos = 0
        while existe == False and intentos < 3:
            id = input('Insertar password valida ' + str(3 - intentos) + ' intentos restantes ->')
            for i in range(len(datos)):
                if int(id) == int(datos[i]["PW"]):
                    existe = True
                    perfil = i
            intentos += 1
        if existe == False:
            return -1
        return datos[perfil]

    @staticmethod
    def inicio_sesion():
        ruta = 'BBDD/Usuarios.json'
        json_file = open(ruta)
        data = json.load(json_file)
        data = Json.datos_iniciar_sesion()
        existe = False
        intentos = 0
        while existe == False and intentos < 3:
            id = input('Insertar id\n ' + str(3 - intentos) + ' intentos restantes ->')
            for i in range(len(data)):
                if int(id) == int(data[i]["ID"]):
                    existe = True
                    posicion = i
            intentos += 1
        if existe == False:
            return -1
        # Si llega aqui es que el usuario existe
        salt = Checks.json_bytes(data[posicion]['salt'])
        iv = Checks.json_bytes(data[posicion]['iv'])
        expediente = salt.hex()
        IniciarSesion.contraseña(salt, iv, expediente)
        print(expediente)


    @staticmethod
    def contraseña(salt, iv, expediente):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        pw = input('Escriba su contraseña -> ')
        key = kdf.derive(str.encode(pw))
        return key
