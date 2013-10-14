'''
Kirk Sefchik
UTA ID 1000814472
10/14/13
Description: Task 1 (10 pts): A very simple function

a) Write a function, 'my_sum()', that takes two arguments and returns the sum of her arguments. Your function should not print anything.
b) Write the main() function. It should get two user inputs (as either int or float) and call your function to add them. Print the result. 
Name your file hw06_task1.py.
	Here are 2 sample runs:
>>> ================================ RESTART ================================
>>> 
Enter the first number: 2
Enter the second number: 3
2 + 3 = 5
>>> ================================ RESTART ================================
>>> 
Enter the first number: 1
Enter the second number: -3
1 + -3 = -2
>>> ================================ RESTART ================================
>>> 
Enter the first number: 3
Enter the second number: 6
3 + 6 = 9
>>> ================================ RESTART ================================
>>> 
Enter the first number: -1
Enter the second number: -2
-1 + -2 = -3	

'''

def my_sum(x, y):
	''' returns the sum of two numbers '''
	return x + y

def main():
	''' main program function '''
	x = int(input("Enter the first number: "))
	y = int(input("Enter the second number: "))

	print(x, "+", y, "=", my_sum(x, y))

main()