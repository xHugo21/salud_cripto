from SPantallas import Pantallas
from checks import Checks
from IniciarSesion import IniciarSesion
from json_things.json import Json

class PPrincipal:
    while True:
        Pantallas.PPrincipal()
        decision = Checks.check_numero_teclado(1)
        if decision == 0:
            Pantallas.mensaje_salida()
            break
        if decision == 1:
            salt, iv, expediente, key = IniciarSesion.inicio_sesion()
            ruta = 'BBDD/' + str(expediente) + '.txt'
            data = Json.leer_txt(ruta, key, iv)
            print(data[0]['Nivel'])




