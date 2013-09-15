# Kirk Sefchik
# UTA ID 1000814472
# 09/12/13
# Description: write a program that takes an integer N as input. If N is between 1
# and 100 (inclusive), it prints out (on a single line) all the divisors of N. 
# Input validation: If N is outside the [1,100] interval, your program should 
# display an error message and keep asking for a valid N 

n = 0
running = True
while running:
    n = int(input("Enter N: "))
    if n >= 1 and n <= 100:
        i = 1
        print("The divisors of N are: ", end="")
        while i <= n:
            if n % i == 0:
                print(i, end=" ")
            i += 1
        running = False
    else:
        print("Error. Please enter only numbers in the range [1, 100].")
print()