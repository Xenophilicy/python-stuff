import Image
from multiprocessing import Process,Manager
import ImageChops
import os
import time

start = time.monotonic()
imgs = []
iteration = 0
processes = []
total = 0

def similar(img1,img2):
    try:
        return ImageChops.difference(img1, img2).getbbox() is None
    except Exception:
        return False

for filename in os.listdir("Images"):
    preDir = "Images/"
    imgs.append(preDir+filename)

def compareImages(img,returnDict,iteration):
    before = time.monotonic()
    img1 = Image.open("Bear.jpg")
    img2 = Image.open(img)
    dec = similar(img1,img2)
    delta = round((time.monotonic() - before)*1000,2)
    if dec == True:
        returnDict[iteration] = [img,True,delta]
    else:
        returnDict[iteration] = [img,False,delta]

returnDict = Manager().dict()
for img in imgs:
    iteration +=1
    print(f"(Process {iteration}) Started comparing {img}...")
    p = Process(target=compareImages,args=(img,returnDict,iteration,))
    processes.append(p)
    p.start()
print("Finished spawning.")
print("Gathering return values...")
for process in processes:
    process.join()

print("Printing results...")

for ret in returnDict:
    ret = returnDict[ret]
    if ret[1] == True:
        ending = "similar"
    else:
        ending = "not similar"
    print(f"{ret[0]} is {ending}")
    total+=ret[2]

average = round(total/iteration,2)
ending = round(time.monotonic()-start,2)
print(f"Total iteration count was {iteration}")
print(f"Average process duration was {average} ms")
print(f"Total duration was {ending} seconds")