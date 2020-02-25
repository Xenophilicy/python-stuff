from pynput.keyboard import Key, Controller as KController
from pynput.mouse import Button, Controller as MController
from tkinter import Tk
import time, sys

def hit(key):
    keyboard.press(key)
    keyboard.release(key)

delay = 0

keyboard = KController()
mouse = MController()

count = int(input("How many messages would you like deleted?\n>>"))

print("Select the window now...")
for i in range(-5,0):
    sys.stdout.write(f"\rWaiting {-i} seconds...")
    time.sleep(1)
sys.stdout.write(f"\rOkay, deleting {count} messages...\n")

before = time.time()
for i in range(1,count+1):
    start = time.time()
    hit(Key.enter)
    hit(Key.backspace)
    hit(Key.up)
    time.sleep(.1)
    keyboard.press(Key.ctrl)
    hit("a")
    keyboard.release(Key.ctrl)
    hit(Key.backspace)
    hit(Key.enter)
    time.sleep(.1)
    hit(Key.enter)
    time.sleep(.2)
    delta = (time.time()-start)*1000
    delay += delta
    print(f"\rFinished pass #{i}")
after = round((time.time()-before),2)
perPass = round(delay/count,2)

print(f"Deleted {i} message(s)!")
print(f"Average pass: {perPass} ms")
print(f"Total duration: {after} seconds")