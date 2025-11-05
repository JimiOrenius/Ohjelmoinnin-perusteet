LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char: str, shift) -> str:
    if isinstance(shift, str):
        shift = 13

    if char in LOWER_ALPHABETS:
        index = (LOWER_ALPHABETS.index(char) + shift) % 26
        return LOWER_ALPHABETS[index]
    
    elif char in UPPER_ALPHABETS:
        index = (UPPER_ALPHABETS.index(char) + shift) % 26
        return UPPER_ALPHABETS[index]
    
    else: 
        return char
    
def rot13(text: str) -> str:
    result = ""
    for char in text:
        result += shiftCharacter(char, 13)
    return result

def writeFile(filename: str, content) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        if isinstance(content, list):
            for line in content:
                f.write(str(line) + "\n")

        else:
            f.write(str(content))

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")

    rows = []

    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break

        rows.append(row)

    ciphered_rows = [rot13(r) for r in rows]

    print("\n#### Ciphered text ####")
    for r in ciphered_rows:
        print(r)

    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    writeFile(filename, ciphered_rows)
    print("Ciphered text saved!")

    print("Program ending.")

if __name__ == "__main__":
    main()