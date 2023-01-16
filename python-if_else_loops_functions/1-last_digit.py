#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute = number % 10
absoluteString = ''
if (number < 0):
    absolute = number * -1 % 10
    absoluteString = '-'

if (number % 10 > 5):
    print('Last digit of', number, 'is',
    absoluteString + str(absolute), 'and
    is greater than 5')

if (number % 10 < 5 and absolute % 10 > 0):
    print('Last digit of', number, 'is',
    absoluteString + str(absolute), 'and
    is less than 6 and not 0')

if (number % 10 == 0):
    print('Last digit of', number, 'is', absolute, 'and is 0')
