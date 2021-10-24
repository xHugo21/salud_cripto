'''Clase que contiene el rol "Doctor". Capaz de ver sus pacientes y crear nuevos pacientes'''

# Imports
from checks import Checks
import os
from json_things.jsonmethods import JsonMethods
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from interfaces.stringinterfaz import StringInterfaz


class Doctor:
    def __init__(self, id, key, iv, salt, expediente):
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente

    def add_paciente(self):
        '''Método que permite añadir paciente'''
        print('\nNuevo paciente')
        nombre = input('\tInsertar nombre: ')
        apellidos = input('\tInsertar apellidos: ')
        id = input('\tInsertar ID: ')
        pw = input('\tInsertar contraseña: ')
        informe = input('\tInsertar informe: \n\t')
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
        data = JsonMethods.crear_diccionario_paciente(nombre, apellidos, id, 1, self.__id, informe)
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        new_wrap_key = JsonMethods.añadir_acceso(self.__key, key)
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        data[0]['Acceso'].append([id, new_wrap_key])
        JsonMethods.escribir_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv, data)
        return 0

    def seleccion_paciente(self):
        '''Lista los paciente y devuelve el ID del paciente seleccionado'''
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        Accesos = data[0]['Acceso']
        print('\t0. Atrás')
        for i in range(len(Accesos)):
            print(f'\t{str(i + 1)}. ID: {Accesos[i][0]}')
        decision = Checks.check_numero_teclado(len(Accesos))
        if decision == 0:
            return -1
        id_seleccion = Accesos[decision - 1]
        return id_seleccion

    def mis_pacientes(self):
        '''Accede a los datos del paciente seleccionado'''
        print('\nSeleccione el paciente')
        id_seleccion = self.seleccion_paciente()
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
        StringInterfaz.ficha_paciente(data)
        return 0

    def borrar_paciente(self):
        '''Método que permite borrar paciente'''
        print('\nSeleccione el paciente para borrar')
        ruta = 'BBDD/usuarios.json'
        data = JsonMethods.obtener_datos(ruta)
        id_seleccion = self.seleccion_paciente()
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