########################################################
# Task A9_T4
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    value = input("Insert Celsius: ")
    try:
        celsius = float(value)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{value}'")
    if not (TEMP_MIN <= celsius <= TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")
    return celsius

def main() -> None:
    print("Program starting.\n")
    try:
        c = collectCelsius()
        print(f"You inserted {c} °C")
    except Exception as e:
        print("Error:", e)
    print("Program ending.")

if __name__ == "__main__":
    main()
