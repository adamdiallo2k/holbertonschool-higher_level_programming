#!/usr/bin/python3
numbers = [i for i in range(10)]
output = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        output.append("{}{}".format(numbers[i], numbers[j]))
print(", ".join(output))
