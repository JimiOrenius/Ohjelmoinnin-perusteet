def readValues(filename: str) -> list[float]:
    values = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    try:
                        values.append(float(line))
                    except ValueError:
                        print(f"Warning: Could not convert '{line}' to float, skipping.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return values

def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)

def calculateAverage(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 1)

def main() -> None:
    print("Program starting.")
    
    values: list[float] = []
    
    while True:
        print("Options:")
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            filename = input("Insert filename: ")
            values = readValues(filename)
        elif choice == "2":
            print(f"Amount of values {len(values)}\n")
        elif choice == "3":
            total = calculateSum(values)
            print(f"Sum of values {total}\n")
        elif choice == "4":
            avg = calculateAverage(values)
            print(f"Average of values {avg}\n")
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.\n")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
