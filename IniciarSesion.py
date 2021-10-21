
from json_things.json import Json


class IniciarSesion:
    def __init__(self):
        self.__ruta = '/json/cuentas.json'

    @staticmethod
    def iniciar_sesion():
        datos = Json.datos_iniciar_sesion()
        existe = False
        intentos = 0
        while existe == False and intentos <3:
            id = input('Insertar id valido '+ str(3-intentos) + ' intentos restantes ->')
            for i in range(len(datos)):
                if int(id) == int(datos[i]["ID"]):
                    existe = True
            intentos += 1
        if existe == False:
            return -1
        existe = False
        intentos = 0
        while existe == False and intentos < 3:
            id = input('Insertar password valida ' + str(3 - intentos) + ' intentos restantes ->')
            for i in range(len(datos)):
                if int(id) == int(datos[i]["PW"]):
                    existe = True
                    perfil = i
            intentos += 1
        if existe == False:
            return -1
        return datos[perfil]


