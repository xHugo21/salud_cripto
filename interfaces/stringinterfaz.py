'''Clase que almacena los strings impresos por pantalla en PPrincipal.'''


class StringInterfaz:

    @staticmethod
    def bucle_inicio():
        '''String mostrado al iniciar la aplicación'''
        print('------------------------------')
        print('\tBienvenido a MiSalud')
        print('------------------------------\n')
        print('¿Qué desea hacer?\n'
              '\t0. Salir\n'
              '\t1. Iniciar sesión')

    @staticmethod
    def bucle_super(nombre):
        '''String mostrado al iniciar sesión como super'''
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Super]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Lista doctores\n'
              '\t2. Añadir doctor\n'
              '\t3. Borrar doctor')

    @staticmethod
    def bucle_doctor(nombre):
        '''String mostrado al iniciar sesión como doctor'''
        print('\n' * 80)
        print('\nSe ha identificado como ' + nombre + ' [Doctor]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Lista pacientes\n'
              '\t2. Añadir paciente\n'
              '\t3. Borrar paciente\n'
              '\t4. Añadir informe')

    @staticmethod
    def bucle_paciente(nombre):
        '''String mostrado al iniciar sesión como paciente'''
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Paciente]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Mis informes')

    @staticmethod
    def ficha_doctor(data):
        '''String que muestra la ficha de uno de los doctores al seleccionarlo desde la lista de doctores de super'''
        print(f'\nFicha del doctor {data[0]["Nombre"]} {data[0]["Apellidos"]}')
        print(f'\tID: {data[0]["ID"]}')
        print(f'\tPacientes asociados: ')
        for i in range(len(data[0]['Acceso'])):
            print(f'\t\t {data[0]["Acceso"][i][0]}')



    @staticmethod
    def ficha_paciente(data):
        '''String que muestra la ficha de uno de los pacientes al seleccionarlo desde la lista de pacientes de un doctor'''
        print(f'\nFicha del paciente {data[0]["Nombre"]} {data[0]["Apellidos"]}')
        print(f'\tID: {data[0]["ID"]}')
        print(f'\tDoctor asociado: {data[0]["ID_Doctor"]}')
        print('\tInformes:')
        for i in range(len(data[0]['Informe'])):
            print(f'\t\t {data[0]["Informe"][i]}')



    @staticmethod
    def mensaje_salida():
        '''String mostrado al salir (introducir 0) desde el menú inicial de la aplicación'''
        print('\n' * 80)
        print('------------------------------')
        print('\t   ¡Vuelva pronto!')
        print('------------------------------')


