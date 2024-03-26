import string
import random
class SaltGenerator :
    @staticmethod
    def generate_salt():
        # Génère un sel aléatoire
        length = 16  # Longueur du sel
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))