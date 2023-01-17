#!/usr/bin/python3
numbers = [i for i in range(10)]
output = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        output.append(f"{numbers[i]:d}{numbers[j]:d}")
print(", ".join(output))
