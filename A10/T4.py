########################################################
# Task A10_T4
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import sys
from A10_TLib import readValues, displayValues, mergeSort

def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    Values = readValues(Filename)

    print(f"Raw '{Filename}' -> ", end="")
    displayValues(Values)

    mergeSort(Values, PAsc=True)
    print(f"Ascending '{Filename}' -> ", end="")
    displayValues(Values)

    mergeSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -> ", end="")
    displayValues(Values)

    Values.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()