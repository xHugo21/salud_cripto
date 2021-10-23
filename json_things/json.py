import json


class Json:
    @staticmethod
    def datos_iniciar_sesion():
        json_file = open('BBDD/Usuarios.json')
        data = json.load(json_file)
        return data

    @staticmethod
    def sobreescibir_json(data):
        try:
            with open('BBDD/Usuarios.json', "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError as ex:
            raise ("Wrong file or file path") from ex
