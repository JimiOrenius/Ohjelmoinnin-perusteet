def main():
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "r") as file:
            content = file.read()

        print(f'### START "{filename}" ####')
        print(content)
        print(f'#### END "{filename}" ####')

    except FileNotFoundError:
        print(f'File "{filename}" not found!')

    print("Program ending.")

if __name__ == "__main__":
    main()