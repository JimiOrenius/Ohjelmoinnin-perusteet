########################################################
# Task A9_T5
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try:
        val_float = float(Feed)
        if not val_float.is_integer():
            raise ValueError("Not an integer")
        val_int = int(val_float)
        if not (0 <= val_int <= 255):
            raise ValueError("Out of range")
        return val_int
    except:
        raise ValueError("Invalid input value")
def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)
def main():
    print("Program starting.")
    try:
        R = askIntByte("Insert red: ")
        G = askIntByte("Insert green: ")
        B = askIntByte("Insert blue: ")

        hex_color = createHex(R, G, B)

        print("RGB Details:")
        print(f"- Red {R}")
        print(f"- Green {G}")
        print(f"- Blue {B}")
        print(f"- Hex {hex_color}")
        print(f"- R-byte {R:08b}")
        print(f"- G-byte {G:08b}")
        print(f"- B-byte {B:08b}")

    except Exception as e:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()