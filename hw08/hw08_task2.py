'''
Kirk Sefchik
UTA ID 1000814472
11/13/13
Description: Task 2 (35 points) - Morse code

(problem 21, chapter 9, book: "Python 3" by W. Punch and R. Enbody, applied to the International Morse Code listed on wiki) 

Morse code uses a series of short and long pulses called dots and dashes, respectively, to encode letters and digits. For example the letter 'A' is 'dot-dash', 'B' is 'dash-dot-dot-dot', 'C' is 'dash-dot-dash-dot'. 

Write a function named 'build_dictionary()' that takes no arguments. This function should read the data from file Morse.txt and create a dictionary for mapping characters and digits to Morse Code. It should return the dictionary. Notice that in the Morse.txt file the English letters are separated by the Morse code character sequence by a tab.

Write another function named 'translate()' that takes 2 arguments: the dictionary and an English word. This function should use the dictionary to create and return the Morse Code representation of that word. In the Morse code word, separate the character-strings by spaces (for example the Morse code for the word 'CAB' is 'dash-dot-dash-dot dot-dash dash-dot-dot-dot' and your function should return the string '-.-. .- -...' (notice the spaces seprating C from A and A from B). This function should be able to translate a word that contains both uppercase and lowercase characters (that is, it should be able to translate all of the following words: CAB, cab, Cab, cAb).

Write a main() function that creates the dictionary and then uses it to translate the following 3 words: cab, tin, sunny.

You can find the international Morse code on the wikipedia at: http://en.wikipedia.org/wiki/Morse_code.

Sample run:

cab:    -.-. .- -...
Tin:    - .. -.
suNny:  ... ..- -. -. -.--

'''

def build_dictionary():
	morse_dict = {}
	morse_file = open('morse.txt')
	for line in morse_file:
		morse_dict[line.split()[0].lower()] = line.split()[1]
	morse_file.close()
	return morse_dict

def translate(d, word):
	word = word.lower()
	res = ''
	for char in word:
		res += d[char] + ' '
	return res.strip()

def main():
	dicti = build_dictionary()
	print(translate(dicti, 'cab'))
	print(translate(dicti, 'Tin'))
	print(translate(dicti, 'suNny'))

main()