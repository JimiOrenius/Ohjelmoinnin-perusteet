########################################################
# Task A10_T7
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0])
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows-1)
        c = random.randint(0, cols-1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0])
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for i in range(max(0, r-1), min(rows, r+2)):
                for j in range(max(0, c-1), min(cols, c+2)):
                    if PMineField[i][j] == 9:
                        count += 1
            PMineField[r][c] = count

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0]*PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def main() -> None:
    PMineField: list[list[int]] = []
    print("Program starting.\n")
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(PMineField, rows, cols, mines)
        elif choice == "2":
            for row in PMineField:
                print(row)
        elif choice == "3":
            filename = input("Insert filename: ")
            with open(filename, "w", encoding="utf-8") as f:
                for row in PMineField:
                    f.write(",".join(map(str, row)) + "\n")
            print(f"Board saved in {filename}")
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
