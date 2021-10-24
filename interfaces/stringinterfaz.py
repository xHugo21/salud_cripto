'''Clase que almacena los strings impresos por pantalla en PPrincipal.'''


class StringInterfaz:

    @classmethod
    def mensaje_inicio(cls):
        print('------------------------------')
        print('\tBienvenido a MiSalud')
        print('------------------------------\n')
        print('¿Qué desea hacer?\n'
              '\t0. Salir\n'
              '\t1. Iniciar sesión\n')
        return 0

    @classmethod
    def error(cls):
        raise Exception('Se ha producido un error')

    @classmethod
    def mensaje_salida(cls):
        print('\n------------------------------')
        print('\t   ¡Vuelva pronto!')
        print('------------------------------\n')

