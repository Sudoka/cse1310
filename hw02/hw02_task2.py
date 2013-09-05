# Kirk Sefchik
# UTA ID 1000814472
# 09/05/13
# Description:  divides two numbers, inverts them and divides them again,
#               printing the result each time. Checks for division by zero
#               before doing the operation and prints INF if the operation
#               would have resulted in division by zero

a = int(input("a = "))
b = int(input("b = "))

if b == 0:
    print("INF")
else:
    print(a / b)

if a == 0:
    print("INF")
else:
    print(b / a)