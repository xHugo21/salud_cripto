'''Clase que contiene métodos para manejar los archivos JSON'''

# Imports
import json
import base64
import ast
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from checks import Checks
from cryptography.hazmat.primitives.keywrap import aes_key_wrap,aes_key_unwrap


class JsonMethods:
    def __init__(self):
        self.obtener_datos()
        self.sobreescibir_json()

    @staticmethod
    def obtener_datos(ruta):
        '''Método que devuelve los datos almacenados en el JSON introducido en "ruta"'''
        json_file = open(ruta)
        data = json.load(json_file)
        return data

    @staticmethod
    def sobreescibir_json(data, ruta):
        '''Método que sobreescribe el contenido de un archivo JSON'''
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError as ex:
            raise Exception("Wrong file or file path") from ex

    @staticmethod
    def leer_txt(ruta, key, iv):
        '''Método que permite leer un archivo .txt encriptado'''
        f = open(ruta, 'r')
        data = f.read()
        f.close()
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        decryptor = cipher.decryptor()
        fin = decryptor.update(base64.urlsafe_b64decode(data)) + decryptor.finalize()
        try:
            data = fin.decode()
        except UnicodeDecodeError:
            print('No es correcta la contraseña')
            return -1
        data = ast.literal_eval(data)
        return data

    @staticmethod
    def escribir_txt(ruta, key, iv, data):
        '''Método que permite escribir un archivo .txt encriptándolo'''
        f = open(ruta, 'w')
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        encryptor = cipher.encryptor()
        data = encryptor.update(str(data).encode()) + encryptor.finalize()
        data64 = base64.urlsafe_b64encode(data).decode('utf-8')
        f.write(data64)
        f.close()
        return 0

    @staticmethod
    def crear_expediente(salt):
        '''Método que permite crear un expediente'''
        expediente = salt.hex()
        ruta = 'BBDD/'+str(expediente)+'.txt'
        f = open(ruta, 'w')
        f.close()

    @staticmethod
    def crear_diccionario_doctor(nombre, apellidos, id, nivel):
        '''Método que crea el diccionario de un doctor'''
        data = [{"Nombre": nombre,
                   "Apellidos": apellidos,
                   "ID": id,
                   "Nivel": str(nivel),
                   "Acceso": []}]
        return data

    @staticmethod
    def crear_diccionario_paciente(nombre, apellidos, id, nivel, id_doctor, informe):
        '''Método que crea el diccionario de un paciente'''
        data = [{"Nombre": nombre,
                 "Apellidos": apellidos,
                 "ID": id,
                 "Nivel": str(nivel),
                 "ID_Doctor": id_doctor,
                 "Informe": [informe]}]
        return data

    def add_usuario(self, id, salt, iv):
        '''Método que añade un usuario del JSON de usuarios'''
        ruta = 'BBDD/usuarios.json'
        data = self.obtener_datos(ruta)
        aux = {
            "ID": id,
            "salt": Checks.bytes_json(salt),
            "iv": Checks.bytes_json(iv)
        }
        data.append(aux)
        self.sobreescibir_json(data, ruta)
        return 0

    def delete_usuario(self, id):
        '''Método que elimina un usuario del JSON de usuarios'''
        ruta = 'BBDD/usuarios.json'
        data = self.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                print('pop', data.pop(i))
        self.sobreescibir_json(data, ruta)
        return 0

    @staticmethod
    def add_acceso(wrapping_key, key_to_wrap):
        '''Método que hace wrap de la key introducida empleando la wrapping_key'''
        new_key = aes_key_wrap(wrapping_key, key_to_wrap)
        return new_key

    @staticmethod
    def leer_acceso(wrapping_key, wrapped_key):
        '''Método que hace unwrap de la key introducida empleando la wrapping_key'''
        return_key = aes_key_unwrap(wrapping_key, wrapped_key)
        return return_key


