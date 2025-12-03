from dataclasses import dataclass

DELIMITER = ";"

@dataclass       
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

    def total(self):
        return self.consumption * self.price
    
def readTimestamps(filename: str, timestamps: list[TIMESTAMP]):

    with open(filename, "r", encoding="UTF-8") as f:
        header = f.readline()   

        for line in f: 
            row = line.strip() 

            if not row:
                continue

            cols = row.split(DELIMITER)
            ts = TIMESTAMP(
                weekday = cols[0],
                hour = cols[1], 
                consumption = float(cols[2]), 
                price = float(cols[3])
            )

            timestamps.append(ts)

def displayTimestamps(timestamps: list[TIMESTAMP]):
    print("Electricity usage:")

    for ts in timestamps:
        print(
            f" - {ts.weekday} {ts.hour}:00, price {ts.price:.2f} €"
            f"consumption {ts.consumption:.2f} kwh, total {ts.total():.2f} €"
        )

def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    print(f'Reading file "{filename}".')

    timestamps: list[TIMESTAMP] = []
    readTimestamps(filename, timestamps)

    displayTimestamps(timestamps)

    print("Program ending.")

if __name__ == "__main__":
    main()