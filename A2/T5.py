print("Program starting.\n")
word = input("Insert a closed compound word: ")

reversed_word = word[::-1]
length = len(word)
first_char = word[0]
last_char = word[-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
print(f"The inserted word length is {length}")
print(f"Last character is '{last_char}'\n")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = word[start:end:step]

print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")

print("Program ending. ")