def print_menu():
	''' print the application menu '''
	menu = """1 - Open and load from a file
2 - Minimum
3 - Maximum 
4 - Sum 
5 - Delete
6 - Save
7 - Save as (specify new file name)
0 - Exit"""
	print(menu)

def menu_prompt():
	''' prompts the user for their menu choice. error checks, returns result '''
	try:
		choice = int(input("Your choice: "))
	except ValueError:
		choice = -1
	return choice

def is_valid_table(table):
	''' check a loaded table to make sure it's a valid table '''
	if not len(table):
		print('Data could not be loaded (table is empty)')
		return False
	
	try:
		cols = len(table[0])
	except IndexError:
		print('Data could not be loaded (empty zero index)')
		return False
	
	for row in table:
		if len(row) != cols:
			print('Data could not be loaded (the number of columns is not the same for all rows)')
			return False

	return True

def parse_file(file_obj):
	''' transform a table into a list of lists '''
	table = []
	for line in file_obj.readlines():
		line = line.strip().split(',')
		new_line = []
		for item in line:
			new_line.append(float(item))	
		table.append(new_line)

	if not is_valid_table(table):
		return []
	else:
		return table

def open_file():
	''' load a file and return a dictionary object representing the table 
		returns an empty table on errors '''
	file_path = input('Enter a filename (if you hit enter, data1.txt will be opened): ')
	if file_path == '':
		file_path = 'data1.txt'
	try:
		file_obj = open(file_path)
	except IOError:
		print('File could not be opened.')
		table = []
		file_path = ''
	else:
		table = parse_file(file_obj)
		file_obj.close()
	finally:
		return (table, file_path)

def print_hr(cols):
	''' prints a horizontal rule commesurate to the number of columns in the table '''
	print('-' * 7, end='')
	for i in range(0, cols):
		print(('-' * 8), end='')
	print()

def print_col_header(cols):
	''' prints a lettered table header '''
	import string
	print_hr(cols)
	print('|'+(' ' * 5), end='')
	for i in range(0, cols):
		print('|{: ^7}'.format(string.ascii_uppercase[i]), end='')
	print('|')
	print_hr(cols)

def char_to_col_num(character):
	''' converts a column letter to the corresponding column number '''
	if len(character) > 1 or not character.isalpha():
		return None
	if not character.isupper():
		character = character.upper()

	return ord(character) - ord('A')

def print_table(table):
	''' print a copy of a table '''
	print('\n' * 3)
	if table == []:
		return

	cols = len(table[0])
	print_col_header(cols)
	i = 0
	for row in table:
		print('|{: >4} '.format(table.index(row)), end='')
		for cell in row:
			print('|{: ^7.2f}'.format(cell), end='')
		print('|')
	print_hr(cols)
	
def save_table():
	''' save a table to disk. overwrites old version without prompting '''
	pass

def save_table_as():
	''' save a table to disk under a different file name. prompts for overwrites '''
	pass

def prompt_element():
	''' prompts the user for a number or column entry '''
	return input('Enter a row (as a number) or a column (as an uppercase letter): ')

def get_element(element, is_row):
	''' takes a validated element and boolean that indicates whether the passed element is a 
		row or a column. returns a list represeting the contents of the specified element. '''
	pass

def validate_element(element, table):
	''' takes an unverified element as either a string or integer. 
		returns a tuple containing a valid element index and boolean that indicates 
		whether it represents a row or a column. returns None if the element would generate
		an IndexError '''
	is_row = None
	try:
		element = int(element)
	except ValueError:
		# it could be a letter...
		element = char_to_col_num(element)
		is_row = False
	else:
		is_row = True
	


def get_minimum(table):
	''' takes a table. promputs user for column or row entry. returns the minimum value across specified element. '''
	element = prompt_element()
	element, is_row = validate_element(element, table)



def get_maximum():
	''' takes a column or row. returns the maximum value across that element.'''
	pass

def delete_element():
	''' takes a column or row. deletes that element '''
	pass

def sum_element():
	''' takes a column or row. returns the sum of those elements '''
	pass

def main():
	''' main function. executes all other functions '''
	import os
	table = []
	table_path = ''

	while True:
		print_table(table)
		print_menu()
		choice = menu_prompt()
		if choice == 0:
			quit()
		elif choice == 1:
			table, table_path = open_file()
		else:
			print("Invalid selection")

main()