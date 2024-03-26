from Cryptographie.UserDBManager import UserDBManager
from Cryptographie.UserManager import UserManager



def main():
    filename = "../DB/users.csv"

    user_db_manager = UserDBManager().load_users(filename)

    user_manager = UserManager(user_db_manager)

    # Demande à l'utilisateur s'il souhaite s'inscrire ou se connecter ou se deconnecter
    choice = input("Do you want to register (r) or login (l)?")

    if choice.lower() == 'r':  # Inscription
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user_manager.register_user(username, password, filename)

    elif choice.lower() == 'l':  # Connexion
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        logged_in = user_manager.login_user(username, password)

        if logged_in:     # Si l'utilisateur est connecté, lui donner la possibilité de se déconnecter

            logout_choice = input("Do you want to logout (y/n)?")
            if logout_choice.lower() == 'y':
                user_manager.logout_user()
                print("You have been logged out.")

    else:
        print("Invalid choice.")

#****************************************

if __name__ == "__main__":
    main()