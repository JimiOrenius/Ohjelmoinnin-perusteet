print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = input("Your choice: ")

if choice == "1":
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F\n")
elif choice == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C\n")
elif choice == "0":
    print("Exiting...")
else:
    print("Invalid choice, please select 0, 1 or 2.\n")

print("\nProgram ending.")