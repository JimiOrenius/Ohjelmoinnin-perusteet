########################################################
# Task A9_T1
# Developer Jimi Orenius
# Date 2025-11-26
########################################################


def main() -> None:
    print("Program starting.\n")
    total = 0.0

    while True:
        value = input("Insert a floating-point value (0 to stop): ")
        try:
            f_value = float(value)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(value))
            continue

        if f_value == 0:
            break

        total += f_value

    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")

if __name__ == "__main__":
    main()
