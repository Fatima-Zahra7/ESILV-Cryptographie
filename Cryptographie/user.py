import random
import string
import csv
import os
from Cryptographie.PasswordHash import PasswordHasher

class SaltGenerator :
    @staticmethod
    def generate_salt():
        # Génère un sel aléatoire
        length = 16  # Longueur du sel
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

#****************************************
class User:
    def __init__(self, id, username, password, salt):
        self.id = id
        self.username = username
        self.password = password
        self.salt = salt


#****************************************

class UserManager:
    def __init__(self):
        self.users = {}
        self.last_id = 0

    def load_users(self, filename):
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                # header
                header = next(reader)
                # Vérifier si l'en-tête est valide
                if header == ['ID', 'Username', 'Password', 'Salt']:
                    for row in reader:
                        if row:  # check if valide row
                            user_id = int(row[0])
                            self.users[user_id] = User(user_id, row[1], row[2], row[3])
                            self.last_id = max(self.last_id, user_id)
                        else:
                            print("Ligne vide dans le fichier CSV.")
                else:
                    print("L'en-tête du fichier CSV n'est pas valide.")
        else:
            print("Le fichier CSV est vide ou n'existe pas.")

    def register_user(self, username, password, filename):

        # Générer un nouvel ID
        self.last_id += 1
        user_id = self.last_id

        if username in self.users:
            print("This username is taken.")

        # Vérifier si le mot de passe fourni par l'utilisateur est sécurisé
        while not self.is_password_strong(password):
            # Redemander un mot de passe sécurisé
            password = input("Enter a more secure password: ")

        # Hacher le mot de passe
        salt = SaltGenerator().generate_salt()
        hashed_password = PasswordHasher().hash_password(password, salt)

        # Création de l'instance User
        new_user = User(user_id, username, hashed_password, salt)
        self.users[user_id] = new_user

        # Write to file
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
               writer.writerow(['ID','Username', 'Password', 'Salt'])
            writer.writerow([user_id,username, hashed_password,salt])
        print("User " + username + " was successfully registered.")

    def is_password_strong(self, password):
        # Vérifier si le mot de passe respecte les critères de sécurité
        # Vous pouvez implémenter vos propres critères de force de mot de passe ici
        # Par exemple, longueur minimale, utilisation de caractères spéciaux, de chiffres et de lettres majuscules et minuscules
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
        for user_id, user in self.users.items():
            if user.username == username:
                return user.salt
        print("User doesn't exist")
        return None