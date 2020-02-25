from pynput.keyboard import Key
from pynput.keyboard import Controller as KController
from pynput.mouse import Button
from pynput.mouse import Controller as MController
from tkinter import Tk
import time, sys

def hit(key):
    keyboard.press(key)
    keyboard.release(key)

string = "https://accounts.google.com/signin/v2/recoveryidentifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

keyboard = KController()
mouse = MController()

username = input("What's the username of gmail account?\n>>")

print("Open a chrome window now...")
for i in range(-5,0):
    sys.stdout.write(f"\rWaiting {-i} seconds...")
    time.sleep(1)
sys.stdout.write(f"\rBegin...\n")
keyboard.press(Key.ctrl)
hit("t")
keyboard.release(Key.ctrl)

for i in range(1,999):
    if i%10 == 0:
        for i in range(0,10):
            keyboard.press(Key.ctrl)
            hit("w")
            keyboard.release(Key.ctrl)
            time.sleep(.05)
    keyboard.press(Key.ctrl)
    hit("t")
    keyboard.release(Key.ctrl)
    time.sleep(.1)
    keyboard.type("https://accounts.google.com/signin/v2/recoveryidentifier")
    hit(Key.enter)
    time.sleep(.9)
    keyboard.type(f"{username}{i}@gmail.com")
    hit(Key.enter)
    time.sleep(1)
    mouse.position = (312, 51)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    hit("c")
    keyboard.release(Key.ctrl)
    cd = Tk().clipboard_get()
    if not str(cd) == string:
        print(f"HIT → {username}{i}@gmail.com")

for i in range(1,999):
    if i%10 == 0:
        for i in range(0,10):
            keyboard.press(Key.ctrl)
            hit("w")
            keyboard.release(Key.ctrl)
            time.sleep(.05)
    keyboard.press(Key.ctrl)
    hit("t")
    keyboard.release(Key.ctrl)
    time.sleep(.1)
    keyboard.type("https://accounts.google.com/signin/v2/recoveryidentifier")
    hit(Key.enter)
    time.sleep(.9)
    keyboard.type(f"{username}{i}@gmail.com")
    hit(Key.enter)
    time.sleep(1)
    mouse.position = (312, 51)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    hit("c")
    keyboard.release(Key.ctrl)
    cd = Tk().clipboard_get()
    if not str(cd) == string:
        print(f"HIT → {username}{i}@gmail.com")

print("Finished!!")