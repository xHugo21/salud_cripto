'''Clase que almacena los strings impresos por pantalla en PPrincipal.'''


class StringInterfaz:

    @staticmethod
    def bucle_inicio():
        print('------------------------------')
        print('\tBienvenido a MiSalud')
        print('------------------------------\n')
        print('¿Qué desea hacer?\n'
              '\t0. Salir\n'
              '\t1. Iniciar sesión')

    @staticmethod
    def bucle_super(nombre):
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Super]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Lista doctores\n'
              '\t2. Añadir doctor\n'
              '\t3. Borrar doctor')

    @staticmethod
    def bucle_doctor(nombre):
        print('\n' * 80)
        print('\nSe ha identificado como ' + nombre + ' [Doctor]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Lista pacientes\n'
              '\t2. Añadir paciente\n'
              '\t3. Borrar paciente')

    @staticmethod
    def bucle_paciente(nombre):
        print('\n' * 80)
        print('Se ha identificado como ' + nombre + ' [Paciente]')
        print('\n¿Qué desea hacer?\n'
              '\t0. Log out\n'
              '\t1. Mi informe')

    @staticmethod
    def ficha_doctor(data):
        print(f'\nFicha del doctor {data[0]["Nombre"]} {data[0]["Apellidos"]}')
        print(f'\tID: {data[0]["ID"]}')
        cadena = '['
        for i in range(len(data[0]['Acceso'])):
            cadena = cadena + data[0]['Acceso'][i] + ', '
        cadena = cadena + ']'
        print(f'\tPacientes asociados: {cadena}')


    @staticmethod
    def ficha_paciente(data):
        print(f'\nFicha del paciente {data[0]["Nombre"]} {data[0]["Apellidos"]}')
        print(f'\tID: {data[0]["ID"]}')
        print(f'\tDoctor asociado:{data[0]["ID_Doctor"]}')
        print(f'\tInforme: {data[0]["Informe"]}')



    @staticmethod
    def mensaje_salida():
        print('\n' * 80)
        print('------------------------------')
        print('\t   ¡Vuelva pronto!')
        print('------------------------------')


