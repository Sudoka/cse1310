# Kirk Sefchik
# UTA ID 1000814472
# 09/05/13
# Description:  takes two integers and a string representing an arithmetic operation
#               prints the operation and its result (or an error if an invalid operation
#               was specified.

x = int(input("Enter the first number: "))
op = input("Enter the operation: ")
y = int(input("Enter the second number: "))
result = 'undefined'

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    if y != 0:
        result = x / y
elif op == '//':
    if y != 0:
        result = x // y
elif op == '**':
    if not (x == 0 and y <= 0):
        result = x ** y
elif op == '%':
    if y != 0:
        result = x % y
else:
    print("This operation is not recognized.")

print(x, op, y, '=', result)