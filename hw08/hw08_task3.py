'''
Kirk Sefchik
UTA ID 1000814472
11/13/13
Description: Task 3 (50 points)

(Problem 24, chapter 9, book: "Python 3" by W. Punch and R. Enbody) 
Write a program that reads a word list and prints out, in increasing order of the word length, all the anagrams in the word list. An anagram is a word that contains the same letters but in a different order. Notice that for two words that are anagrams of each other, the listing of their characters in sorted order is identical (it is a way to identify that the two are anagrams of each other). For example the following three words are anagrams: 'enlarge', 'general', 'gleaner'. 
Here is the large text file with words that I have used for the sample run below: words.txt (source: the web). 
Notice that the words file is very large and that the program runs for a long time to produce this data. Consider making and using a smaller file of words. 
If you have a Mac and you had trouble reading the file words.txt, try adding and modifying the following lines in your program:
import codecs
 f= open("words.txt", "r", encoding='unicode_escape')

'''

# len_max was used for testing purposes to truncate the list
def get_sorted_keys(d, len_max):
	res = []
	i = 0
	while i < len_max + 1:
		for key in d.keys():
			if len(key) == i:
				res.append(key)
		i += 1
	return res

def sort_line(line):
	return ''.join(sorted(list(line)))

def match_anagrams(d, ana, found):
	res = []
	ana = sort_line(ana)
	for key in d:
		if d[key] == ana and key not in found:
			res.append(key)
	if len(res) > 1:
		found.extend(res)
		return res
	else:
		return []

def build_word_dict(filename):
	d = {}
	try:
		words_file = open(filename)
	except IOError:
		print("IOError")
		return d
	else:
		i = 0
		for line in words_file:
			d[line.strip()] = sort_line(line.strip())
	finally:
		words_file.close()
		return d

def main():
	d = build_word_dict('words.txt')
	sorted_keys = get_sorted_keys(d, 30)
	found_keys = []
	for key in sorted_keys:
		anagram = match_anagrams(d, key, found_keys)
		if len(anagram) > 1:
			print(anagram)

main()