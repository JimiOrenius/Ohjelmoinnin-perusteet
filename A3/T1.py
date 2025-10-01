print("Program starting.")
print("Insert two integers.")

num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")
if num1 == num2:
    print("Integers are the same")
elif num1 > num2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

total = num1 + num2
print("\nAdding integers together")
print(f"{num1} + {num2} - {total}")

print("\nChecking the parity of the sum...")

if total % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd.")

print("Program ending.")
