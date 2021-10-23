'''Clase que contiene la interfaz de nuestra aplicación'''

# Imports
from stringinterfaz import StringInterfaz
from checks import Checks
from iniciarsesion import IniciarSesion
from json_things.jsonmethods import JsonMethods


class Interfaz:
    def __init__(self):
        self.bucle_principal()

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
                salt, iv, expediente, key = IniciarSesion.inicio_sesion()
                ruta = 'BBDD/' + str(expediente) + '.txt'
                data = JsonMethods.leer_txt(ruta, key, iv)
                print(data[0]['Nivel'])

    def menu_super(self, super):
        '''Menu del rol super'''
        while True:
            print('BIENVENIDO ' + super.cuenta['Nombre'] + ' ' + super.cuenta["Apellidos"])
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
                super.paciente(super.lista_pacientes())
            # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                super.paciente(super.buscar_paciente())

    def menu_doctor(self, doctor):
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

    def menu_paciente(self, paciente):
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





