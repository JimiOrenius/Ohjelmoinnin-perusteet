print("Program starting.\n")
Feed = input("Insert starting point: ")
pointStart = int(Feed)
Feed = input("Insert stopping point: ")
PointStop = int(Feed)
Feed = input("Insert inspection point: ")
PointInspect = int(Feed)
print("")

Run = True
#ajetaan ohjelma, oletuksena että on oikein (flagei?)
if(pointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if((pointStart > PointInspect) or (PointInspect > PointStop)):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break:\n")
    for i in range(pointStart, PointStop):
        if(i == PointInspect):
            break
        if(i == pointStart):
            print(i, end="")
        else:
            print(f" -{i}", end="")
    print("")
    print("Second loop - inspection with continue")
    for i in range(pointStart, PointStop):
        if(i == PointInspect):
            continue
        else:
            if(i == (PointStop-1)):
                print(i)
            else:
                print(i, end=" ")


print("Program ending.")