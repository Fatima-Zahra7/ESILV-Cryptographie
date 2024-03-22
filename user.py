import random
import string

class PasswordGenerator:
    @staticmethod
    def generate_password():
        # Génère un mot de passe sécurisé
        length = 14  # Longueur du mot de passe
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

#****************************************

import csv

class UserManager:
    def __init__(self):
        self.users = {}

    def load_users(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.users[row[0]] = User(row[0], row[1])

    def register_user(self, username, password, filename):
        # Enregistre un nouvel utilisateur
        if username in self.users:
            print("Ce nom d'utilisateur est déjà utilisé.")
            return False
        else:
            # Vérifier si le mot de passe fourni par l'utilisateur est sécurisé
            if not self.is_password_strong(password):
                # Générer un mot de passe sécurisé
                password = PasswordGenerator.generate_password()
                print("Mot de passe généré : " + password)

            # Création de l'instance User
            self.users[username] = User(username, password)

            # Write to file
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if csvfile.tell() == 0:
                    writer.writerow(['Username', 'Password'])
                writer.writerow([username, password])
            print("User " + username + " was successfully registered.")

            return True


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
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return False

#****************************************
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

#****************************************

def main():
    filename = "users.csv"
    user_manager = UserManager()
    user_manager.load_users(filename)

    # Demande à l'utilisateur s'il souhaite s'inscrire ou se connecter
    choice = input("Do you want to register (r) or login (l)?")

    if choice.lower() == 'r':  # Inscription
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if not password:
            password = PasswordGenerator.generate_password()
        user_manager.register_user(username, password,filename)

    elif choice.lower() == 'l':  # Connexion
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_manager.login_user(username, password)

    else:
        print("Invalid choice.")

#****************************************

if __name__ == "__main__":
    main()