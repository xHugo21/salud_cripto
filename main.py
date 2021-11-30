"""
APP PARA IMPLEMENTAR LAS OPCIONES DE CRIPTOGRAFIA - ENTREGABLE 1
Ejecutable principal que inicia la interfaz de la aplicación

Autores: Juan Franco Labarra 100429065 y Hugo García Cuesta 100428954
"""


# Imports
from interfaces.interfaz import Interfaz
from add_super import MaxSuper
from pki import Pki
from interfaces.stringinterfaz import StringInterfaz

aux = False
# Si aux == True -> Función para crear super. Si super ya está creado -> inicia aplicación
if aux == True:
    MaxSuper.add_super()

# Inicio de la aplicación
else:
    if (Pki.check_certificados() == 0 and
    Pki.verificar_super() == 0):
        app = Interfaz()
    else:
        StringInterfaz.mensaje_salida()
