from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import json

class Pki:

    @staticmethod
    def check_certificados():
        with open("FirmaDigital/AC1/ac1cert.pem", "rb") as f:
            aux = f.read()
            ac1cert = load_pem_x509_certificate(aux)
        issuer_public_key = ac1cert.public_key()
        cert_to_check = ac1cert
        try:
            issuer_public_key.verify(
            cert_to_check.signature,
            cert_to_check.tbs_certificate_bytes,
            PKCS1v15(),
            cert_to_check.signature_hash_algorithm)

        except InvalidSignature:
            print('No se han podido verfificar los certificados')
            return -1

        with open("FirmaDigital/A/Acert.pem", "rb") as f:
            aux = f.read()
            acert = load_pem_x509_certificate(aux)

        cert_to_check = acert
        try:
            issuer_public_key.verify(
                cert_to_check.signature,
                cert_to_check.tbs_certificate_bytes,
                PKCS1v15(),
                cert_to_check.signature_hash_algorithm)
            print('\nLos certificados se han verificado correctamente')

        except InvalidSignature:
            print('No se han podido verfificar los certificados')
            return -1

        return 0

    @staticmethod
    def verificar_super():
        with open("FirmaDigital/A/Akey.pem", "rb") as f:
            aux = f.read()
            Akey = load_pem_private_key(aux, b'admin')
        ruta = 'BBDD/usuarios.json'  # Ruta al archivo json que almacena los usuarios

        # Abrimos el json y guardamos el contenido en data
        json_file = open(ruta)
        data = json.load(json_file)
        super_info = data[0]
        inf_bytes = str(super_info).encode()
        with open('FirmaDigital/pki.txt', "rb") as f:
            signature = f.read()
        public_key = Akey.public_key()
        try:
            public_key.verify(
                signature,
                inf_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print('\nLos datos del super son validos')
        except InvalidSignature:
            print('\nLos datos del super NO son validos')
            return -1
        return 0



