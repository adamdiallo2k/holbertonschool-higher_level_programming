#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute = number
if (number < 0):
    absolute = number * -1
if (absolute % 10 > 5):
    print('Last digit of', number,'is',absolute % 10,'and is greater than 5')
if (absolute % 10 < 5 and absolute % 10 > 0):
    print('Last digit of', number,'is',absolute % 10,'and is less than 5')
if (absolute % 10 == 0) :
    print('Last digit of', number,'is',absolute % 10,'and is 0')
