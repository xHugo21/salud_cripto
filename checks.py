
class Checks():
    @classmethod
    def check_numero_teclado(cls, maximum=1):
        input_number = input('0 - ' + str(maximum) + ' ->')
        while not input_number.isnumeric() or int(input_number) not in range(0, maximum+1):
            input_number = input('Escriba un número valido ->')
        input_number = int(input_number)
        return input_number
