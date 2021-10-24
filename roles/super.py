'''Clase que contiene el rol "Super". Es el rol con más permisos y se le permite añadir y eliminar doctores'''

# Imports
from checks import Checks
import os
from json_things.jsonmethods import JsonMethods
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


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
        data = JsonMethods.crear_diccionario(nombre, apellidos, id, 2)
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        new_wrap_key = JsonMethods.añadir_acceso(self.__key, key)
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        print(data)
        data[0]['Acceso'].append([id, new_wrap_key])
        print(data)
        JsonMethods.escribir_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv, data)
        return 0

    def lista_doctores(self):
        print('Seleccione el doctor')
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        Accesos = data[0]['Acceso']
        print('\t0. Atrás')
        for i in range(len(Accesos)):
            print(f'\t{str(i+1)}. ID: {Accesos[i][0]}')
        decision = Checks.check_numero_teclado(len(Accesos))
        print('decision, ', decision)
        if decision == 0:
            return -1
        id_seleccion = Accesos[decision-1]
        return id_seleccion

    def mis_doctores(self):
        '''Accede a los datos del doctor seleccionado'''
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
        #interfaz.mostrar_informe(data)
        print(data)
