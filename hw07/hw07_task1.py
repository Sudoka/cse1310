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
	for row in table:
		print('|{: >4} '.format(table.index(row) + 1), end='')
		for cell in row:
			print('|{: ^7.2f}'.format(cell), end='')
		print('|')
	print_hr(cols)
	
def save_table(table, file_path):
	''' save a table to disk. overwrites old version without prompting '''
	file_obj = None
	try:
		file_obj = open(file_path, mode='wt')
	except IOError:
		print('Error saving file...')
	
	for row in table:
		for cell in row:
			print(cell, sep='', end='', file=file_obj)
			if row.index(cell) != len(row) - 1:
				print(',', end='', file=file_obj)
		print(file=file_obj)
	file_obj.close()

def save_table_as(table):
	''' save a table to disk under a different file name. prompts for overwrites '''
	file_path = input('Enter a new filename: ')
	import os
	if os.path.exists(file_path):
		while True:
			answer = input('This file already exists. Do you want to overwrite it (y/n)? ')
			if answer.upper() == 'Y':
				save_table(table, file_path)
				return file_path
			if answer.upper() == 'N':
				return ''
	else:
		save_table(table, file_path)
		return file_path

def prompt_element():
	''' prompts the user for a number or column entry '''
	return input('Enter a row (as a number) or a column (as an uppercase letter): ')

def get_element(element, is_row, table):
	''' takes a validated element and boolean that indicates whether the passed element is a 
		row or a column. returns a list represeting the contents of the specified element. '''
	if is_row:
		return table[element].copy()
	else:
		composite_element = []
		for i in range(0, len(table)):
			composite_element.append(table[i][element])
		return composite_element

def validation_error():
	''' helper. prints an error message. returns (None, None) '''
	print('Invalid selection')
	return (None, None)

def validate_element(element_string, table):
	''' takes an unverified element as either a string or integer. 
		returns a tuple containing a valid element index and boolean that indicates 
		whether it represents a row or a column. prints an error message and
		returns a (None, None) tuple if the element would generate an IndexError '''

	# convert element to a column number if nescessary or an integer if it refers to a row
	is_row = None
	element = None
	try:
		element = int(element_string)
	except ValueError:
		# it could be a letter...
		element = char_to_col_num(element_string)
		is_row = False
	else:
		element -= 1
		is_row = True

	# throw out obvious errors
	if is_row:
		if element < 0 or element > len(table):
			return validation_error()
	else:
		try:
			table_len = len(table[0])
		except IndexError:
			table_len = 0
		if element < 0 or element > table_len:
			return validation_error()

	# test out the element to see if its valid. Guarantees no IndexErrors.
	try:
		if is_row:
			table[element][0]
		else:
			table[0][element]
	except IndexError:
		return validation_error()
	else:
		return (element, is_row)

def print_minimum(table):
	''' takes a table. prompts user for column or row entry. returns the minimum value across specified element. '''
	element, is_row = validate_element(prompt_element(), table)
	if element == None:	
		return

	element = get_element(element, is_row, table)
	minimum = element[0]
	for number in element:
		if number < minimum:
			minimum = number
	print('Minimum is:', minimum)

def print_maximum(table):
	''' takes a table. prompts user for column or row entry. returns the maximum value across specified element. '''
	element, is_row = validate_element(prompt_element(), table)
	if element == None:	
		return

	element = get_element(element, is_row, table)
	maximum = element[0]
	for number in element:
		if number > maximum:
			maximum = number
	print('Maximum is:', maximum)

def delete_element(table):
	''' takes a table. prompts user for column or row entry. deletes the specified element from the table. '''
	element, is_row = validate_element(prompt_element(), table)	
	if element == None:	
		return

	if is_row:
		del table[element]
	else:
		for row in table:
			del row[element]

def print_sum(table):
	''' takes a column or row. returns the sum of those elements '''
	element, is_row = validate_element(prompt_element(), table)	
	if element == None:	
		return
	
	element = get_element(element, is_row, table)
	my_sum = 0
	for number in element:
		my_sum += number
	print('The sum is:', my_sum)

def main():
	''' main function. executes all other functions '''
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
		elif choice == 2:
			print_minimum(table)
		elif choice == 3:
			print_maximum(table)
		elif choice == 4:
			print_sum(table)
		elif choice == 5:
			delete_element(table)
		elif choice == 6:
			save_table(table, table_path)
		elif choice == 7:
			new_path = save_table_as(table)
			if new_path != '':
				table_path = new_path
		else:
			print("Invalid selection")

main()