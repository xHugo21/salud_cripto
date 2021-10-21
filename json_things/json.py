


class Json:
    @staticmethod
    def datos_iniciar_sesion():
        json_file = open("C:/Users/jfran/PycharmProjects/app-cripto/json_things/cuentas.json")
        data = json.load(json_file)
        return data
