########################################################
# Task A10_T6
# Developer Jimi Orenius
# Date 2025-11-26
########################################################

import copy
import time
from typing import Callable

def readValues(PValues: list[int]) -> None:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line != "":
                PValues.append(int(line))
    return filename

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n):
        for j in range(0, n-i-1):
            if PNums[j] > PNums[j+1]:
                PNums[j], PNums[j+1] = PNums[j+1], PNums[j]
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[0]
    left = [x for x in PNums[1:] if x <= pivot]
    right = [x for x in PNums[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    start = time.perf_counter_ns()
    PSortingAlgorithm(copy.deepcopy(PArr))
    end = time.perf_counter_ns()
    return end - start

def main() -> None:
    print("Program starting.\n")
    Values: list[int] = []
    Results: list[str] = []
    filename = ""
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            filename = readValues(Values)
        elif choice == "2":
            if not Values:
                print("No dataset loaded!")
                continue
            builtin = measureSortingTime(sorted, Values)
            bubble = measureSortingTime(bubbleSort, Values)
            quick = measureSortingTime(quickSort, Values)
            print(f"Measured speeds for dataset '{filename}':")
            print(f" - Built-in sorted {builtin} ns")
            print(f" - Bubble sort {bubble} ns")
            print(f" - Quick sort {quick} ns")
            Results = [
                f"Measured speeds for dataset '{filename}':",
                f" - Built-in sorted {builtin} ns",
                f" - Bubble sort {bubble} ns",
                f" - Quick sort {quick} ns"
            ]
        elif choice == "3":
            savefile = input("Insert results filename: ")
            with open(savefile, "w", encoding="utf-8") as f:
                f.write("\n".join(Results) + "\n")
            print(f"Results saved in {savefile}")
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Invalid choice. Try again.")
    Values.clear()
    Results.clear()

if __name__ == "__main__":
    main()
