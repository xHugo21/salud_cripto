'''
APP PARA IMPLEMENTAR LAS OPCIONES DE CRIPTOGRAFIA - ENTREGABLE 1
La app consiste en un sistema, usado mediante la propia terminal de windows, consistirá en el acceso por parte de
tanto médicos como pacintes a los datos propios de estos últimos, dependiendo del acceso que tenga cada uno.
De esta forma podemos gestionar los accesos dependiendo del acceso que tenga cada médico y cada paciente para que
unicamente acceda a la mínima cantidad de datos necesaria
'''

'''Ejecutable principal que inicia la interfaz de la aplicación'''

'''
Autores: Juan Franco Labarra 100429065 y Hugo García Cuesta 100428954
'''

'''
COMENTARIOS Y TODO'S: Al devolver error al escribir el ID de usuario se debe reiniciar el bucle. Solución: que inicio_sesion devuelva solo la posicion y salt, iv, expediente y key se generen en otro método
Interfaz dentro de la clase Doctor mover a interfaz.py?
Interfaz dentro de la clase Super mover a interfaz.py?
Cambiar directorio json_things a python package?
'''

# Imports
from interfaces.interfaz import Interfaz

# Inicio de la aplicación
app = Interfaz()
