#!/usr/bin/python3
numbers = [i for i in range(10)]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        print("{}{}".format(numbers[i], numbers[j]), end = ', ')
