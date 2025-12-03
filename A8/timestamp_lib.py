
from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    """
    Reads timestamps from a file and appends datetime objects into PTimestamps list.
    Skips empty lines.
    """
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        ts = datetime.strptime(line, "%Y-%m-%d %H:%M")
                        PTimestamps.append(ts)
                    except ValueError:
                        print(f"Warning: Could not parse '{line}', skipping.")
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    return sum(1 for ts in PTimestamps if ts.year == PYear)

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    if PMonth not in MONTHS:
        return 0
    month_index = MONTHS.index(PMonth) + 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    if PWeekday not in WEEKDAYS:
        return 0
    weekday_index = WEEKDAYS.index(PWeekday)
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
