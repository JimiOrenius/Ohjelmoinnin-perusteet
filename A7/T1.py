def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")
    
    numbers = []  

    while True:  
        user_input = input("Insert positive integer (negative stops): ")

        try:
            number = int(user_input)  
        except ValueError:
            print("Please enter a valid integer.")
            continue 

        if number < 0:  
            break 
        else:
            numbers.append(number)  

    print("Stopped collecting positive integers.")  

    if len(numbers) == 0:  
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers): 
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

    print("Program ending.")  


if __name__ == "__main__":
    main()