'''Clase que contiene métodos para manejar los archivos JSON'''

# Imports
import json
import base64
import ast
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class JsonMethods:
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
        '''Método que permite leer un archivo .txt'''
        f = open(ruta, 'r')
        data = f.read()
        f.close()
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        decryptor = cipher.decryptor()
        fin = decryptor.update(base64.urlsafe_b64decode(data)) + decryptor.finalize()
        data = ast.literal_eval(fin.decode())
        return data

    @staticmethod
    def escribir_txt(ruta, key, iv, data):
        '''Método que permite escribir un archivo .txt'''
        f = open(ruta, 'w')
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        encryptor = cipher.encryptor()
        data = encryptor.update(str(data).encode()) + encryptor.finalize()
        data64 = base64.urlsafe_b64encode(data).decode('utf-8')
        f.write(data64)
        f.close()
        return 0

