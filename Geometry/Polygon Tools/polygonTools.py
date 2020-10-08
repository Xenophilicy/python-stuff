import math
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

prefixes = {
    3:"Triangle",
    4:"Quadrilateral",
    5:"Pentagon",
    6:"Hexagon",
    7:"Heptagon",
    8:"Octagon",
    9:"Nonagon",
    10:"Decagon",
    11:"Hendecagon",
    12:"Dodecagon"
}
sortedPairs = {}
sidePairs = []
sides = {}
perimeter = 0
apothems = []
coords = []
maxSize = 0
scale = 100

def sc(num):
    return scale*num

def PolygonArea(coords):
    n = len(coords)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    area = abs(area) / 2.0
    return area

def join(a,b):
    return f"{a}{b}"

def allEqual(lst):
   return lst[1:] == lst[:-1]

sideLetters = input("Enter side letters in clockwise order without spaces...\n>>")
sideCount = len(sideLetters)

if sideCount > 12:
    shape = f"{sideCount}-gon"
else:
    shape = prefixes[sideCount]

print("Enter ordered pairs without parenthesis and X & Y values separated by a space...")

for side in sideLetters:
    pair = input(f"{side}: ")
    x = int(pair.split()[0])
    y = int(pair.split()[1])
    if abs(x) > maxSize:
        maxSize = abs(x)
    if abs(y) > maxSize:
        maxSize = abs(y)
    sides[side] = [x,y]

gWidth = int(sc(maxSize*2.2))
gHeight = int(sc(maxSize*2.2))
sWidth = gWidth/2
sHeight = gHeight/2
image = Image.new("RGB", (gWidth, gHeight),color="white")
draw = ImageDraw.Draw(image)
draw.line([(0,gWidth/2),(gWidth,gHeight/2)],fill="black")
draw.line([(gWidth/2,gHeight),(gWidth/2,0)],fill="black")

for coord in sides.items():
    x = int(coord[1][0])
    y = int(coord[1][1])
    coords.append([x,y])

font = ImageFont.truetype('Blazed.ttf', int(sc(2)/7))
for letter in list(sideLetters):
    if letter not in sidePairs:
        indx = sideLetters.index(letter)
        try:
            nextIndx = sideLetters[indx+1]
        except IndexError:
            nextIndx = sideLetters[0]
        sidePairs.append(join(sideLetters[indx],nextIndx))
    x = sides[letter][0]
    y = sides[letter][1]

for sidePair in sidePairs:
    splitSides = list(sidePair)
    for side in splitSides:
        try:
            sortedPairs[sidePair] = [sortedPairs[sidePair],sides[side]]
        except KeyError:
            sortedPairs[sidePair] = sides[side]

print("Slopes and Distances:")
for sortedPair in sortedPairs:
    fPair = sortedPairs[sortedPair][0]
    sPair = sortedPairs[sortedPair][1]
    fx = fPair[0]
    fy = fPair[1]
    sx = sPair[0]
    sy = sPair[1]
    leftParen = (sx-fx)**2
    rightParen = (sy-fy)**2
    numer = fx-sx
    denom = fy-sy
    slope = f"{numer}/{denom}"
    if denom == 0:
        slope = "horizontal"
    elif numer == 0:
        slope = "vertical"
    distSqrt = math.sqrt(leftParen+rightParen)
    dist = leftParen+rightParen
    perimeter += distSqrt
    print(f"    {sortedPair}: m = {slope}, D = √{dist}({round(distSqrt,2)})")
    apothem = round(dist/(2*(math.tan(180/sideCount))))
    apothems.append(apothem)

if allEqual(apothems):
    area = (perimeter*apothem)/2
    print("Type: Regular")
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} units²")
    print(f"Apothem: {apothem} units")
    print(f"Shape: {shape}")
else:
    area = PolygonArea(coords)
    print("Type: Irregular")
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} units²")
    print(f"Shape: {shape} ")
print("Graph: graph.png")

cds = []
for c in coords:
    cds.append((sc(c[0])+sWidth,-sc(c[1])+sHeight))
draw.polygon(cds,fill="red")

for letter in list(sideLetters):
    x = sc(sides[letter][0])
    y = sc(sides[letter][1])
    mod = sc(1)
    draw.text((x+sWidth,-y+sHeight),letter,font=font, fill="black")
    draw.point([(x,y)],fill="black")

image.save("graph.png")
image.show()