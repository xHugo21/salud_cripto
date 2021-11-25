'''Clase que contiene el rol "Paciente". Capaz de ver sus pacientes y crear nuevos pacientes'''

# Imports
from jsonmethods import JsonMethods
from interfaces.stringinterfaz import StringInterfaz
from checks import Checks
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from base64 import b64decode

class Paciente:
    def __init__(self, id, key, iv, salt, expediente):
        '''Inicializa los atributos del paciente'''
        self.__id = id
        self.__key = key
        self.__iv = iv
        self.__salt = salt
        self.__expediente = expediente

    def mi_informe(self):
        '''Accede a los datos del paciente seleccionado'''
        data = JsonMethods.leer_txt('BBDD/' + self.__salt.hex() + '.txt', self.__key, self.__iv)
        StringInterfaz.ficha_paciente(data)
        return 0

    def mis_recetas(self):
        '''Método que permite ver las recetas asociadas al paciente. Utiliza cifrado asimétrico'''
        id_seleccion = self.seleccion_recetas()
        if id_seleccion == -1:
            return -1
        id_receta = id_seleccion[0]
        receta = id_seleccion[1]
        signature = id_seleccion[2]
        StringInterfaz.interfaz_recetas(receta)
        ruta = 'BBDD/publickeys.json'
        data = JsonMethods.obtener_datos(ruta)
        for i in range(len(data)):
            if data[i]["ID_receta"] == id_receta:
                public_key_bytes = data[i]["PublicKey"]
        public_key_new = load_pem_public_key(b64decode(public_key_bytes))
        try:
            data_receta = (str(receta)).encode()
            public_key_new.verify(signature, data_receta, ec.ECDSA(hashes.SHA256()))
        except InvalidSignature:
            print('No se ha podido validar la receta ')
            return -2
        print('Esta receta es valida')

        return 0


    def seleccion_recetas(self):
        '''Lista las recetas y devuelve el id de la receta seleccionada'''
        data = JsonMethods.leer_txt('BBDD/' + self.__expediente + '.txt', self.__key, self.__iv)
        recetas = data[0]['Recetas']
        print('\t0. Atrás')
        for i in range(len(recetas)):
            print(f'\t{str(i + 1)}. ID: {recetas[i][0]}')
        decision = Checks.check_numero_teclado(len(recetas))
        if decision == 0:
            return -1
        id_seleccion = recetas[decision - 1]
        return id_seleccion