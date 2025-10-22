# Functions example 2:
# voi käyttää "-> None"  TAI "return none".

def displayMenu() -> None: 
    print("Menu:")
    print("1 - View balance")
    print("2 - Deposit money")
    print("3 - Withdraw money")
    print("0 - Exit")
    return None

def getUserChoice() -> int:
    userInput = input("Enter your choice: ")
    return int(userInput)

def main() -> None:
    print("Welcome to the bank app...")
    choice = -1
    while choice != 0:
        displayMenu()
        choice = getUserChoice()
    return None

main()