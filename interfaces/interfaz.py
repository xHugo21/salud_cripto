'''Clase que contiene la interfaz de nuestra aplicación'''

# Imports
from interfaces.stringinterfaz import StringInterfaz
from checks import Checks
from iniciarsesion import IniciarSesion
from jsonmethods import JsonMethods
from roles.super import Super
from roles.doctor import Doctor
from roles.paciente import Paciente

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
            StringInterfaz.bucle_inicio()  # Selección 1: Salir (0) o Iniciar Sesión (1)
            decision = Checks.check_numero_teclado(1)  # Obtener input

            # Si decision == 0 -> Salir
            if decision == 0:
                StringInterfaz.mensaje_salida()
                break  # Termina ejecución

            # Si decision == 1 -> Iniciar Sesión
            if decision == 1:
                print('\nInicio de sesión')
                aux = IniciarSesion.inicio_sesion()
                if aux == -1:
                    break # Llamamos a inicio_sesion para comprobar ID y contraseña
                salt, iv, expediente, key, id = aux  # Guardamos los valores devueltos necesarios para la encriptación y funcionamiento de la aplicación
                ruta = 'BBDD/' + str(expediente) + '.txt'
                data = JsonMethods.leer_txt(ruta, key, iv)  # Leemos y desencriptamos el .txt asociado al usuario
                # Si leer_txt() devuelve -1 -> error
                if data == -1:
                    return -1

                # Distinguimos el tipo de usuario que ha iniciado sesión
                nombre = data[0]['Nombre'] + ' ' + data[0]['Apellidos']
                if data != -1:
                    if data[0]['Nivel'] == str(2):
                        self.sujeto = Super(id, key, iv, salt, expediente)  # Crear objeto super y llamar a su menú
                        self.menu_super(nombre)
                    elif data[0]['Nivel'] == str(1):
                        self.sujeto = Doctor(id, key, iv, salt, expediente, nombre)  # Crear objeto doctor y llamar a su menú
                        self.menu_doctor(nombre)
                    elif data[0]['Nivel'] == str(0):
                        self.sujeto = Paciente(id, key, iv, salt, expediente)  # Crear objeto paciente y llamar a su menú
                        self.menu_paciente(nombre)

    def menu_super(self, nombre):
        '''Menu del rol super'''
        while True:
            StringInterfaz.bucle_super(nombre)  # Llamada a string del bucle
            decision = Checks.check_numero_teclado(3)  # Obtener input
            # Si decision == 0 -> Log out
            if decision == 0:
                print('\nCerrando sesión\n')
                print('\n' * 80)
                break

            # Si decision == 1 -> Lista doctores
            elif decision == 1:
                if self.sujeto.mis_doctores() != -1:
                    print('\n\t0. Atrás')
                    Checks.check_numero_teclado(0)

            # Si decision == 2 -> Añadir doctor
            elif decision == 2:
                if self.sujeto.add_doctor() == -1:
                    print('\n\t0. Atrás')
                    Checks.check_numero_teclado(0)

            # Si decision == 3 -> Borrar doctor
            elif decision == 3:
                self.sujeto.borrar_medico()


    def menu_doctor(self, nombre):
        '''Menu del rol doctor'''
        while True:
            StringInterfaz.bucle_doctor(nombre)  # Llamada a string del bucle
            decision = Checks.check_numero_teclado(4)  # Obtener input
            # Si decision == 0 -> Log out
            if decision == 0:
                print('\nCerrando sesión\n')
                print('\n' * 80)
                break

            # Si decision == 1 -> Lista paciente
            elif decision == 1:
                if self.sujeto.mis_pacientes() != -1:
                    print('\n\t0. Atrás')
                    Checks.check_numero_teclado(0)

            # Si decision == 2 -> Añadir paciente
            elif decision == 2:
                if self.sujeto.add_paciente() == -1:
                    print('\n\t0. Atrás')
                    Checks.check_numero_teclado(0)

            # Si decision == 3 -> Borrar paciente
            elif decision == 3:
                self.sujeto.borrar_paciente()

            # Si decision == 4 -> Añadir informe
            elif decision == 4:
                self.sujeto.add_informe()

    def menu_paciente(self, nombre):
        '''Menu del rol paciente'''
        while True:
            StringInterfaz.bucle_paciente(nombre)  # Llamada a string del bucle
            decision = Checks.check_numero_teclado(1)  # Obtener input
            # Si decision == 0 -> Log out
            if decision == 0:
                print('\nCerrando sesión\n')
                break
            # Si decision == 1 -> Mi informe
            elif decision == 1:
                if self.sujeto.mi_informe() != -1:
                    print('\n\t0. Atrás')
                    Checks.check_numero_teclado(0)





