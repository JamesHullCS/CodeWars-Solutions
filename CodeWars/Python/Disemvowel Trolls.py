# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

# James Hull

# Original Solution
def disemvowel(string):
	return string.translate(string.maketrans({'A': '', 'a': '','E': '', 'e': '','I': '', 'i': '','o': '', 'O': '','e': '', 'E': '','U': '', 'u': ''}))