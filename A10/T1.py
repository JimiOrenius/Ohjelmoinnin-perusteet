########################################################
# Task A10_T1
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

def main() -> None:
    print("Program starting.\n")

    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            values = [line.strip() for line in f if line.strip() != ""]
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        return

    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")

    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

    print("Program ending.")

if __name__ == "__main__":
    main()
