import argon2

class PasswordHasher:

    def hash_password(self, password, salt):
        # Hacher le mot de passe avec Argon2
        hasher = argon2.PasswordHasher()

        # Salt le mot de passe
        hashed_password = hasher.hash(password + salt)
        return hashed_password

def main():
    # Créer une instance de PasswordHasher
    password_hasher = PasswordHasher()

    # Définir un mot de passe et un sel
    password = input("Enter your password: ")
    salt = "randomsalage@09/"

    # Hacher le mot de passe
    hashed_password = password_hasher.hash_password(password, salt)

    # Afficher le mot de passe haché
    print("Mot de passe haché:", hashed_password)

if __name__ == "__main__":
    main()