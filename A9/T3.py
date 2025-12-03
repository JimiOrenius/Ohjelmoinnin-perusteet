########################################################
# Task A9_T3
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import os
import sys

def main() -> None:
    print("Program starting.\n")
    filename = input("Insert filename: ")

    if not os.path.exists(filename):
        print(f'Error! File "{filename}" does not exist.')
        sys.exit(1)

    print(f"## {filename} ##")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
    print(f"## {filename} ##")
    print("Program ending.")

if __name__ == "__main__":
    main()
