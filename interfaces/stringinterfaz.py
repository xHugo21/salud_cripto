'''Clase que almacena los strings impresos por pantalla en PPrincipal.'''


class StringInterfaz:

    @staticmethod
    def mensaje_inicio():
        print('------------------------------')
        print('\tBienvenido a MiSalud')
        print('------------------------------\n')
        print('¿Qué desea hacer?\n'
              '\t0. Salir\n'
              '\t1. Iniciar sesión')

    @staticmethod
    def mensaje_super(nombre):
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Super]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Lista doctores\n'
              '\t2. Añadir doctor')

    @staticmethod
    def mensaje_doctor(nombre):
        print('\n' * 80)
        print('\nSe ha identificado como ' + nombre + ' [Doctor]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Mis pacientes\n'
              '\t2. Añadir paciente')

    @staticmethod
    def mensaje_paciente(nombre):
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Paciente]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. ¿Mi doctor?\n'
              '\t2. Mi informe médico')

    @staticmethod
    def informe_doctor(data):
        pass

    @staticmethod
    def informe_paciente(data):
        pass


    @staticmethod
    def mensaje_salida():
        print('\n' * 80)
        print('------------------------------')
        print('\t   ¡Vuelva pronto!')
        print('------------------------------')


