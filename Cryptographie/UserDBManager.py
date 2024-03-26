import csv
import os
import csv
import os
from Cryptographie.user import User


class UserDBManager:
    def __init__(self):
        self.users = {}
        self.last_id = 0

    def load_users(self, filename):
        loaded_users = {}  # Initialiser un dictionnaire pour stocker les utilisateurs chargés
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # En-tête
                if header == ['ID', 'Username', 'Password', 'Salt']:
                    for row in reader:
                        if row:  # Vérifier si la ligne est valide
                            user_id = int(row[0])
                            loaded_users[user_id] = User(user_id, row[1], row[2], row[3])
                            self.last_id = max(self.last_id, user_id)
        self.users = loaded_users  # Mettre à jour self.users avec les utilisateurs chargés
        return loaded_users  # Retourner le dictionnaire contenant les utilisateurs chargés


    def save_user_to_file(self, user, filename):
        if not user:
            return
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                writer.writerow(['ID', 'Username', 'Password', 'Salt'])
            writer.writerow([user.id, user.username, user.password, user.salt])
        print("User " + user.username + " was successfully registered.")