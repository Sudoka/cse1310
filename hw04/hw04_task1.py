# Kirk Sefchik
# UTA ID 1000814472
# 09/26/13
# Description: 
# Problem 36, page 223 (second edition). Generate the following table. You do 
# not need to generate the numbers in the table, just to print them. However you
# must use the string formatting to make your table look like the one shown. If 
# you print the hardcoded lines 
#  (e.g., 'print("|Methane | -162.00 | -183.00|")' ), you will get no credit for
# this assignment. Your solution must use the format() method from strings to 
# generate each line that will be printed. The table must have the following 
# format:
#
# In the table header, all column names must be centered.
# The data in the left column of the table must be left alligned.
# The data in the center column of the table must be centered.
# The data in the right column of the table must be right alligned.
# Print the numbers in the table as floats, not as strings.
# Sample run:
# >>> ================================ RESTART ================================
# >>> 
# Melting and Boiling Points of Alkanes:
# ------------------------------------------------------------
# |  Name   | Melting Point (deg C)  | Boiling Point (deg C) |
# ------------------------------------------------------------
# |Methane  |        -162.00         |                -183.00|
# |Ethane   |         -89.00         |                -172.00|
# |Propane  |         -42.00         |                -188.00|
# |Butane   |         -0.50          |                -135.00|
# ------------------------------------------------------------

col1 = 9
col2 = 24
col3 = 23
table_width = 60
line = table_width * '-'

print(line)
fmt = '|{:^{col1}}|{:^{col2}}|{:^{col3}}|'
print(fmt.format('Name', 'Melting Point (deg C)','Boiling Point (deg C)', 
	col1=col1, col2=col2, col3=col3))
print(line)

fmt = '|{:<{col1}}|{:^{col2}.2f}|{:>{col3}.2f}|'
print(fmt.format('Methane', -162.0, -183.0, col1=col1, col2=col2, col3=col3))
print(fmt.format('Ethane', -89.0, -172.0, col1=col1, col2=col2, col3=col3))
print(fmt.format('Propane', -42.0, -188.0, col1=col1, col2=col2, col3=col3))
print(fmt.format('Butane', -0.5, -135.0, col1=col1, col2=col2, col3=col3))
print(line)