def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth, PHeight) -> float:
   Area = PWidth * PHeight
   return float(Area)

def main():
   print("Program starting.")
   Width = askDimension("width")
   Height = askDimension("height")
   Area = calcRectangleArea(Width, Height)
   print()
   print(f"Area is {Area}²")
   print("Program ending.")

main()