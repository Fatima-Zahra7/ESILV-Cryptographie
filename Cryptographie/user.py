import random
import string
import csv

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
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                user_id = int(row[0])
                self.users[user_id] = User(user_id, row[1], row[2], row[3])
                self.last_id = max(self.last_id, user_id)

    def register_user(self, username, password, salt, filename):
        # Générer un nouvel ID
        self.last_id += 1
        user_id = self.last_id

        # Création de l'instance User
        new_user = User(user_id, username, password, salt)
        self.users[user_id] = new_user

        # Write to file
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
               writer.writerow(['ID','Username', 'Password', 'Salt'])
            writer.writerow([user_id,username, password,salt])
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
        # Connecte un utilisateur
        if username in self.users and self.users[username].password == password:
            print("Connexion réussie.")
            return True
        else:
            print("username or password incorrect.")
            return False

    def get_user_salt(self, username):
        if username in self.users:
            return self.users[username].salt
        else :
            print("user doesn't exist")
            return None
