'''Clase que contiene el rol "Doctor". Capaz de ver sus pacientes y crear nuevos pacientes'''

# Imports
from interfaces.interfaz import Interfaz
from checks import Checks
from json_things.jsonmethods import JsonMethods


class Doctor:
    def __init__(self, cuenta):
        self.cuenta = cuenta  # JSON que contiene la información del doctor
        self.datos = JsonMethods.obtener_datos(cuenta)  # Almacena los datos del doctor

        # ¿Mover a interfaz.py?
        # Bucle de la interfaz del doctor
        Interfaz.menu_doctor(self)

    def lista_pacientes(self):
        '''Método que devuelve la lista de pacientes asociados al doctor'''
        id_doctor = self.cuenta["ID"]
        contador = 0
        pacientes = []
        for i in range(len(self.datos)):
            if id_doctor == self.datos[i]['Doctor']:
                contador += 1
                pacientes.append(self.datos[i]['ID'])
                print(str(contador) + '. ' + self.datos[i]['Nombre'] + ' ' + self.datos[i]['Apellidos'])
        return pacientes[Checks.check_numero_teclado(len(pacientes)) - 1]

    def paciente(self, id_paciente):
        for i in range(len(self.datos)):
            if self.datos[i]['ID'] == id_paciente:
                print(self.datos[i]['Expediente'])
        print('0. Atras')
        Checks.check_numero_teclado(0)

    def buscar_paciente(self):
        '''Método que devuelve un paciente concreto'''
        busqueda = input('buscar: ')
        contador = 0
        pacientes = []
        for i in range(len(self.datos)):
            if (self.cuenta["ID"] == self.datos[i]['Doctor'] and
                    (busqueda == self.datos[i]['Nombre'] or
                     busqueda == self.datos[i]['Apellidos'] or
                     busqueda == self.datos[i]['ID'])):
                contador += 1
                pacientes.append(self.datos[i]['ID'])
                print(str(contador) + '. ' + self.datos[i]['Nombre'] + ' ' + self.datos[i]['Apellidos'])
        return pacientes[Checks.check_numero_teclado(len(pacientes)) - 1]
