#!/usr/bin/env python3
first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
result = first_num * second_num
print(str(first_num) + " x " + str(second_num) + " = " + str(result))
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")