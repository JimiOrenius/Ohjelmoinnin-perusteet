########################################################
# Task A9_T6
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def askChoice() -> int:
    try:
        choice = int(input("Your choice: "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number.")
        return -1


def saveLines(PLines: list[str]) -> None:
    if not PLines:
        print("No lines to save.")
        return
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines([line.rstrip("\n") + "\n" for line in PLines])
        print(f"{len(PLines)} lines saved to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")


def insertLine(PLines: list[str]) -> None:
    try:
        line = input("Insert text: ")
        PLines.append(line)
    except Exception as e:
        print(f"Error inserting line: {e}")


def onInterrupt(PLines: list[str]) -> None:
    print("\nKeyboard interrupt and unsaved progress!")
    if PLines:
        try:
            save_choice = input("Save before quit(y/n)?: ").strip().lower()
            if save_choice == "y":
                saveLines(PLines)
        except Exception:
            print("Error during saving process.")
    print("Program ending.")
    exit(0)


def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()