import random

includeLetters = False
includeNumbers = False
valid = False

def genPassword():
    pwd = ""
    for char in range(0,int(length)):
        char = random.choice(bagString)
        pwd += char
    return pwd

letters = "abcdefghijklmnopqrstuvwxyz"
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
bagString = ""

while valid == False:
    try:
        length = input("How long would you like your password to be?\nThe password must be at least 6 characters.\n>>")
        if int(length) >= 6:
            valid = True
            print(f"Okay, your password will be {length} characters long.")
        else:
            print("Whoops, that's invalid! Please choose a length of at least 6 characters.")
            continue
    except Exception:
        print("Whoops, that's invalid! Please enter a numerical value.")
        continue

valid = False
while valid == False:
    try:
        charType = input("What would you like your password to be made up of?\nYour choices are Letters, Numbers, or Both.\n>>")
        if charType.lower() == "both":
            includeNumbers = True
            includeLetters = True
            valid = True
            print(f"Okay, your password will be made of both letters and numbers.")
        elif "number" in charType.lower():
            includeNumbers = True
            valid = True
            print(f"Okay, your password will be made of only numbers.")
        elif "letter" in charType.lower():
            includeLetters = True
            valid = True
            print(f"Okay, your password will be made of only letters.")
        else:
            print("Whoops, that's invalid! Please choose one of the three character types.")
            continue
    except Exception:
        print("Whoops! Please choose one of the three character types.")
        continue
includeCapitals = False
if includeLetters == True:
    valid = False
    while valid == False:
        cap = input("Would you like to include capital letters?\nType Yes or No for an answer.\n>>")
        if cap.lower() == "yes":
            valid = True
            print("Okay, capital letters will be included in your password.")
            includeCapitals = True
            bagString += capitals
        elif cap.lower() == "no":
            valid = True
            print("Okay, capital letters won't be included in your password.")
            
        else:
            print("Whoops, that's invalid! Please choose yes or no.")
            continue

valid = False
while valid == False:
    if includeLetters == True and includeNumbers == True:
        desiredLetterCount = input("How many letters would you like in your password?\n>>")
        desiredNumberCount = input("How many numbers would you like in your password?\n>>")
        bagString += letters + numbers
    else:
        if includeLetters == True:
            desiredLetterCount = int(length)
            desiredNumberCount = 0
            bagString += letters
            break
        else:
            desiredNumberCount = int(length)
            desiredLetterCount = 0
            bagString += numbers
            break
    if not int(desiredLetterCount)+int(desiredNumberCount) == int(length):
        print(f"Your character counts must add up to {length}, please try again.")
        continue
    else:
        print(f"Okay, your password will have {desiredLetterCount} letter(s) and {desiredNumberCount} number(s).")
        valid = True
print(f"Password settings:\nLength: {length}\nChar Type: {charType}\nLetters: {desiredLetterCount}\nNumbers: {desiredNumberCount}\n")
print("Generating password...\n")
correct = False
attempts = 0
while correct == False:
    attempts+=1
    foundLetters = 0
    foundNumbers = 0
    pwd = genPassword()
    if includeLetters == True:
        for char in pwd:
            if char.lower() in list(letters):
                foundLetters += 1
        if not foundLetters == int(desiredLetterCount):
            continue
    if includeNumbers == True:
        for char in pwd:
            if char in list(numbers):
                foundNumbers += 1
        if not foundNumbers == int(desiredNumberCount):
            continue
    hit = False
    if includeCapitals == True:
        for char in pwd:
            if char in list(capitals):
                hit = True
                break
        if hit == False:
            continue
    correct = True
print(f"Finished! (Tried {attempts} iterations)")
print(f"Your password is: {pwd}")