from loginlib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            username = askValue("username")
            password = askValue("password")
            if login(username, password):
                print("Login successful!\n")
                userMenu(username)
            else:
                print("Login failed.\n")

        elif choice == 2:
            username = askValue("username")
            password = askValue("password")
            register(username, password)
            print("User registration completed!\n")

        elif choice == 0:
            print("Exiting program.")
            break

        else:
            print("Invalid choice.\n")

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()
        if choice == 1:
             viewProfile(PUsername)
        elif choice == 2:
             new_pass = askValue("new password")
             change_password(PUsername, new_pass)
             print("Password changed.\n")
        elif choice == 0:
             print("Logged out.\n")
             break
        else:
             print("Invalid choice.\n")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()