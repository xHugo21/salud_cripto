'''Clase que contiene el rol "Super". Es el rol con más permisos y se le permite añadir y eliminar doctores'''

# Imports
from checks import Checks
import os
from jsonmethods import JsonMethods
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from interfaces.stringinterfaz import StringInterfaz
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from base64 import b64encode


class Super:
    def __init__(self, id, key, iv, salt, expediente):
        '''Inicializa los atributos del super'''
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente

    def add_doctor(self):
        '''Método que permite añadir doctores'''
        print('\nNuevo doctor')
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

        data = JsonMethods.crear_diccionario_doctor(nombre, apellidos, id, 1, self.generate_private_key())
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        new_wrap_key = JsonMethods.add_acceso(self.__key, key)
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        data[0]['Acceso'].append([id, new_wrap_key])
        JsonMethods.escribir_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv, data)
        return 0

    def seleccion_doctor(self):
        '''Lista los doctores y devuelve el ID del doctor seleccionado'''
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        Accesos = data[0]['Acceso']
        print('\t0. Atrás')
        for i in range(len(Accesos)):
            print(f'\t{str(i+1)}. ID: {Accesos[i][0]}')
        decision = Checks.check_numero_teclado(len(Accesos))
        if decision == 0:
            return -1
        id_seleccion = Accesos[decision-1]
        return id_seleccion

    def mis_doctores(self):
        '''Accede a los datos del doctor seleccionado'''
        print('\nSeleccione el doctor')
        id_seleccion = self.seleccion_doctor()
        if id_seleccion == -1:
            return -1
        id = id_seleccion[0]
        wrap_key = id_seleccion[1]
        key = JsonMethods.leer_acceso(self.__key, wrap_key)
        ruta = 'BBDD/usuarios.json'
        data = JsonMethods.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                salt = data[i]['salt']
                iv = data[i]['iv']
        salt = Checks.json_bytes(salt)
        iv = Checks.json_bytes(iv)
        data = JsonMethods.leer_txt('BBDD/' + salt.hex() + '.txt', key, iv)
        StringInterfaz.ficha_doctor(data)
        return 0

    def borrar_medico(self):
        '''Método que permite borrar doctores'''
        print('\nSeleccione el doctor para borrar')
        ruta = 'BBDD/usuarios.json'
        data = JsonMethods.obtener_datos(ruta)
        id_seleccion = self.seleccion_doctor()
        if id_seleccion == -1:
            return -1
        id = id_seleccion[0]
        JsonMethods.delete_usuario(id)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                salt = data[i]['salt']
        expediente = Checks.json_bytes(salt).hex()
        os.remove('BBDD/' + expediente + '.txt')
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        for i in range(len(data[0]['Acceso'])):
            if data[0]['Acceso'][i][0] == id:
                data[0]['Acceso'].pop(i)
        JsonMethods.escribir_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv, data)
        return -1
    @staticmethod
    def generate_private_key():
        private_key = ec.generate_private_key(ec.SECP384R1)
        private_key_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
        private_key_json = b64encode(private_key_bytes).decode('utf-8')

        return private_key_json





