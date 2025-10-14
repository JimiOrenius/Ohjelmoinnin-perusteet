print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
if start <= stop:
    step = 1
else: 
    step = -1

for i in range(start, stop + step, step):
    print(i)

print("\nProgram ending.")