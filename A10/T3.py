########################################################
# Task A10_T3
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    # Handle CLI argument or prompt
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert dataset filename: ")

    # Read values from file
    Values = readValues(Filename)
    if not Values:
        print("No values read. Exiting.")
        return

    print("Raw values:")
    displayValues(Values)

    # Sort ascending
    bubbleSort(Values, PAsc=True)
    print("Sorted ascending:")
    displayValues(Values)

    # Sort descending
    bubbleSort(Values, PAsc=False)
    print("Sorted descending:")
    displayValues(Values)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()