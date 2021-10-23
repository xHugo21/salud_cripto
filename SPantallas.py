

class Pantallas:

    @classmethod
    def PPrincipal(cls):
        print('BIENVENIDO\n')
        print('¿Que desea hacer?\n'
              '0. salir\n'
              '1. Iniciar sesion\n')
        return 0

    @classmethod
    def error(cls):
        raise 'Se ha producido un error'

    @classmethod
    def mensaje_salida(cls):
        print('Saliendo del sistema\n')

