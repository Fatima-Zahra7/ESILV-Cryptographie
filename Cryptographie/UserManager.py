from Cryptographie.PasswordHash import PasswordHasher
from Cryptographie.SaltGenerator import SaltGenerator
from Cryptographie.user import User


class UserManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager


    def register_user(self, username, password, filename):

        self.db_manager.last_id += 1    # new ID
        user_id = self.db_manager.last_id

        if username in self.db_manager.users:
            print("This username is taken.")
            return

        # Vérifier si le mot de passe fourni par l'utilisateur est sécurisé
        while not self.is_password_strong(password):
            password = input("Enter a more secure password: ")

        # Hash password
        salt = SaltGenerator().generate_salt()
        hashed_password = PasswordHasher().hash_password(password, salt)

        # Create new User
        new_user = User(user_id, username, hashed_password, salt)
        self.db_manager.users[user_id] = new_user

        self.db_manager.save_user_to_file(new_user, filename)


    def is_password_strong(self, password):
        if len(password) < 14:
            return False

        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password)

        return has_digit and has_upper and has_lower and has_special


    def login_user(self, username, password):
        password_hasher = PasswordHasher()
        # Connecte un utilisateur
        salt = self.get_user_salt(username)
        if salt:
            hashed_password = password_hasher.hash_password(password, salt)

            if password_hasher.verify_password(hashed_password, salt, password):

                print("Connexion réussie!")
                return True
            else:
                print("Password incorrect!")
                return False
        else:
            print("User not found.")
            return False

    def get_user_salt(self, username):
        for user_id, user in self.db_manager.items():
            if user.username == username:
                return user.salt
        print("Utilisateur non trouvé.")
        return None


    def logout_user(self):
        self.current_user = None  # Réinitialiser l'utilisateur actuellement connecté