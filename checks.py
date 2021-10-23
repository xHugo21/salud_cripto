from base64 import b64decode,b64encode
class Checks():
    @classmethod
    def check_numero_teclado(cls, maximum=1):
        input_number = input('0 - ' + str(maximum) + ' ->')
        while not input_number.isnumeric() or int(input_number) not in range(0, maximum+1):
            input_number = input('Escriba un número valido ->')
        input_number = int(input_number)
        return input_number

    @classmethod
    def bytes_json(cls, salt):
        token = b64encode(salt).decode('utf-8')
        print('token', token)
        return token

    @classmethod
    def json_bytes(cls, token):
        salt = b64decode(token)
        return salt

