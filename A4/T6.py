print("Program starting.\n")

n = int(input("Insert a positive integer: "))

steps = 0
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(" ->", n, end="")
    steps += 1

print(f"\nSequence had {steps} total steps.\n")
print("Program ending.")