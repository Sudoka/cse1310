# Kirk Sefchik
# UTA ID 1000814472
# 09/05/13
# Description: takes three integers and prints the smallest one

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

smallest = 0
if a <= b:
    smallest = a
else:
    smallest = b
    
if c <= smallest:
    smallest = c
    
print(smallest)
    