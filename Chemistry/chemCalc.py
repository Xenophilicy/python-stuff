import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

def plot(title, maxY, a, b, filename):
    plt.clf()
    plt.title(title)
    plt.xlabel('Time (Iteration)')
    plt.ylabel('Bean Count (Rounded)')
    plt.xlim([0,15])
    plt.ylim([0,maxY])
    plt.plot(range(0,16),a)
    plt.plot(range(0,16),b)
    plt.savefig(f'C:/Users/xenop/Desktop/{filename}.png')

print("------- Part 1 -------")
a = 100;
b = 0;
aStack = [a]
bStack = [b]
print(f"Pass 0 | A: {a} B: {b}")
for i in range(1,16):
    diff = round(.1*a)
    a -= diff
    b += diff
    aStack.append(a)
    bStack.append(b)
    print(f"Pass {i} | A: {a} B: {b} (Net: {diff})")
plot("Part 1", 100, aStack, bStack, "part1")

print("------- Part 2 -------")
a = 100;
b = 0;
aStack = [a]
bStack = [b]
print(f"Pass 0 | A: {a} B: {b}")
for i in range(1,16):
    diffA = round(.1*a)
    diffB = round(.1*b)
    a = (a-diffA)+diffB
    b = (b-diffB)+diffA
    aStack.append(a)
    bStack.append(b)
    print(f"Pass {i} | A: {a} B: {b} (Net: {diffA-diffB})")
plot("Part 2", 100, aStack, bStack, "part2")

print("------- Part 3 -------")
a += 20
aStack = [a]
bStack = [b]
print(f"Pass 0 | A: {a} B: {b}")
for i in range(1,16):
    diffA = round(.1*a)
    diffB = round(.1*b)
    a = (a-diffA)+diffB
    b = (b-diffB)+diffA
    aStack.append(a)
    bStack.append(b)
    print(f"Pass {i} | A: {a} B: {b} (Net: {diffA-diffB})")
plot("Part 3", 120, aStack, bStack, "part3")