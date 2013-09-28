# Kirk Sefchik
# UTA ID 1000814472
# 09/26/13
# Description: 
# Write a program that plays the number-guessing game. It will ask the user to 
# choose (think of) a number between 1 and 100 inclusive. Let's name it N. Then it 
# will try to guess N by the following algorithm that always removes half of the 
# possible numbers.

# o At first the computer will ask the user if the number is less than or equal to 
# 	50 ( because 50 is the middle value in the original inteval [1,100])
# o If the user answers 'y' or 'Y' (for 'yes'), you should update the interval of 
# 	possible nubmers to be [1,50] (because you know that the number is not greater 
# 	than 50).
# o If the user answers 'n' or 'N' (for 'no'), you should update the interval of 
# 	possible nubmers to be [51,100] (because you know that the number is strictly 
# 	greater than 50).
# o Next you estimate the middle point of the new interval and ask again if N is 
# 	less or equal to the new middle point.
# o Based on the user's answer, you update the interval again.
# o You keep repeating this process until you find the number (which happens when 
#	your interval of possible numbers contains only one number).

# In addition to implementing the algorithm, your program must also follow these 
# conventions:
# o It will accept 'y' or 'Y' for the answer 'yes'. Do not use '1', 'yes' or anything else.
# o It will accept 'n' or 'N' for the answer 'no'. Do not use '0', 'no' or anything 
# 	else.
# o It will print the current interval. In the example below, the first line
# 		interval: [1,100]. Is your number <= 50? y
# 	indicates that the current interval is [1,100] and the middle point of it is 50. 
# 	The computer is asking me if my number is in the first half of the 
# 	interval : <= 50. My number (11) was in the first half, so I answered 'y'.

# Hint: You can represent an interval by the first and last number of the interval. 
# For example the interval [1,100] has all the numbers between 1 and 100 inclusive 
# so I can represent it with the first value, 1, and the last value, 100. And I know
# that N must be between these two values. 

# Here is a sample run. The number that I thought of, was 11. The computer guessed it.
# Think of a number between 1 and 100 (inclusive).
# Answer the following questions with letters y or Y for yes and n or N for no.
# interval: [1,100]. Is your number <= 50? y
# interval: [1,50]. Is your number <= 25? y
# interval: [1,25]. Is your number <= 13? y
# interval: [1,13]. Is your number <= 7? n
# interval: [8,13]. Is your number <= 10? n
# interval: [11,13]. Is your number <= 12? y
# interval: [11,12]. Is your number <= 11? y
# Your number is:  11

print("Think of a number between 1 and 100 (inclusive).")
print("Answer the following questions with letters y or Y for yes and n or N for no.")

lower_bound = 1
upper_bound = 100

while upper_bound != lower_bound:
	guess = ((upper_bound - lower_bound) // 2) + lower_bound
	prompt = "interval: [{lower}, {upper}]. Is your number <= {guess}? "
	answer = input(prompt.format(lower=lower_bound, upper=upper_bound, guess=guess))
	if answer.lower() == 'y':
		upper_bound = guess
	elif answer.lower() == 'n':
		lower_bound = guess + 1
print("Your number is: ", lower_bound)