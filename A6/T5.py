SEPARATOR = ";"

def readValues(filename: str) -> str:
    values = ""
    with open(filename, "r") as f:
        for line in f:
            number = line.strip()
            if number:
                values += number + SEPARATOR
    if values.endswith(SEPARATOR):
        values = values[:-1]
    
    return values

def analyseValues(values: str) -> str:
    numbers = [int(v) for v in values.split(SEPARATOR)]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0
    result = f"Count{SEPARATOR}Sum{SEPARATOR}Greatest{SEPARATOR}Average\n"
    result += f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}\n"
    return result

def displayResults(filename: str, analysis: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(analysis)
    print("#### Number analysis - END ####")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    analysis = analyseValues(values)
    displayResults(filename, analysis)
    print("Program ending.")

if __name__ == "__main__":
    main()