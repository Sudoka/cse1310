# Kirk Sefchik
# UTA ID 1000814472
# 09/26/13
# Description: Write a program that does the following:

# Asks the user to enter a string.

# Asks the user to enter a strictly positive (strictly greater than 0) 
# integer. If the user does not enter a good value, the program should display 
# an error message and prompt the user for the integer again. The program 
# should keep on like this until the user enters a strictly positive integer. 

# You can assume the user will always enter integers, you just have to check 
# that they are strictly greater than zero. We will refer to this integer as 
# step.

# If the length of the string is even the program should print the second half 
# of the string and then the first half.
# If the length of the string is odd, the program should print the middle 
# letter, than the second half, and then the first half.

# Next it should print every step-th letter and a message explaining that. The 
# message will depend on the value of step as follows:
# when step is 1, it should say: "Every letter and it's index are:"
# when step is 2, it should say: "Every second letter and it's index are:"
# when step is 3, it should say: "Every third letter and it's index are:"
# for all other values for step it should say: "Every step-th letter and it's 
# index are:" (See sample runs.)

# Finally the program should print every step-th letter (starting from the 
# first one) and the corrsponding index, one letter-index pair per line.

# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abc
# Enter a step: -1
# Error. The step should be strictly greater than 0.
# Enter a step: 0
# Error. The step should be strictly greater than 0.
# Enter a step: -4
# Error. The step should be strictly greater than 0.
# Enter a step: 5
# b
# c
# a
# Every 5-th letter and it's index are:
# a 0
# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abcde
# Enter a step: 2
# c
# de
# ab
# Every second letter and it's index are:
# a 0
# c 2
# e 4
# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abcd
# Enter a step: 3
# cd
# ab
# Every third letter and it's index are:
# a 0
# d 3
# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abcd
# Enter a step: 1
# cd
# ab
# Every letter and it's index are:
# a 0
# b 1
# c 2
# d 3
# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abcd
# Enter a step: 2
# cd
# ab
# Every second letter and it's index are:
# a 0
# c 2
# >>> ================================ RESTART ================================
# >>> 
# Enter a string: abcd
# Enter a step: 4
# cd
# ab
# Every 4-th letter and it's index are:
# a 0
# >>>

string = input("Enter a string: ")
while True:
	step = int(input("Enter a step: "))
	if not step > 0:
		print("Error. The step should be strictly greater than 0.")
	else:
		break

if len(string) % 2 == 0:
	print(string[len(string) // 2: len(string)])
	print(string[0:len(string) // 2])
else:
	print(string[len(string) // 2])
	print(string[(len(string) // 2) + 1: len(string)])
	print(string[0:len(string) // 2])

if step == 1:
	print("Every letter and it's index are:")
elif step == 2:
	print("Every second letter and it's index are:")
elif step == 3:
	print("Every third letter and it's index are:")
else:
	print("Every {step}-th letter and it's index are:".format(step=step))

i = 0
for letter in string[::step]:
	print(letter, i)
	i += step