########################################################
# Task A10_T5
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.\n")
    num = int(input("Insert factorial: "))
    result = recursiveFactorial(num)
    print(f"Factorial {num}!\n{num} = {result}")
    print("Program ending.")

if __name__ == "__main__":
    main()
