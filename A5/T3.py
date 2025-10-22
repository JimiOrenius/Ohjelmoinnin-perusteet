def askName():
    name = input("Insert name: ")
    return name

def greetUser(Pname):
    print(f"Hello {Pname}")
    return None

def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()