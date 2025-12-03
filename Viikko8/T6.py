from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    Dwg = Drawing()
    print("Program starting.\n")
    
    while True:
        showOptions()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue

        match choice:
            case 1:
                print("Insert square")
                left = askValue1("Left edge position")
                top = askValue1("Top edge position")
                sideLength = askValue1("Side length")
                fillColor = askValue1("Fill color")
                strokeColor = askValue1("Stroke color")
                drawSquare(Dwg, left, top, sideLength, fillColor, strokeColor)
                print("Square added.\n")
            
            case 2:
                print("Insert circle")
                centerX = askValue1("Center X position")
                centerY = askValue1("Center Y position")
                radius = askValue1("Radius")
                fillColor = askValue1("Fill color")
                strokeColor = askValue1("Stroke color")
                drawCircle(Dwg, centerX, centerY, radius, fillColor, strokeColor)
                print("Circle added.\n")
            
            case 3:
                filename = askValue1("Insert filename")
                saveSvg(Dwg, filename)
            
            case 0:
                print("Exiting program.\n")
                break
            
            case _:
                print("Invalid choice. Try again.\n")

    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()
