'''Clase que contiene el rol "Doctor". Capaz de ver sus pacientes y crear nuevos pacientes'''

# Imports
from checks import Checks
import os
from jsonmethods import JsonMethods
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from interfaces.stringinterfaz import StringInterfaz
from datetime import date
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.serialization import load_pem_private_key

class Doctor:
    def __init__(self, id, key, iv, salt, expediente, nombre_doctor, private_key):
        '''Inicializa los atributos del doctor'''
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente
        self.__nombre_doctor = nombre_doctor
        self.__private_key = private_key

    def add_paciente(self):
        '''Método que permite añadir un paciente nuevo'''
        print('\nNuevo paciente')
        nombre = input('\tInsertar nombre: ')
        apellidos = input('\tInsertar apellidos: ')
        id = input('\tInsertar ID: ')
        if JsonMethods.control_usuarios(id) == -1:
            return -1
        pw = input('\tInsertar contraseña: ')
        today = date.today()
        day = today.strftime("%b-%d-%Y")
        informe = day + ' -> ' + input('\tInsertar informe: \n\t')
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
        doctor = self.__nombre_doctor + ' [' + str(self.__id) + ']'
        data = JsonMethods.crear_diccionario_paciente(nombre, apellidos, id, 0, doctor, informe)
        JsonMethods.escribir_txt(new_ruta, key, iv, data)
        new_wrap_key = JsonMethods.add_acceso(self.__key, key)
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        data[0]['Acceso'].append([id, new_wrap_key])
        JsonMethods.escribir_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv, data)
        return 0

    def seleccion_paciente(self):
        '''Lista los pacientes y devuelve el ID del paciente seleccionado'''
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        accesos = data[0]['Acceso']
        print('\t0. Atrás')
        for i in range(len(accesos)):
            print(f'\t{str(i + 1)}. ID: {accesos[i][0]}')
        decision = Checks.check_numero_teclado(len(accesos))
        if decision == 0:
            return -1
        id_seleccion = accesos[decision - 1]
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
        '''Método que permite borrar un paciente'''
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

    def add_informe(self):
        '''Metodo que permite añadir un nuevo informe a un paciente'''
        print('\nSeleccione el paciente al que quiere añadir un informe')
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
        today = date.today()
        day = today.strftime("%b-%d-%Y")
        informe = day + ' -> ' + input('\tInsertar informe: \n\t')
        data[0]['Informe'].append(informe)
        JsonMethods.escribir_txt('BBDD/' + salt.hex() + '.txt', key, iv, data)
        return 0

    def dispensar_receta(self):
        '''Metodo que permite a un doctor dispensar una receta para un paciente. Se emplea cifrado asimétrico.'''
        print('\nSeleccione el paciente al que quiere añadir una receta')
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
        today = date.today()
        day = today.strftime("%b-%d-%Y")
        id_nueva_receta = 'R' + data[0]["ID"] + str(len(data[0]["Recetas"]))
        medicamento = input('\tInsertar medicamento: \n\t')
        tratamiento = input('\tInsertar tratamiento: \n\t')
        receta = [{"Id_receta": id_nueva_receta,
                   "Paciente": data[0]["Nombre"] + ' ' + data[0]["Apellidos"],
                   "Doctor": self.__nombre_doctor,
                   "Fecha": day,
                   "Medicamento": medicamento,
                   "Tratamiento": tratamiento}]
        receta_bytes = [id_nueva_receta, receta, self.generate_signature(receta, id_nueva_receta)]
        data[0]['Recetas'].append(receta_bytes)
        JsonMethods.escribir_txt('BBDD/' + salt.hex() + '.txt', key, iv, data)
        return 0

    def generate_signature(self, receta, id_receta):
        private_key_bytes = b64decode(self.__private_key)
        private_key = load_pem_private_key(private_key_bytes, None)
        receta_bytes = str(receta).encode()
        signature = private_key.sign(receta_bytes, ec.ECDSA(hashes.SHA256()))
        public_key = private_key.public_key()
        public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
        public_key_bytes = b64encode(public_key_bytes).decode('utf-8')
        JsonMethods.add_publickey(id_receta, public_key_bytes)
        return signature
