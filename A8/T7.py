import svgwrite
import math

shapes = []

def draw_square():
    print("Insert square details:")
    x = int(input("Top-left X: "))
    y = int(input("Top-left Y: "))
    size = int(input("Side length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    square = svgwrite.shapes.Rect(insert=(x, y), size=(size, size), fill=fill, stroke=stroke)
    shapes.append(square)
    print("Square added.\n")

def draw_circle():
    print("Insert circle details:")
    cx = int(input("Center X: "))
    cy = int(input("Center Y: "))
    r = int(input("Radius: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    circle = svgwrite.shapes.Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke)
    shapes.append(circle)
    print("Circle added.\n")

def draw_hexagon():
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    R = apothem / math.cos(math.radians(30))
    points = []
    
    for angle_deg in [30, 90, 150, 210, 270, 330]:
        x = cx + R * math.cos(math.radians(angle_deg))
        y = cy - R * math.sin(math.radians(angle_deg))
        points.append((round(x), round(y)))

    hexagon = svgwrite.shapes.Polygon(points=points, fill=fill, stroke=stroke)
    shapes.append(hexagon)
    print("Hexagon added.\n")

def save_svg():
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == 'y':
        dwg = svgwrite.Drawing(filename)
        for shape in shapes:
            dwg.add(shape)
        dwg.save()
        print("Vector saved successfully!\n")
    else:
        print("Save canceled.\n")

def main():
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            draw_square()
        elif choice == "2":
            draw_circle()
        elif choice == "3":
            draw_hexagon()
        elif choice == "4":
            save_svg()
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
