import argon2

class PasswordHasher:

    def hash_password(self, password, salt):
        # Hacher le mot de passe avec Argon2
        hasher = argon2.PasswordHasher()

        # Salt le mot de passe
        hashed_password = hasher.hash(password + salt)
        return hashed_password

#****************************************

    def verify_password(self, hashed_password, salt, provided_password):
        # Vérifier si le mot de passe fourni correspond au mot de passe haché
        hasher = argon2.PasswordHasher()
        try:
            # Tenter de vérifier le mot de passe
            hasher.verify(hashed_password, provided_password + salt)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False