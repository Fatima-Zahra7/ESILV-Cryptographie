import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

class AsymmetricEncryptor:
    @staticmethod
    def encrypt_with_public_key(public_key, data):
        encrypted_data = public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=cryptography.hazmat.primitives.hashes.SHA256()),
                algorithm=cryptography.hazmat.primitives.hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted_data)
