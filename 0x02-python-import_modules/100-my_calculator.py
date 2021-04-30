#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    myArgs = sys.argv

    if len(myArgs) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(myArgs[1])
        b = int(myArgs[3])
        operator = myArgs[2]

    if operator not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))

    if operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))

    if operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))

    if operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
