'''
Kirk Sefchik
UTA ID 1000814472
10/14/13
Description: Task 3 (55 points)

This task will implement the functionality of creating a list from a string that contains numbers separated by commas (with possibly blank space between them). For example the string "1,2,3, 4.5, 6.7, 8" would become the list: [1, 2, 3, 4.5, 6.7, 8]. Write the following functions:
is_numeric() - This function has a string parameter and returns True if all the characters in the string are digits, comma, space, or dot. If there are any other characters, the function should return False.
string_to_list() - This function takes a string parameter and returns the list of the numbers in the string. First it should call the is_numeric() function to check that the string has no bad characters (e.g. letters). If there are any bad characters, it should return the empty list. If there are no bad characters it should try to build the list out of teh data in the string. For this it should look at every substring between two consecutive commas. If there is no dot in that substring, then the substring should be converted to an integer. If there is exactly one dot (no more, no less) it should be converted into a float. If any of the substrings between two consecutive commas can not be converted to an int or a float (e.g. "4.5.8" as it has too many dots), the function should still return the empty list. Hint: the split() method may be useful for this task.
main() - The main() function that will get a string from the user, it will then call the string_to_list() function to build a list out of the user string and then print the resulting list. It will next ask the user if they want to continue. If they want to continue, they should eneter 'y'. In that case the function (main) should repeat the previous steps: ask the user for an input, convert it to a list, ask the user again if they want to continue. And so on until the user does not want to continue, in which case he or she should enter 'n'.
Sample run
>>> ================================ RESTART ================================
>>> 
Enter a set of numbers (integers or floats) separated by comma: 1,2,3,a
The list is: []
continue ?( y / n):  y
Enter a set of numbers (integers or floats) separated by comma: 1,2,3,4.5.8
The list is: []
continue ?( y / n):  y
Enter a set of numbers (integers or floats) separated by comma: 1,   2,  3 , 4.5, 6
The list is: [1, 2, 3, 4.5, 6]
continue ?( y / n):  n
>>> 

'''

def is_numeric(string):
	for character in string:
		if not character.isnumeric():
			if character == ' ' or character == ',' or character == '.':
				continue
			else:
				return False
	return True

def string_to_list(l):
	if not is_numeric(l):
		return []

	l = l.split(',')
	num_list = []
	for chunk in l:
		chunk = chunk.strip()
		if chunk.count('.') > 1 or ' ' in chunk:
			return []
		elif '.' in chunk:
			num_list.append(float(chunk))
		elif '.' not in chunk:
			num_list.append(int(chunk))

	return num_list

def main():
	''' main program function '''
	while True:
		string = input("Enter a set of numbers (integers or floats) separated by comma: ")
		print("The list is:", string_to_list(string))
		cont = ''
		while cont.lower() != 'y' and cont.lower() != 'n':
			cont = input("continue? (y/n): ")
		if cont.lower() == 'n':
			quit()

main()