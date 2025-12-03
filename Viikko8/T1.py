import time

print("Program starting.")

# Initialize default pause duration
pause_duration = 1.0  # default 1 second

while True:
    # Display menu
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        try:
            pause_duration = float(input("Insert pause duration (s): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "2":
        print(f"Pausing for {pause_duration} seconds.")
        time.sleep(pause_duration)
        print("Unpaused.\n")
    elif choice == "0":
        print("Exiting program.\n")
        break
    else:
        print("Invalid choice. Please select 0, 1, or 2.\n")

print("Program ending.")