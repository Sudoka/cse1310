'''
Kirk Sefchik
UTA ID 1000814472
10/14/13
Description: Task 2 (35 points)

Given a list of N numbers, write a function to shift the numbers circularly by some integer k (where k < N). The function should take the list and k as arguments and return the shifted list. 
a) Write a function that assumes the shifting is to the left. It should not print anything. 
b) Write a function that takes a third argument that specifies shifting left or right. It should not print anything. Perform whatever error-checking you consider necessray. 
c) Write a main() function that calls the above functions. It should print the lists both before and after shifting. Perform whatever error-checking you consider necessray. 
Name your file hw06_task2.py.
Sample run 
>>> ================================ RESTART ================================
>>> 
original list:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shifted by 4, to the left: [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
shifted by 4, to the right: [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

'''
def shift_list_left(l, shift):
	''' shifts a list a number of elements to the left '''
	if shift < 0:
		shift = int(-shift)
	if not l:
		return []
		
	new_list = l[:]
	for i in range(0, len(l)):
		new_list[i] = l[i+(shift-len(l))]
	return new_list

def shift_list(l, shift, left):
	''' shifts a list a number of elements to the left or right '''
	if shift < 0:
		shift = int(-shift)
	if not l:
		return []
	if left:
		return shift_list_left(l, shift)

	new_list = l[:]
	for i in range(0, len(l)):
		new_list[i] = l[i-shift]
	return new_list

def main():
	''' main program function '''
	l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print('original list:', l)
	print('shifted by 4 to the left:', shift_list_left(l, 4))
	print('shifted by 4 to the right:', shift_list(l, 4, False))

main()