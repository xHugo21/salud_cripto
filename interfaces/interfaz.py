'''Clase que contiene la interfaz de nuestra aplicación'''

# Imports
from interfaces.stringinterfaz import StringInterfaz
from checks import Checks
from iniciarsesion import IniciarSesion
from json_things.jsonmethods import JsonMethods
from roles.super import Super
import os

'''
from roles.doctor import Doctor
from roles.paciente import Paciente'''


class Interfaz:
    def __init__(self):
        self.bucle_principal()
        self.sujeto = None

    def bucle_principal(self):
        '''Bucle que mantiene la pantalla principal hasta seleccionar 0 (salir)'''

        while True:
            StringInterfaz.mensaje_inicio()  # Selección 1: Salir (0) o Iniciar Sesión (1)
            decision = Checks.check_numero_teclado(1)  # Obtener input

            # Si decision == 0 -> Salir
            if decision == 0:
                StringInterfaz.mensaje_salida()
                break  # Termina ejecución

            # Si decision == 1 -> Iniciar Sesión
            if decision == 1:
                print('\nInicio de sesión')
                aux = IniciarSesion.inicio_sesion()
                salt, iv, expediente, key, id = aux
                ruta = 'BBDD/' + str(expediente) + '.txt'
                data = JsonMethods.leer_txt(ruta, key, iv)
                nombre = data[0]['Nombre'] + ' ' + data[0]['Apellidos']
                if data != -1:
                    if data[0]['Nivel'] == str(2):
                        self.sujeto = Super(id, key, iv, salt, expediente)
                        self.menu_super(nombre)
                    elif data[0]['Nivel'] == str(1):
                        self.sujeto = Super(id, key, iv, salt, expediente)
                        Interfaz.menu_doctor(nombre)
                    elif data[0]['Nivel'] == str(0):
                        self.sujeto = Super(id, key, iv, salt, expediente)
                        Interfaz.menu_paciente(nombre)

    def menu_super(self, nombre):
        '''Menu del rol super'''
        while True:
            StringInterfaz.mensaje_super(nombre)
            decision = Checks.check_numero_teclado(2)  # Obtener input
            # Si decision == 0 -> Log out
            if decision == 0:
                print('\nCerrando sesión\n')
                print('\n' * 80)
                break
            # Si decision == 1 -> Lista doctores
            elif decision == 1:
                while True:
                    aux = self.sujeto.mis_doctores()
                    if aux == -1:
                        break
            # Si decision == 2 -> Añadir doctor
            elif decision == 2:
                self.sujeto.add_doctor()


    def menu_doctor(self, nombre):
        '''Menu del rol doctor'''
        while True:
            StringInterfaz.mensaje_doctor(nombre)
            decision = Checks.check_numero_teclado(2)  # Obtener input
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('\nCerrando sesión\n')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                self.sujeto.mis_doctores()
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                self.sujeto.add_doctor()


    def menu_paciente(self, nombre):
        '''Menu del rol paciente'''
        while True:
            StringInterfaz.mensaje_paciente(nombre)
            decision = Checks.check_numero_teclado(2)  # Obtener input
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('\nCerrando sesión\n')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                self.sujeto.mis_doctores()
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                self.sujeto.add_doctor()





