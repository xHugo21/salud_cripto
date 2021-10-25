'''import os
import json
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
json_file = open("json_things/pruebas.json")
data = str(json.load(json_file))
print(type(data))
add = b'Aqui estamos'
pri
key = ChaCha20Poly1305.generate_key()
print(key)
chacha = ChaCha20Poly1305(key)
print(chacha)
nonce = os.urandom(12)
print(nonce)
nonce = os.urandom(12)
print(nonce)
nonce = os.urandom(12)
print(nonce)
ct = chacha.encrypt(nonce, data, add)
print(ct)
auix = chacha.decrypt(nonce, ct, add)
print(auix)'''

'''import base64

binarydata = b'MN\\\xde\xa1'
import json
json_file = open("json_things/pruebas.json")
hola = str(json.load(json_file))
hola = 'La'
codificao = str.encode(hola)
print(codificao)
print(codificao.decode())
() #Converting byte-like data to hex
#print("Hex string hex_binarydata =", hex_binarydata)
#print("Bytes from hex string", bytes.fromhex(hex_binarydata))

b64_binarydata = base64.b64encode(codificao) #Converting byte-like data to B64 string
print("Base64 string b64_binarydata =", b64_binarydata)
print("Base64 Decoding b64_binarydata", base64.b64decode(b64_binarydata))

b64url_binarydata = base64.urlsafe_b64encode(codificao) #Converting byte-like data to URL safe B64 string
print("Base64url string b64url_binarydata =", b64url_binarydata)
print("Base64url Decoding b64url_binarydata", base64.urlsafe_b64decode(b64url_binarydata))
'''
'''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import json
import base64
from checks import Checks
json_file = open("json_things/pruebas.json")
Palabra = 'Secreto'
codificao = base64.urlsafe_b64encode(str.encode(Palabra))
print('codifiaco', codificao)
salt = os.urandom(16)
print('salt1', salt)
salt2 = Checks.json_bytes(Checks.bytes_json(salt))
print('salt2', salt2)
print(salt== salt2)
# derive
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = kdf.derive(str.encode('admin'))
print('key', key)

# verify
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt2,
    iterations=100000,
)
print('key2', key)
kdf.verify(str.encode('admin'), key)

iv = os.urandom(16)
print('iv', iv)
cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(codificao) + encryptor.finalize()
print(ct)
#key = os.urandom(32)
paco = Cipher(algorithms.AES(key), modes.CTR(iv))
decryptor = paco.decryptor()
fin = decryptor.update(ct) + decryptor.finalize()
print('fin', fin)
print('decode', base64.urlsafe_b64decode(fin).decode())
'''
'''
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
salt = os.urandom(16)
print(salt)
salt = b"]\x00\x97\xa8uiL\xf7\x89,\xf1\xed'\xa3\xf8\x85"
# derive
kdf = Scrypt(
    salt=salt,
    length=128,
    n=2**14,
    r=8,
    p=1,
)
key = kdf.derive(b"my great password")
print(key)
# verify
kdf = Scrypt(
    salt=salt,
    length=128,
    n=2**14,
    r=8,
    p=1,
)
a = kdf.verify(b"my great password", key)
print(a)

from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
print(digest)
print(digest.update(b"abc"))
a  = digest.copy()
print(digest.finalize())
print(a.finalize())
b'l\xa1=R\xcap\xc8\x83\xe0\xf0\xbb\x10\x1eBZ\x89\xe8bM\xe5\x1d\xb2\xd29%\x93\xafj\x84\x11\x80\x90'

'''
'''
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# Salts should be randomly generated
salt = os.urandom(16)
print(hashes.SHA256())
print(hashes.SHA256())
# derive
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = kdf.derive(b"my great password")
print('key2', key)
# verify
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
kdf.verify(b"my great password", key)
'''
from iniciarsesion import IniciarSesion
from json_things.jsonmethods import JsonMethods
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import json
import ast
'''salt, iv, expedinte, key = IniciarSesion.inicio_sesion()
ruta = 'BBDD/'+str(expedinte)+'.json'
data = Json.datos_iniciar_sesion(ruta)
data64 = base64.urlsafe_b64encode(str.encode(str(data)))
print(data64)
data1 = base64.urlsafe_b64decode(data64).decode()
print(data1)
#Json.sobreescibir_json()'''
'''ruta = 'BBDD/usuarios.json'
data = Json.datos_iniciar_sesion(ruta)
print( type(data))
#Json.sobreescibir_json(data, ruta)
data64 = base64.urlsafe_b64encode(str.encode(str(data))).decode('utf-8')
data1 = base64.urlsafe_b64decode(data64).decode()
Json.escribit_txt('BBDD/aqui.txt', str(data64))
data = Json.leer_txt('BBDD/aqui.txt')
print(data)
data1 = base64.urlsafe_b64decode(data).decode()
print(data1)

data = ast.literal_eval(data1)
print(type(data))'''
'''data = JsonMethods.obtener_datos('json_things/pruebas.json')
print(data)
print(type(data))
print(data[0]['ID'])
data[0]['ID'] = 23456789
salt, iv, expedinte, key = IniciarSesion.inicio_sesion()
JsonMethods.escribir_txt('BBDD/2b1cddc11e325b1abd68dad5bb4a2429ff2e48214b351fd1e5138e8b2d1c801c.txt', key, iv, data)
data1 = JsonMethods.leer_txt('BBDD/2b1cddc11e325b1abd68dad5bb4a2429ff2e48214b351fd1e5138e8b2d1c801c.txt', key, iv)
print(data)
print('tipo int:', type(data))
print(data == data1)'''
'''ruta = 'BBDD/usuarios.json'
data = Json.datos_iniciar_sesion('json_things/pruebas.json')
data = base64.urlsafe_b64encode(str.encode(str(data))).decode('utf-8').encode()
print('data', data)
salt, iv, expedinte, key = IniciarSesion.inicio_sesion()
cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
encryptor = cipher.encryptor()
data = encryptor.update(data) + encryptor.finalize()
print('data', data)'''
salt, iv, expediente, key, id = IniciarSesion.inicio_sesion()
data = JsonMethods.leer_txt('BBDD/' + expediente + '.txt', key, iv)
print(data)
data[0]['Acceso'] = []
print(data)
JsonMethods.escribir_txt('BBDD/' + expediente + '.txt', key, iv, data)

