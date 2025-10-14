print("Program starting.\n")

print("Check multiplicative persistence.")
n = input("Insert an integer: ")

steps = 0

while len(n) > 1:
    digits = [int(d) for d in n]
    result = 1
    print(" * ".join(n), end=" = ")
    for d in digits:
        result *= d
    print(result)
    steps += 1
    n = str(result)

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")