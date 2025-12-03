from dataclasses import dataclass

DELIMITER = ";"

@dataclass       
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

@dataclass
class DayUsage:
    weekday: str
    total_consumption: float = 0.0
    total_cost: float = 0.0

def readFile(filename: str):
    timestamps = []

    try: 
        with open(filename, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("Weekday"):
                    continue

                weekday, hour, consumption, price = line.split(DELIMITER)

                timestamps.append(
                    TIMESTAMP(
                        weekday = weekday,
                        hour = hour, 
                        consumption = float(consumption),
                        price = float(price)
                    )
                )

        return timestamps
    
    except FileNotFoundError:
        print(f'File "{filename}" not found.')
        return []
    
def analyse(timestamps: list[TIMESTAMP]):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]
    results = {day: DayUsage(weekday = day) for day in weekdays}

    for ts in timestamps: 
        weekday = ts.weekday
        
        if weekday not in results:
            print(f'Warning: Unknown weekday "{ts.weekday}" in data. Skipping this row.')
            continue

        day_usage = results[weekday]
        day_usage.total_consumption += ts.consumption
        day_usage.total_cost += ts.consumption * ts.price

    return list(results.values())

def display(results: list[DayUsage]):
    print("### Electricity consumption summary ###")

    for day in results: 
        print(f" - {day.weekday} usage {day.total_consumption:.2f} kWh, cost {day.total_cost:.2f} €")

    print("### Electricity consumption summary ###")

def main():
    print("Program starting.")

    while True:
        filename = input("Insert filename: ").strip()
        print(f'Reading file "{filename}".')

        timestamps = readFile(filename)

        if timestamps:
            break

        print("Please try again.")

    print("Analysing timestamps.")

    results = analyse(timestamps)

    print("Displaying results.")

    display(results)

    print("Program ending.")

if __name__ == "__main__":
    main()