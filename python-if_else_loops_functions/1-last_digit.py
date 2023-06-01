#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnumber = abs(number) % 10
if (number < 0):
    if (absnumber == 0):
        print("Last digit of",number," is",absnumber, "and is 0")
    else:
        
        print("Last digit of",number,"is","-" + str(absnumber),"and is less than 6 and not 0")
if (number > 0):
    if (absnumber == 0):
        print("Last digit of",number,"is",absnumber, "and is 0")
    elif (absnumber > 0 and absnumber < 6):
        print("Last digit of",number,"is",absnumber, "and is less than 6 and not 0")
    else:
       print("Last digit of",number,"is",absnumber, "and is greater than 5")