# Kirk Sefchik
# UTA ID: 1000814472
# 08/29/13
# Desc: Performs the following numeric operations on two input variables
#       multiplication, division, floor division, modulus, power of

# Get (and convert) numbers from user
x = float(  input('Enter the first number   --> '))
y = float(  input('Enter the second number  --> '))

# Do operations and print results
print(x, '*', y, '=', x * y)
print(x, '/', y, '=', x / y)
print(x, '//', y, '=', x // y)
print(x, '%', y, '=', x % y)
print(x, '**', y, '=', x ** y)