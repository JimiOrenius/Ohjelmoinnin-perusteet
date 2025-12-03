
from timestamp_lib import readTimestamps, calculateYears, calculateMonths, calculateWeekdays

def main() -> None:
    print("Program starting.")
    
    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)
    
    while True:
        print("Options:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            try:
                year = int(input("Insert year: "))
                count = calculateYears(year, timestamps)
                print(f"Amount of timestamps during year '{year}' is {count}\n")
            except ValueError:
                print("Invalid year input.\n")
        elif choice == "2":
            month = input("Insert month: ").strip()
            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}\n")
        elif choice == "3":
            weekday = input("Insert weekday: ").strip()
            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.\n")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
