from Cryptographie.user import UserManager

def main():
    filename = "../DB/users.csv"

    user_manager = UserManager()
    user_manager.load_users(filename)

    # Demande à l'utilisateur s'il souhaite s'inscrire ou se connecter
    choice = input("Do you want to register (r) or login (l)?")

    if choice.lower() == 'r':  # Inscription
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user_manager.register_user(username, password, filename)

    elif choice.lower() == 'l':  # Connexion
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user_manager.login_user(username, password)

    else:
        print("Invalid choice.")

#****************************************

if __name__ == "__main__":
    main()