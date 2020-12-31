import sys
import time

from pynput.keyboard import Key, Controller as KController
from pynput.mouse import Controller as MController


def hit(key):
    keyboard.press(key)
    time.sleep(.1)
    keyboard.release(key)


delay = 0

keyboard = KController()
mouse = MController()

count = int(input("How many messages would you like deleted?\n>>"))

print("Select the window now...")
for i in range(-5, 0):
    sys.stdout.write(f"\rWaiting {-i} seconds...")
    time.sleep(1)
sys.stdout.write(f"\rOkay, deleting {count} messages...\n")
total = 0
before = time.time()
while total != count:
    start = time.time()
    time.sleep(.1)
    hit(Key.enter)
    hit(Key.backspace)
    time.sleep(.1)
    hit(Key.up)
    time.sleep(.1)
    keyboard.press(Key.ctrl)
    hit("a")
    keyboard.release(Key.ctrl)
    hit(Key.backspace)
    hit(Key.enter)
    time.sleep(.2)
    hit(Key.enter)
    delta = (time.time() - start) * 1000
    delay += delta
    total += 1
    print(f"\rFinished pass #{total}")
after = round((time.time() - before), 2)
perPass = round(delay / count, 2)

print(f"Deleted {total} message(s)!")
print(f"Average pass: {perPass} ms")
print(f"Total duration: {after} seconds")
input("Press enter to close")
