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
                break # Termina ejecución

            # Si decision == 1 -> Iniciar Sesión
            if decision == 1:
                salt, iv, expediente, key = IniciarSesion.inicio_sesion()
                ruta = 'BBDD/' + str(expediente) + '.txt'
                data = JsonMethods.leer_txt(ruta, key, iv)
                print(data[0]['Nivel'])




