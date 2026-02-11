#!/usr/bin/env python3
print("Enter a number")
number = int(input())
i = 0
while i < 10:
    result = i * number
    print(str(i) + " x " + str(number) + " = " + str(result))
    i += 1