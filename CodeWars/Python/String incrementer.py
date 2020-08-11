# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(string):
    List = []
    for char in string:
    	if char.isdigit():
        	strVal = str(char)
        	List.append(str(strVal))
        	for i in List:
        		if i.isdigit() ==
        	newstring = ''.join(List)
        	print(newstring)

        	intstr = int(newstring) + 1
        	print(intstr)
    return string

print(increment_string("Hello00009"))