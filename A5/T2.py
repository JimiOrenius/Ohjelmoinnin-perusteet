def frameWord(Pword):
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print()
    print("Program ending.")
    return None

main()