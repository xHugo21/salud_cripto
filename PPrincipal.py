from SPantallas import Pantallas
from checks import Checks
from IniciarSesion import IniciarSesion

class PPrincipal:
    while True:
        Pantallas.PPrincipal()
        decision = Checks.check_numero_teclado(1)
        if decision == 0:
            Pantallas.mensaje_salida()
            break
        if decision == 1:
            IniciarSesion.inicio_sesion()




