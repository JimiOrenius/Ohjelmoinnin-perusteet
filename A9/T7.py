########################################################
# Task A9_T7
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import sys
import os

def showHelp() -> None:
    print("Usage: python A9_T7.py <source_file> <destination_file>")

def copyFile(src: str, dst: str) -> None:
    proceed = True
    if os.path.exists(dst):
        ans = input(f'Destination file "{dst}" exists. Overwrite? (y/n): ')
        if ans.lower() != "y":
            proceed = False
            print("Copy aborted by user.")
    if proceed:
        try:
            with open(src, "r", encoding="utf-8") as f_src:
                content = f_src.read()
            with open(dst, "w", encoding="utf-8") as f_dst:
                f_dst.write(content)
            print(f'Copying file "{src}" to "{dst}".')
        except Exception as e:
            print(f"Error copying file: {e}")
            sys.exit(-1)

def main() -> None:
    print("Program starting.\n")
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        showHelp()
        sys.exit(1)

    src_file = sys.argv[1]
    dst_file = sys.argv[2]

    if not os.path.exists(src_file):
        print(f'Error! Source file "{src_file}" does not exist.')
        sys.exit(-1)

    copyFile(src_file, dst_file)
    print("Program ending.")

if __name__ == "__main__":
    main()
