"""
APP PARA IMPLEMENTAR LAS OPCIONES DE CRIPTOGRAFIA - ENTREGABLE 1
Ejecutable principal que inicia la interfaz de la aplicación

Autores: Juan Franco Labarra 100429065 y Hugo García Cuesta 100428954
"""


# Imports
from interfaces.interfaz import Interfaz
from add_super import MaxSuper
# Inicio de la aplicación
aux = False
if aux == True:
    MaxSuper.add_super()
else:
    app = Interfaz()
