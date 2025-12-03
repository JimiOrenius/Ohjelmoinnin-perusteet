WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")


def readFile(filename: str, rows: list[str]) -> None:
    print(f'Reading file "{filename}".')
    rows.clear()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            header = file.readline()
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                rows.append(line)
    except FileNotFoundError:
        print("Error: File not found.")
    return None


def analyseTimestamps(rows: list[str], results: list[str]) -> None:
    print("Analysing timestamps.")
    results.clear()
    WeekdayTimestampAmount = [0, 0, 0, 0, 0, 0, 0]
    for row in rows:
        for i, weekday in enumerate(WEEKDAYS):
            if row.startswith(weekday):
                WeekdayTimestampAmount[i] += 1
    results.append("### Timestamp analysis ###")
    for i, weekday in enumerate(WEEKDAYS):
        results.append(f" - {weekday} {WeekdayTimestampAmount[i]} stamps")
    results.append("### Timestamp analysis ###")
    return None


def displayResults(results: list[str]) -> None:
    print("Displaying results.")
    for row in results:
        print(row)
    return None


def main() -> None:
    print("Program starting.")
    Rows = []
    Results = []
    filename = input("Insert filename: ")
    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)
    Rows.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()