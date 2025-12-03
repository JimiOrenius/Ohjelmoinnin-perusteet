def main():
    print("Program starting.")

    user_input = input("Insert comma separated integers: ")

    parts = user_input.split(',')

    valid_numbers = []  

    for part in parts:
        part = part.strip()  

        try:
            number = int(part)  
            valid_numbers.append(number)
        except ValueError:
            if part != '':
                print(f"Error: '{part}' is not a valid integer.")

    if len(valid_numbers) == 0:
        print("No valid integers to analyze.")
    else:
        total = sum(valid_numbers)
        count = len(valid_numbers)

        if total % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        print(f"There are {count} integers in the list.")
        print(f"Sum of the integers is {total} and it's {parity}")

    print("Program ending.")  

if __name__ == "__main__":
    main()
