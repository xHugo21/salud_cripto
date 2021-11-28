from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat,\
    NoEncryption
from checks import Checks
from cryptography.hazmat.primitives import hashes
from jsonmethods import JsonMethods
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.exceptions import InvalidSignature
from base64 import b64decode,b64encode

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
    print('No se ha podido validar la receta ')