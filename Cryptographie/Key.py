from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from tink import hybrid
from tink.integration import awskms

class KeyGenerator:
    @staticmethod
    def generate_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_private_key(private_key):
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    @staticmethod
    def deserialize_private_key(serialized_private_key):
        return serialization.load_pem_private_key(serialized_private_key, password=None, backend=default_backend())

    @staticmethod
    def serialize_public_key(public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @staticmethod
    def deserialize_public_key(serialized_public_key):
        return serialization.load_pem_public_key(serialized_public_key, backend=default_backend())