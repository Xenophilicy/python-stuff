import matplotlib.pyplot as plt
from PIL import ImageDraw
from PIL import Image
import math
import time
import sys

scale = 10

def sc(size):
    return scale*size

def unsc(size):
    return size/scale

valid = False
while valid == False:
    radius = input("What would you like the radius of the circle to be?\n>>")
    try:
        radius = int(radius)
    except ValueError:
        print("Invalid midpoint entered, make sure the radius entered is numeric!")
        continue
    if radius >= 50:
        print(f"{radius} is too large of a radius, please choose a number less than 50.")
    else:
        print(f"Okay, your circle will have a desired radius of {radius}!")
        valid = True
valid = False
while valid == False:
    midpoint = input("What would you like your midpoint of the circle to be?\nMake sure to enter it without parenthesis and X & Y values separated by a space.\n>>")
    try:
        mpX = sc(int(midpoint.split()[0]))
        mpY = sc(int(midpoint.split()[1]))
        print(f"Okay, your scaled midpoint will be at ({mpX},{mpY}) on the grid!")
        valid = True
    except Exception:
        midpoint = print("Invalid midpoint entered, make sure the midpoint entered follows criteria!")

processStart = time.monotonic()

sRadius = sc(radius)
width = int((sRadius*3)+((abs(mpX) if abs(mpX) > abs(mpY) else abs(mpY))*2))

image = Image.new("RGB", (width, width),color="white")
draw = ImageDraw.Draw(image)
draw.line([(0,width/2),(width,width/2)],fill="black")
draw.line([(width/2,width),(width/2,0)],fill="black")

points = []
totalPixels = width**2
passList = []
delayList = []

print(f"\nImage scale: {sc(1)} pixels")
print(f"Image resolution: {width}x{width} pixels")
print(f"Total pixels: {totalPixels:,}")
print(f"Desired radius: {radius}")
print(f"Scaled radius: {sRadius}\n")

print("Generating points...")
bar = "-------------------"
sys.stdout.write(f"\r[{bar}] 0.0%")

widthRange = range(-width,width)
last = 0
currPass = 0

def updateLoadingBar():
    pass

def isAloneInString(string):
    units = ["day","hr","min","sec"]
    for unit in units:
        if unit in string:
            return string+", "
    return string

def formatTime(days, hours, minutes, seconds):
    fU = []
    timeFormat = ""
    if days > 1 or days == 0:
        fU.append("days")
    else:
        fU.append("day")
    if hours > 1 or hours == 0:
        fU.append("hrs")
    else:
        fU.append("hr")
    if minutes > 1 or minutes == 0:
        fU.append("mins")
    else:
        fU.append("min")
    if seconds > 1 or seconds == 0:
        fU.append("secs")
    else:
        fU.append("sec")
    if not days == 0:
        timeFormat += (f"{days} {fU[0]}")
    if not hours == 0:
        timeFormat = isAloneInString(timeFormat)
        timeFormat += (f"{hours} {fU[1]}")
    if not minutes == 0:
        timeFormat = isAloneInString(timeFormat)
        timeFormat += (f"{minutes} {fU[2]}")
    if not seconds == 0:
        timeFormat = isAloneInString(timeFormat)
        timeFormat += (f"{seconds} {fU[3]}")
    if timeFormat == "":
        return "0 secs"
    return timeFormat

def formatMilliseconds(total):
    secs =(total/1000)%60
    secs = round(secs,2)
    mins = (total/(1000*60))%60
    mins = int(mins)
    hrs = int(((total/(1000*60*60))%24))
    days = int(total/(1000*60*60*24))
    return days,hrs,mins,secs

genStart = time.monotonic()
delays = []
for x in widthRange:
    for y in widthRange:
        pointStart = time.monotonic()
        currPass += 1
        current = widthRange.index(x)
        percent = round((current/len(widthRange))*100,1)
        elapsed = time.monotonic() - genStart
        fm = formatMilliseconds(((width*2)**2*elapsed/currPass-elapsed)*1000)
        timeLeft = formatTime(fm[0],fm[1],fm[2],fm[3])
        if percent%.5 == 0.0 or percent%5 == 0.0:
            if not percent == last:
                bar = ""
                count = 0
                tenDiv = int(percent/5)
                for i in range(0,tenDiv):
                    count += 1
                    bar += '█'
                for i in range(tenDiv,20):
                    bar += '-'
                last = percent
                barString = f"\r[{bar}] {percent}% (about {timeLeft} remaining)"
                sys.stdout.write(barString)
        leftParen = (x-mpX)**2
        rightParen = (y-mpY)**2
        distSqrt = int(math.sqrt(leftParen+rightParen))
        if distSqrt == sRadius:
            points.append((x+(width/2),-y+(width/2)))
        if currPass%10 == 0:
            passList.append(currPass)
            delayList.append((time.monotonic()-pointStart))

pointDelta = round((time.monotonic()-genStart)*1000,2)

sys.stdout.write("\033[K")
print("\r[███████████████████] 100.0%", end="")
print("\nDone.")
print("Generating tweens...")

polyPoints = []
drawPoints = []

for point in points:
    polyPoints.append(point)
    for x in range(-1,1):
        for y in range(-1,1):
            drawPoints.append((point[0]+x,point[1]+y))

print("Done.")
print("Drawing points")

for point in drawPoints:
    draw.point([(point[0],point[1])],fill="black")

print("Done.")
print("Drawing polygon...")

draw.polygon(polyPoints,fill="red")

image.save("graph.png")
print("Done.")
length = len(points)

print("Drawing time graph...")

plt.scatter(passList,delayList)
plt.savefig("timeGraph.png")

print("Done.")

processDelta = round((time.monotonic()-processStart)*1000,2)

print(f"Circle drawn with {length} points")
fm = formatMilliseconds(pointDelta)
delta = formatTime(fm[0],fm[1],fm[2],fm[3])
print(f"Point search took {pointDelta} ms ({delta})")
fm = formatMilliseconds(processDelta)
delta = formatTime(fm[0],fm[1],fm[2],fm[3])
print(f"Entire process took {processDelta} ms ({delta})")

#image.show()