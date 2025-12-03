from typing import List

def readValues(PFilename: str) -> List[int]:
    """
    Reads integers from a file, one per line.
    Returns a list of integers.
    """
    Values: list[int] = []
    try:
        with open(PFilename, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    Values.append(int(line))
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error reading file '{PFilename}': {e}")
    return Values


def displayValues(PValues: list[int]) -> None:
    """
    Prints the values space-separated on a single line.
    """
    print(" ".join(str(v) for v in PValues))


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """
    Merge two sorted lists into PMerge in order specified by PAsc.
    """
    PMerge.clear()
    i = j = 0
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    while i < len(PLeft):
        PMerge.append(PLeft[i])
        i += 1
    while j < len(PRight):
        PMerge.append(PRight[j])
        j += 1


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """
    In-place merge sort using merge function.
    """
    n = len(PValues)
    if n <= 1:
        return
    mid = n // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)