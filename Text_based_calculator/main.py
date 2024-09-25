#!/usr/bin/env python3
def get_number(number):
    while True:
        operand = input(f"Number {number}: ")
        try:
            return float(operand)
        except:
            print("Invalid number, Try again.")

operand = get_number(1)
operand2 = get_number(2)


sign = input("Sign (+, -, *, /): ")


result = None
match sign:
    case '+':
        result = operand + operand2
    case '-':
        result = operand - operand2
    case '/':
        if operand2 != 0:
            result = operand / operand2
        else:
            print("Division by Zero")
    case '*':
        result = operand * operand2
    case _:
     print("invalid sign")
if result is not None:
    print(result)