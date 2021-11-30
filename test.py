from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat,\
    NoEncryption
from checks import Checks
from cryptography.hazmat.primitives import hashes
from jsonmethods import JsonMethods
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key, load_pem_parameters
from cryptography.exceptions import InvalidSignature
from base64 import b64decode,b64encode
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
import json
from cryptography.hazmat.primitives.asymmetric import padding

'''
receta = [{'hola': 1234}]
private_key = ec.generate_private_key(ec.SECP384R1)
receta_bytes = Checks.json_bytes_recetas(str(receta).encode())
private_key_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
private_key_json = b64encode(private_key_bytes).decode('utf-8')
private_key_bytes = b64decode(private_key_json)
private_key = load_pem_private_key(private_key_bytes, None)
signature = private_key.sign(str(receta).encode(), ec.ECDSA(hashes.SHA256()))
print(type(str(receta).encode()))

public_key = private_key.public_key()

print('public_key')
print(public_key)
public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
public_key_bytes = b64encode(public_key_bytes).decode('utf-8')
print('public_key_bytes')
print(public_key_bytes)

public_key_new = load_pem_public_key(b64decode(public_key_bytes))
print('public_key_new')
print(public_key_new)

try:
    print(public_key)
    public_key_new.verify(signature, str(receta).encode(), ec.ECDSA(hashes.SHA256()))
    print('OK')
except InvalidSignature:
    print('No se ha podido validar la receta ') '''

with open("FirmaDigital/A/Akey.pem", "rb") as f:
    aux = f.read()
    Akey = load_pem_private_key(aux, b'admin')

print(Akey)

with open("FirmaDigital/A/Acert.pem", "rb") as f:
    aux = f.read()
    acert = load_pem_x509_certificate(aux)

print(acert)

with open("FirmaDigital/AC1/ac1cert.pem", "rb") as f:
    aux = f.read()
    ac1cert = load_pem_x509_certificate(aux)

print(acert)

issuer_public_key = ac1cert.public_key()
cert_to_check = ac1cert
aux = issuer_public_key.verify(
    cert_to_check.signature,
    cert_to_check.tbs_certificate_bytes,
    PKCS1v15(),
    cert_to_check.signature_hash_algorithm
)
print(aux)
cert_to_check = acert
aux = issuer_public_key.verify(
    cert_to_check.signature,
    cert_to_check.tbs_certificate_bytes,
    PKCS1v15(),
    cert_to_check.signature_hash_algorithm
)
print(aux)


ruta = 'BBDD/usuarios.json'  # Ruta al archivo json que almacena los usuarios
ruta2 = 'FirmaDigital/pki.txt'

    # Abrimos el json y guardamos el contenido en data
json_file = open(ruta)
data = json.load(json_file)
super_info = data[0]
print(super_info)


print(type(Akey))
inf_bytes = str(super_info).encode()
signature = Akey.sign(
    inf_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
'''public_key = Akey.public_key()
public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
public_key_bytes = b64encode(public_key_bytes).decode('utf-8')'''

signature_json = b64encode(signature).decode('utf-8')
f = open(ruta2, 'wb')
f.write(signature)

with open(ruta2, "rb") as f:
    signature = f.read()


signature = b64decode(signature_json)
public_key = Akey.public_key()
public_key.verify(
    signature,
    inf_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)