# Kirk Sefchik
# UTA ID 1000814472
# 09/05/13
# Description: displays the quotient of n and 25. also displays the remainder
#               (if any)

# Take inputs and perform operations.
denominator = 25
numerator = int(input("n = "))
remainder = numerator % denominator
quotient  = numerator // denominator

# Check for remainder and print results
if remainder == 0:
    print(numerator, "/", denominator, "=", quotient)
else:
    print(numerator, "/", denominator, "=", quotient, "(remainder: ", remainder, ")")