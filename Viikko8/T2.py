from arithmetic_lib import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    while True:
        choice = input("Your choice: ")
        if choice in ["0", "1", "2", "3", "4"]:
            return int(choice)
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")

def askValue(PPrompt: str) -> float:
    while True:
        try:
            value = float(input(PPrompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main() -> None:
    print("Program starting.")
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
 
        val1 = askValue("Insert first value: ")
        val2 = askValue("Insert second value: ")
        
        if choice == 1:
            result = add(val1, val2)
            print(f"{val1} + {val2} = {result}\n")
        elif choice == 2:
            result = subtract(val1, val2)
            print(f"{val1} - {val2} = {result}\n")
        elif choice == 3:
            result = multiply(val1, val2)
            print(f"{val1} * {val2} = {result}\n")
        elif choice == 4:
            try:
                result = divide(val1, val2)
                print(f"{val1} / {val2} = {result}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
