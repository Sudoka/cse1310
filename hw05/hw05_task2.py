# Kirk Sefchik
# UTA ID 1000814472
# 10/03/13
# Description: Task 2 (35 points)

# Given a list L, and an element x, create a new list, L_indexes, that has the indexes (positions) of the occurrences of x in L. At the end, print a message about how many occurences were found and what they were (that is the L_indexes list). If x is not found in L, print a message about that. For example, for L = [4, 10, 4, 2, 9, 5, 4 ], and x = 4 we find 3 occurences of 4 in L and they are at positions [0,2,6]. The element 2 has 1 occurence in L and that is at position: [3]. The element 7 has no occurences in L (and thus L_indexes for it will be []). 

# L can be hardcoded at the begining of your program, but the solution should work for other lists as well (in particular if we modify the values in the list the program should work with the new values). 

# Sample run
# L =  [4, 10, 4, 2, 9, 5, 4]
# Enter an element to search for in the list: 3
# 3  does not occur in L.

# Sample run
# L =  [4, 10, 4, 2, 9, 5, 4]
# Enter an element to search for in the list: 4
# 4 occurs in L at the following positions:  [0, 2, 6]

L =  [4, 10, 4, 2, 9, 5, 4]
print("L =", L)
x = int(input("Enter an element to search for in the list: "))
L_indexes = []

if (x not in L):
	print(x, "does not occur in L.")
	quit()

for i in range(0, len(L)):
	if L[i] == x:
		L_indexes.append(i)

print(x, "occurs in L at the following positions:", L_indexes)