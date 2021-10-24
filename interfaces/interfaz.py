'''Clase que contiene la interfaz de nuestra aplicación'''

# Imports
from interfaces.stringinterfaz import StringInterfaz
from checks import Checks
from iniciarsesion import IniciarSesion
from json_things.jsonmethods import JsonMethods
from roles.super import Super
'''
from roles.doctor import Doctor
from roles.paciente import Paciente'''


class Interfaz:
    def __init__(self):
        self.bucle_principal()
        self.sujeto = 0

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
                        Interfaz.menu_doctor()
                    elif data[0]['Nivel'] == str(0):
                        self.sujeto = Super(id, key, iv, salt, expediente)
                        Interfaz.menu_paciente()

    def menu_super(self, nombre):
        '''Menu del rol super'''
        while True:
            print('BIENVENIDO ' + nombre)
            print('¿Qué desea hacer?\n'
                  '0. Log out\n'
                  '1. Mis doctores\n'
                  '2. Añadir doctor\n')
            decision = Checks.check_numero_teclado(2)  # Obtener input
            print(decision)
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('Atrás')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                super.paciente(super.lista_pacientes())
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                self.sujeto.añadir_medico()


    @staticmethod
    def menu_doctor(doctor):
        '''Menu del rol doctor'''
        while True:
            print('BIENVENIDO ' + doctor.cuenta['Nombre'] + ' ' + doctor.cuenta["Apellidos"])
            print('¿Qué desea hacer?\n'
                  '0. Log out\n'
                  '1. Mis pacientes\n'
                  '2. Buscar paciente\n')
            decision = Checks.check_numero_teclado(2)  # Obtener input
            print(decision)
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('Atrás')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                print('aqui')
                doctor.paciente(doctor.lista_pacientes())
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                doctor.paciente(doctor.buscar_paciente())
    @staticmethod
    def menu_paciente(paciente):
        '''Menu del rol paciente'''
        while True:
            print('BIENVENIDO ' + paciente.cuenta['Nombre'] + ' ' + paciente.cuenta["Apellidos"])
            print('¿Qué desea hacer?\n'
                  '0. Log out\n'
                  '1. Mis pacientes\n'
                  '2. Buscar paciente\n')
            decision = Checks.check_numero_teclado(2)  # Obtener input
            print(decision)
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('Atrás')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                print('aqui')
                paciente.paciente(paciente.lista_pacientes())
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                paciente.paciente(paciente.buscar_paciente())





