# APP PARA IMPLEMENTAR LAS OPCIONES DE CRIPTOGRAFIA
# La app consiste en un sistema, usado mediante la propia terminal de windows, consistirá en el acceso por parte de
# tanto médicos como pacintes a los datos propios de estos últimos, dependiendo del acceso que tenga cada uno.
# De esta forma podemos gestionar los accesos dependiendo del acceso que tenga cada médico y cada paciente para que
# unicamente acceda a la mínima cantidad de datos necesaria
from checks import Checks
from IniciarSesion import IniciarSesion
from Doctor import Doctor
from super import Super


class PantallaPrincipal:
    while True:
        print('BIENVENIDO')
        print('¿Que desea hacer?\n'
              '0. salir\n'
              '1. Iniciar sesion\n')
        decision = Checks.check_numero_teclado(1)
        if decision == 0:
            print('SALIENDD DEL SISTEMA')
            break
        if decision == 1:
            print('INICIAR SESIÓN')
            sesion = IniciarSesion.iniciar_sesion()
            if sesion == -1:
                print('error')
            elif int(sesion['Nivel']) == 0:
                print(sesion['Expediente'])
                print('0. Atras')
                Checks.check_numero_teclado(0)
            elif int(sesion['Nivel']) == 1:
                Doctor(sesion)
            elif int(sesion['Nivel']) == 2:
                Super(sesion)



