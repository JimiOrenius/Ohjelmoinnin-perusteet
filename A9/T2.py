########################################################
# Task A9_T2
# Developer JImi Orenius
# Date 2025-11-26
########################################################


import sys

def main() -> None:
    print("Program starting.\n")
    try:
        code = int(input("Insert exit code(0-255): "))
        if 0 <= code <= 255:
            print("Clean exit")
            sys.exit(code)
        else:
            print("Error! Exit code must be between 0-255.")
            sys.exit(1)
    except ValueError:
        print("Error! Inserted value is not an integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
