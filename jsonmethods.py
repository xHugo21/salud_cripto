'''Clase que contiene métodos para manejar los archivos JSON'''

# Imports
import hmac
import json
import base64
import ast
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from checks import Checks
from cryptography.hazmat.primitives.keywrap import aes_key_wrap,aes_key_unwrap
from cryptography.hazmat.primitives import hashes
import cryptography.hazmat.primitives.hmac as hmac_u
from cryptography.exceptions import InvalidSignature


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
        sep = b'??a??'
        data = f.read()
        f.close()
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        decryptor = cipher.decryptor()
        fin = base64.urlsafe_b64decode(data)
        dataf = fin[:fin.index(sep)]
        hmacf = fin[(fin.index(sep) + 5):]
        h = hmac_u.HMAC(key, hashes.SHA256())
        h.update(dataf)
        #dataf = fin #quitar esta linea
        try:
            h.verify(hmacf)
        except InvalidSignature:
            print('No es correcta la contraseña (HMAC)')
            return -1

        fin = decryptor.update(dataf) + decryptor.finalize()
        try:
            data = fin.decode()
        except UnicodeDecodeError:
            print('No es correcta la contraseña')
            return -1
        data = ast.literal_eval(data)
        print('Desencriptado con AES256 con modo CTR, longitud de clave: 32')
        print('Generado: ', data)
        return data


    @staticmethod
    def escribir_txt(ruta, key, iv, data):
        sep = b'??a??'
        '''Método que permite escribir un archivo .txt encriptándolo'''
        f = open(ruta, 'w')
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        encryptor = cipher.encryptor()
        data = encryptor.update(str(data).encode()) + encryptor.finalize()

        h = hmac_u.HMAC(key, hashes.SHA256())
        h.update(data)
        hmac = h.finalize()
        data64 = base64.urlsafe_b64encode(data + sep + hmac).decode('utf-8')

        #data64 = base64.urlsafe_b64encode(data).decode('utf-8')
        f.write(data64)
        f.close()
        print('Encriptado con AES256 con modo CTR, longitud de clave: 32')
        print('Generado: ', data64)
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
        print(data)
        return data

    @staticmethod
    def crear_diccionario_paciente(nombre, apellidos, id, nivel, id_doctor, informe):
        '''Método que crea el diccionario de un paciente'''
        data = [{"Nombre": nombre,
                 "Apellidos": apellidos,
                 "ID": id,
                 "Nivel": str(nivel),
                 "ID_Doctor": id_doctor,
                 "Informe": [informe],
                 "Recetas": []}]
        return data

    @classmethod
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

    @classmethod
    def add_publickey(self, id_receta, key):
        '''Método que añade una clave publica al JSON de claves publicas'''
        ruta = 'BBDD/publickeys.json'
        data = self.obtener_datos(ruta)
        aux = {
            "ID_receta": id_receta,
            "PublicKey": key
        }
        data.append(aux)
        self.sobreescibir_json(data, ruta)
        return 0

    @classmethod
    def delete_usuario(self, id):
        '''Método que elimina un usuario del JSON de usuarios'''
        ruta = 'BBDD/usuarios.json'
        data = self.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                data.pop(i)
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

    @classmethod
    def control_usuarios(self, id):
        '''Método que añade un usuario del JSON de usuarios'''
        ruta = 'BBDD/usuarios.json'
        data = self.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                print('Ya existe este paciente, pruebe con otro id')
                return -1
        return 0


