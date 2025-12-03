from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    PDwg.add(Rect(
        insert=(float(left), float(top)),      
        size=(float(sideLength), float(sideLength)),
        fill=color,
        stroke=strokeColor,
        stroke_width=2
    ))

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    PDwg.add(Circle(
        center=(float(centerX), float(centerY)),
        r=float(radius),
        fill=color,
        stroke=stroke,
        stroke_width=2
    ))

def saveSvg(PDwg: Drawing, filename) -> None:
    confirm = input(f'Proceed to save "{filename}"? (y/n): ').strip().lower()
    if confirm == 'y':
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")