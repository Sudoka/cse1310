# Kirk Sefchik
# UTA ID 1000814472
# 09/12/13
# Description: Write a program that takes a positive integer N and computes 
# the following sum: 
# 1 - 2 + 3 - 4 + 5 - 6 + .... N. 
# It should show both the summation and the computed sum. 
# It should also show two other sums: the sum of the values that 
# are being added and the sum of those that are being subtracted. 

# keep bugging user until I get a nonzero positive integer
n = 0
while not n >= 1: 
    n = int(input("Enter N: "))

result = 1      # Stores the final result of the calculation
i = 2           # counts up through n and terminates the loop
pos_sum = 1     
neg_sum = 0
print(result, end="")
while i <= n:
    if i % 2 == 0:
        #evens
        print(" -", i, end="")
        result -= i
        neg_sum += i
    else:
        print(" +", i, end="")
        result += i
        pos_sum += i
    i += 1

print(" =", result)
print("The positive sum is:", pos_sum)
print("The negative sum is:", neg_sum)