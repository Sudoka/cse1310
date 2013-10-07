# Kirk Sefchik
# UTA ID 1000814472
# 10/03/13
# Description: Task 1 (30 points)

# Given a list listA of numbers, write a program that generates a new list listB with the same number of elements as listA, such that each element in the new list is the average of its neighbors and itself in the original list. For example, if listA = [5, 1, 3, 8, 4], listB = [3.0, 3.0, 4.0, 5.0, 6.0], where the values in listB were computed as follows: 

# (5 + 1)/2 = 3.0 
# (5 + 1 + 3)/3 = 3.0 
# (1 + 3 + 8)/3 = 4.0 
# (3 + 8 + 4)/3 = 5.0 
# (8 + 4)/2 = 6.0 

# listA can be hardcoded at the begining of your program, but the solution should work for other lists as well (in particular if we modify the values of the list, the program should work with the new values).

# Sample run:
# listA = [5, 1, 3, 8, 4]
# listB = [3.0, 3.0, 4.0, 5.0, 6.0]

listA = [5, 1, 3, 8, 4]
listB = []
print("listA =", listA)

for center in range(0, len(listA)):
	# set the bounds of the list to be averaged
	if center - 1 < 0:
		low = 0
	else:
		low = center - 1
	if center + 1 > len(listA):
		high = len(listA)
	else:
		high = center + 1

	avg_list = listA[low:high + 1]
	listB.append(sum(avg_list) / len(avg_list)) 

print("listB =", listB)