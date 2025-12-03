########################################################
# Task A10_T2
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import sys
from functools import reduce
from operator import mul

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error! Could not convert line to int: {e}")
        sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    return reduce(mul, PValues, 1)

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)
    print("# --- Sum of numbers --- #")
    print(sumOfValues(Values))
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(productOfValues(Values))
    print("# --- Product of numbers --- #")
    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
