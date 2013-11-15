'''
Kirk Sefchik
UTA ID 1000814472
11/13/13
Description: Task 1 (15 points): Basic operations

(problem 8, chapter 9, book: "Python 3" by W. Punch and R. Enbody) 
Given the following dictionary,
d = {'a':15, 'c':35, 'b':20}
write Python code to print all the:
keys
values
key and value pairs
key and value pairs in order of key
key and value pairs in order of value

You can write all this code in the main function (you do not need 
to write a special function for each requirement, but you are 
welcome to do it if you prefer so).

'''

def main():
	d = { 'a':15, 'c':35, 'b':20 }

	# Keys
	for key in d.keys():
		print(key)

	# Values
	for value in d.values():
		print(value)

	# Key and Value Pairs
	for key, value in d.items():
		print(key, value)

	# Key and Value Pairs in order of key
	for key in sorted(d.keys()):
		print(key, d[key])

	# Key and Value pairs in order of value
	for value in sorted(d.values()):
		for key in d:
			if d[key] == value:
				print(key, value)
				
main()