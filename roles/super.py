'''Clase que contiene el rol "Super". Es el rol con más permisos y se le permite añadir y eliminar doctores'''

# Imports
from checks import Checks
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from json_things.jsonmethods import JsonMethods


class Super:
    def __init__(self, id, key, iv, salt, expediente):
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente

    def add_doctor(self):
        '''Método que permite añadir doctores'''
        nombre = input('\t Insertar nombre: ')
        apellidos = input('\t Insertar apellidos: ')
        id = input('\t Insertar id: ')
        pw = input('\t Insertar contraseña: ')
        salt = os.urandom(16)
        iv = os.urandom(16)
        JsonMethods.crear_expediente(salt)
        JsonMethods.add_usuario()
        kdf = Scrypt(
            salt=salt,
            length=128,
            n=2 ** 14,
            r=8,
            p=1,
        )
        expediente = salt.hex()
        new_ruta = 'BBDD/' + str(expediente) + '.txt'
        key = kdf.derive(pw.encode())
        data = JsonMethods.crear_diccionario(nombre, apellidos, id, 2)
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        new_wrap_key = JsonMethods.añadir_acceso(self.__key, key)
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        data[0]['Acceso'].append([id, new_wrap_key])
        return 0

    def lista_doctores(self):
        print('Seleccione el doctor')
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        Accesos = data[0]['Acceso']
        for i in range(len(Accesos)):
            print(str(i), '. ID: ', Accesos[i][1])
        decision = Checks.check_numero_teclado(len(Accesos))
        id_seleccion = Accesos[decision]
        return id_seleccion

    def mis_doctores(self):
        id_seleccion = self.lista_doctores()
        id = id_seleccion()[0]
        wrap_key = id_seleccion[1]
        key = JsonMethods.leer_acceso(self.__key, wrap_key)
        ruta = 'BBDD/usuarios.json'
        data = JsonMethods.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]['ID'] == id:
                salt = data[i]['salt']
                iv = data[i]['iv']
        data = JsonMethods.leer_txt(salt.hex(), key, iv)
        print(data)
