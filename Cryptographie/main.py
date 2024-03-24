from Cryptographie.PasswordHash import PasswordHasher
from Cryptographie.user import UserManager, SaltGenerator

def main():
    filename = "../DB/users.csv"
    user_manager = UserManager()
    password_hasher = PasswordHasher()

    user_manager.load_users(filename)

    # Demande à l'utilisateur s'il souhaite s'inscrire ou se connecter
    choice = input("Do you want to register (r) or login (l)?")

    if choice.lower() == 'r':  # Inscription

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in user_manager.users:
            print("This username is taken.")

        # Vérifier si le mot de passe fourni par l'utilisateur est sécurisé
        while not user_manager.is_password_strong(password):
            # Redemander un mot de passe sécurisé
            password = input("Enter a more secure password: ")

        # Hacher le mot de passe
        salt = SaltGenerator().generate_salt()
        hashed_password = password_hasher.hash_password(password, salt)

        user_manager.register_user(username, hashed_password, salt, filename)

    elif choice.lower() == 'l':  # Connexion
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        salt = user_manager.get_user_salt(username)

        if salt:
            hashed_password = password_hasher.hash_password(password,salt)

            if password_hasher.verify_password(hashed_password, salt, password):
                print("Connexion réussie!")
            else:
                print("Password incorrect!")
        else:
            print("Username not found!")

    else:
        print("Invalid choice.")

#****************************************

if __name__ == "__main__":
    main()